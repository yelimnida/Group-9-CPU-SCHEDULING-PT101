from algorithms.fcfs import run_fcfs
from algorithms.sjf import run_sjf
from algorithms.srtf import run_srtf
from algorithms.round_robin import run_round_robin


def get_int(prompt, min_val):
    while True:
        try:
            val = int(input(prompt).strip())
            if val < min_val:
                print(f"  [!] Value must be >= {min_val}. Try again.")
                continue
            return val
        except ValueError:
            print("  [!] Invalid input. Enter a whole number.")


def input_processes():
    print("\n--- Enter Process Details ---")
    count = get_int("Number of processes (1-10): ", 1)
    processes = []
    for i in range(1, count + 1):
        pid = f"P{i}"
        print(f"\nProcess {pid}:")
        at = get_int("  Arrival Time (AT >= 0): ", 0)
        bt = get_int("  Burst Time   (BT >= 1): ", 1)
        processes.append({"pid": pid, "at": at, "bt": bt})
    return processes


def print_result(result):
    print("\n" + "=" * 62)
    print(f"Algorithm: {result['name']}")
    print("=" * 62)

    # Gantt
    print("\nGantt Chart:")
    bar = "|"
    timeline = str(result["gantt"][0]["start"])
    for block in result["gantt"]:
        segment = f" {block['pid']} ({block['start']}-{block['end']}) "
        bar += segment + "|"
        timeline += " " * (len(segment) + 1 - len(str(block["end"]))) + str(block["end"])
    print(bar)
    print(timeline)

    # round robin
    if "rr_trace" in result:
        print("\nRound Robin Step Trace:")
        print(f"{'Step':<6}{'PID':<8}{'Time Slice':<14}{'Executed':<10}{'Remaining BT':<14}")
        print("-" * 52)
        for s in result["rr_trace"]:
            print(f"{s['step']:<6}{s['pid']:<8}{s['start']} -> {s['end']:<9}{s['ran']:<10}{s['rem']:<14}")

    # processes
    procs = sorted(result["processes"], key=lambda p: p["pid"])
    print("\nProcess Metrics:")
    print(f"{'PID':<8}{'AT':<8}{'BT':<8}{'CT':<8}{'TAT':<8}{'WT':<8}{'RT':<8}")
    print("-" * 56)
    for p in procs:
        print(f"{p['pid']:<8}{p['at']:<8}{p['bt']:<8}{p['ct']:<8}{p['tat']:<8}{p['wt']:<8}{p['rt']:<8}")
    print("-" * 56)

    n = len(procs)
    avg_tat = sum(p["tat"] for p in procs) / n
    avg_wt = sum(p["wt"] for p in procs) / n
    avg_rt = sum(p["rt"] for p in procs) / n
    print(f"Average Turnaround Time (TAT): {avg_tat:.2f}")
    print(f"Average Waiting Time (WT):     {avg_wt:.2f}")
    print(f"Average Response Time (RT):    {avg_rt:.2f}")


def compare_all(processes, quantum):
    results = [
        run_fcfs(processes),
        run_sjf(processes),
        run_srtf(processes),
        run_round_robin(processes, quantum),
    ]
    print("\n" + "=" * 68)
    print("ALGORITHM COMPARISON SUMMARY")
    print("=" * 68)
    print(f"{'Algorithm':<42}{'Avg TAT':<10}{'Avg WT':<10}{'Avg RT':<10}")
    print("-" * 68)
    for r in results:
        n = len(r["processes"])
        tat = sum(p["tat"] for p in r["processes"]) / n
        wt = sum(p["wt"] for p in r["processes"]) / n
        rt = sum(p["rt"] for p in r["processes"]) / n
        print(f"{r['name']:<42}{tat:<10.2f}{wt:<10.2f}{rt:<10.2f}")
    print("=" * 68)


def main():
    print("==========================================")
    print("   GROUP 9: CPU SCHEDULING SIMULATOR")
    print("==========================================")

    processes = input_processes()

    while True:
        print("\nSelect Scheduling Algorithm:")
        print("  [1] FCFS (First-Come, First-Served)")
        print("  [2] SJF  (Non-Preemptive Shortest Job First)")
        print("  [3] SRTF (Preemptive Shortest Remaining Time First)")
        print("  [4] Round Robin")
        print("  [5] Compare All Algorithms")
        print("  [6] Re-enter Processes")
        print("  [0] Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            print_result(run_fcfs(processes))
        elif choice == "2":
            print_result(run_sjf(processes))
        elif choice == "3":
            print_result(run_srtf(processes))
        elif choice == "4":
            q = get_int("Enter Time Quantum (>= 1): ", 1)
            print_result(run_round_robin(processes, q))
        elif choice == "5":
            q = get_int("Enter Time Quantum for Round Robin (>= 1): ", 1)
            compare_all(processes, q)
        elif choice == "6":
            processes = input_processes()
        elif choice == "0":
            print("Exiting simulator.")
            break
        else:
            print("  [!] Invalid choice. Pick 0-6.")


if __name__ == "__main__":
    main()