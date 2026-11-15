import tkinter as tk
from tkinter import ttk, messagebox
from algorithms.fcfs import run_fcfs
from algorithms.sjf import run_sjf
from algorithms.srtf import run_srtf
from algorithms.round_robin import run_round_robin

GANTT_COLORS = ["#637545", "#9BA685", "#C2A878", "#7D8F69", "#A3B18A", "#B5836D", "#8A9A5B"]


class CPUSchedulerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("GROUP 9: CPU SCHEDULING")
        self.root.geometry("880x580")
        self.root.configure(bg="#EBEBD8")

        self.process_rows = []
        self._build_ui()

        # sample process
        self.add_process_row("0", "6")
        self.add_process_row("2", "4")
        self.add_process_row("4", "2")

    def _build_ui(self):
        # header bar
        header = tk.Frame(self.root, bg="#455230", pady=12)
        header.pack(fill="x")
        tk.Label(
            header, text="GROUP 9: CPU SCHEDULING SIMULATION",
            font=("Segoe UI", 12, "bold"), bg="#455230", fg="#EBEBD8"
        ).pack(side="left", padx=20)

        self.status_badge = tk.Label(
            header, text="READY", font=("Segoe UI", 9, "bold"),
            bg="#637545", fg="#EBEBD8", padx=10, pady=2
        )
        self.status_badge.pack(side="right", padx=20)

        # two columns
        main_frame = tk.Frame(self.root, bg="#EBEBD8", padx=18, pady=15)
        main_frame.pack(fill="both", expand=True)

        # algorithms, time quantum
        left = tk.Frame(main_frame, bg="#F7F7EE", highlightbackground="#9BA685", highlightthickness=1, padx=14, pady=14)
        left.pack(side="left", fill="y", padx=(0, 14))

        tk.Label(left, text="Algorithm:", font=("Segoe UI", 10, "bold"), bg="#F7F7EE", fg="#455230").pack(anchor="w")
        self.algo_var = tk.StringVar(value="FCFS")
        self.algo_combo = ttk.Combobox(
            left, textvariable=self.algo_var, state="readonly", width=22,
            values=["FCFS", "SJF", "SRTF", "Round Robin", "Compare All"]
        )
        self.algo_combo.pack(fill="x", pady=(4, 10))
        self.algo_combo.bind("<<ComboboxSelected>>", self._toggle_quantum)

        q_frame = tk.Frame(left, bg="#F7F7EE")
        q_frame.pack(fill="x", pady=(0, 14))
        tk.Label(q_frame, text="Time Quantum (RR):", font=("Segoe UI", 9, "bold"), bg="#F7F7EE", fg="#455230").pack(side="left")
        self.quantum_entry = tk.Entry(q_frame, width=6, justify="center", bg="#EBEBD8", fg="#2C351E", relief="solid", bd=1)
        self.quantum_entry.insert(0, "2")
        self.quantum_entry.pack(side="right")
        self._toggle_quantum()

        # queue head and buttons
        q_header = tk.Frame(left, bg="#F7F7EE")
        q_header.pack(fill="x", pady=(0, 6))
        tk.Label(q_header, text="Process Queue:", font=("Segoe UI", 10, "bold"), bg="#F7F7EE", fg="#455230").pack(side="left")
        tk.Button(q_header, text="+ Add", bg="#9BA685", fg="#2C351E", relief="flat", padx=6, command=lambda: self.add_process_row("0", "3")).pack(side="right", padx=(4, 0))
        tk.Button(q_header, text="- Remove", bg="#EBEBD8", fg="#455230", relief="flat", padx=6, command=self.remove_process_row).pack(side="right")

        # inputs
        self.grid_frame = tk.Frame(left, bg="#F7F7EE")
        self.grid_frame.pack(fill="both", expand=True)
        for col, text in enumerate(["PID", "Arrival (AT)", "Burst (BT)"]):
            tk.Label(self.grid_frame, text=text, width=9, font=("Segoe UI", 8, "bold"), bg="#F7F7EE", fg="#637545").grid(row=0, column=col, pady=(0, 4))

        # run + reset
        tk.Button(left, text="Run", font=("Segoe UI", 10, "bold"), bg="#637545", fg="#EBEBD8", relief="flat", pady=7, command=self.run_simulation).pack(fill="x", pady=(10, 6))
        tk.Button(left, text="Reset", font=("Segoe UI", 9), bg="#EBEBD8", fg="#455230", relief="flat", pady=5, command=self.clear_results).pack(fill="x")

        # table and average
        right = tk.Frame(main_frame, bg="#EBEBD8")
        right.pack(side="right", fill="both", expand=True)

        # gantt chart square
        gantt_box = tk.Frame(right, bg="#F7F7EE", highlightbackground="#9BA685", highlightthickness=1, padx=12, pady=10)
        gantt_box.pack(fill="x", pady=(0, 12))
        self.gantt_title = tk.Label(gantt_box, text="Gantt Chart Visual", font=("Segoe UI", 10, "bold"), bg="#F7F7EE", fg="#455230")
        self.gantt_title.pack(anchor="w", pady=(0, 6))
        self.gantt_canvas = tk.Canvas(gantt_box, height=75, bg="#F7F7EE", highlightthickness=0)
        self.gantt_canvas.pack(fill="x")

        # result + average
        res_box = tk.Frame(right, bg="#F7F7EE", highlightbackground="#9BA685", highlightthickness=1, padx=12, pady=10)
        res_box.pack(fill="both", expand=True)
        tk.Label(res_box, text="Result", font=("Segoe UI", 10, "bold"), bg="#F7F7EE", fg="#455230").pack(anchor="w", pady=(0, 6))

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Sage.Treeview", background="#F7F7EE", fieldbackground="#F7F7EE", foreground="#2C351E", rowheight=25)
        style.configure("Sage.Treeview.Heading", background="#637545", foreground="#EBEBD8", font=("Segoe UI", 9, "bold"))

        cols = ("pid", "at", "bt", "ct", "tat", "wt", "rt")
        self.tree = ttk.Treeview(res_box, columns=cols, show="headings", style="Sage.Treeview", height=8)
        for col in cols:
            self.tree.heading(col, text=col.upper())
            self.tree.column(col, width=65, anchor="center")
        self.tree.pack(fill="both", expand=True)

        self.avg_label = tk.Label(
            res_box, text="Avg TAT: --   |   Avg WT: --   |   Avg RT: --",
            font=("Segoe UI", 10, "bold"), bg="#F7F7EE", fg="#455230"
        )
        self.avg_label.pack(anchor="w", pady=(10, 0))

    def _toggle_quantum(self, event=None):
        if self.algo_var.get() in ("Round Robin", "Compare All"):
            self.quantum_entry.config(state="normal")
        else:
            self.quantum_entry.config(state="disabled", disabledbackground="#DEDEC8")

    def add_process_row(self, at="0", bt="5"):
        if len(self.process_rows) >= 8:
            return
        row_num = len(self.process_rows) + 1
        pid = f"P{row_num}"

        lbl = tk.Label(self.grid_frame, text=pid, font=("Segoe UI", 9, "bold"), bg="#F7F7EE", fg="#455230")
        lbl.grid(row=row_num, column=0, pady=2)

        at_ent = tk.Entry(self.grid_frame, width=8, justify="center", bg="#EBEBD8", fg="#2C351E", relief="solid", bd=1)
        at_ent.insert(0, at)
        at_ent.grid(row=row_num, column=1, pady=2, padx=4)

        bt_ent = tk.Entry(self.grid_frame, width=8, justify="center", bg="#EBEBD8", fg="#2C351E", relief="solid", bd=1)
        bt_ent.insert(0, bt)
        bt_ent.grid(row=row_num, column=2, pady=2, padx=4)

        self.process_rows.append({"pid": pid, "widgets": (lbl, at_ent, bt_ent), "at": at_ent, "bt": bt_ent})

    def remove_process_row(self):
        if len(self.process_rows) <= 1:
            return
        for w in self.process_rows.pop()["widgets"]:
            w.destroy()

    def clear_results(self):
        self.gantt_canvas.delete("all")
        self.tree.delete(*self.tree.get_children())
        self.avg_label.config(text="Avg TAT: --   |   Avg WT: --   |   Avg RT: --")
        self.gantt_title.config(text="Gantt Chart Visual")
        self.status_badge.config(text="READY", bg="#637545", fg="#EBEBD8")

    def run_simulation(self):
        processes = []
        for r in self.process_rows:
            try:
                at, bt = int(r["at"].get()), int(r["bt"].get())
                if at < 0 or bt < 1:
                    raise ValueError
                processes.append({"pid": r["pid"], "at": at, "bt": bt})
            except ValueError:
                messagebox.showerror("Invalid Input", f"Check {r['pid']}: AT must be >= 0 and BT >= 1.")
                return

        try:
            quantum = int(self.quantum_entry.get())
            if quantum < 1:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Input", "Time Quantum must be >= 1.")
            return

        algo = self.algo_var.get()
        if algo == "Compare All":
            self._show_comparison(processes, quantum)
            return

        runners = {
            "FCFS": lambda: run_fcfs(processes),
            "SJF": lambda: run_sjf(processes),
            "SRTF": lambda: run_srtf(processes),
            "Round Robin": lambda: run_round_robin(processes, quantum),
        }
        self.display_result(runners[algo]())

    def display_result(self, result):
        self.gantt_title.config(text=f"Gantt Chart Visual — {result['name']}")
        self.status_badge.config(text="COMPLETED", bg="#9BA685", fg="#2C351E")

        # show gantt chart
        self.gantt_canvas.delete("all")
        self.root.update_idletasks()
        width = max(self.gantt_canvas.winfo_width(), 450) - 24
        gantt = result["gantt"]
        total_span = max(gantt[-1]["end"] - gantt[0]["start"], 1)

        colors = {"IDLE": "#D6D8C7"}
        for b in gantt:
            if b["pid"] not in colors:
                colors[b["pid"]] = GANTT_COLORS[(len(colors) - 1) % len(GANTT_COLORS)]

        x = 12
        self.gantt_canvas.create_text(x, 62, text=str(gantt[0]["start"]), fill="#455230", font=("Segoe UI", 9, "bold"))
        for b in gantt:
            w = max(((b["end"] - b["start"]) / total_span) * width, 28)
            txt_fg = "#455230" if b["pid"] in ("IDLE", "P2", "P3", "P5") else "#EBEBD8"
            self.gantt_canvas.create_rectangle(x, 8, x + w, 48, fill=colors[b["pid"]], outline="#455230")
            self.gantt_canvas.create_text(x + w / 2, 28, text=b["pid"], fill=txt_fg, font=("Segoe UI", 9, "bold"))
            x += w
            self.gantt_canvas.create_text(x, 62, text=str(b["end"]), fill="#455230", font=("Segoe UI", 9, "bold"))

        # table and averages
        self.tree.delete(*self.tree.get_children())
        procs = sorted(result["processes"], key=lambda p: p["pid"])
        for p in procs:
            self.tree.insert("", "end", values=(p["pid"], p["at"], p["bt"], p["ct"], p["tat"], p["wt"], p["rt"]))

        n = len(procs)
        avg_tat = sum(p["tat"] for p in procs) / n
        avg_wt = sum(p["wt"] for p in procs) / n
        avg_rt = sum(p["rt"] for p in procs) / n
        self.avg_label.config(text=f"Avg TAT: {avg_tat:.2f}   |   Avg WT: {avg_wt:.2f}   |   Avg RT: {avg_rt:.2f}")

    def _show_comparison(self, processes, quantum):
        results = [run_fcfs(processes), run_sjf(processes), run_srtf(processes), run_round_robin(processes, quantum)]
        self.display_result(results[0])

        lines = [f"{r['name']}\n  Avg TAT: {sum(p['tat'] for p in r['processes'])/len(processes):.2f} | "
                 f"Avg WT: {sum(p['wt'] for p in r['processes'])/len(processes):.2f} | "
                 f"Avg RT: {sum(p['rt'] for p in r['processes'])/len(processes):.2f}" for r in results]
        messagebox.showinfo("Algorithm Comparison", "\n\n".join(lines))