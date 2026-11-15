import tkinter as tk
from ui import CPUSchedulerUI


def main():
    root = tk.Tk()
    app = CPUSchedulerUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()