# Group 9 — CPU Scheduling Simulator (PT 101)

A console-based CPU Scheduling Simulator built with Python featuring a modular architecture that separates scheduling logic from the command-line user interface.

## Group 9 Members

* **Calingasan, Yael John P.**
* **Mercado, Jove**
* **Panganiban, Jhanel**
* **Panganiban, Kerk Daniel**

## Documentation & Deliverables

* [**User Guide (PDF)**](documents/User Guide.pdf) — Console execution instructions, interactive menu guide, input rules, and output interpretation.
* [**Testing Evidence (PDF)**](documents/Testing Evidence.pdf) — Verified test cases comparing expected vs. actual simulation outputs and boundary checks.

## Repository Structure

```text
Group-9-CPU-SCHEDULING-PT101/
├── algorithms/
│   ├── __init__.py
│   ├── fcfs.py              # First-Come, First-Served (Non-Preemptive)
│   ├── sjf.py               # Shortest Job First (Non-Preemptive)
│   ├── srtf.py              # Shortest Remaining Time First (Preemptive)
│   └── round_robin.py       # Round Robin (Preemptive with Time Quantum)
├── documents/
│   ├── User_Guide.pdf       # Execution steps, input rules, and output guide
│   └── Testing_Evidence.pdf # Test cases with expected vs. actual results
├── main.py                  # Console application entry point and menu interface
├── README.md                # Project overview and documentation links
└── .gitignore               # Ignores __pycache__/ and local temporary files
```

## Quick Start

### Prerequisites

* **Python 3.10+** installed on Windows, macOS, or Linux.
* Uses only the Python standard library—no external third-party packages are required.

### How to Run

1. Clone or download this repository and open a terminal inside the `Group-9-CPU-SCHEDULING-PT101` directory.
2. Launch the simulator:
   ```bash
   python main.py
   ```
3. Enter the number of processes (`1`–`10`) along with each process's **Arrival Time (`AT >= 0`)** and **Burst Time (`BT >= 1`)**.
4. Use the interactive menu to run a simulation:
   * **`[1]`** FCFS (First-Come, First-Served)
   * **`[2]`** SJF (Non-Preemptive Shortest Job First)
   * **`[3]`** SRTF (Preemptive Shortest Remaining Time First)
   * **`[4]`** Round Robin (prompts for Time Quantum `>= 1`)
   * **`[5]`** Compare All Algorithms
   * **`[6]`** Re-enter Processes
   * **`[0]`** Exit

## Supported Algorithms & Metrics

* **Algorithms:** FCFS, Non-Preemptive SJF, Preemptive SRTF, and Round Robin (with quantum step trace).
* **Calculated Metrics:**
  * **Completion Time (`CT`):** Timestamp when the process finishes execution.
  * **Turnaround Time (`TAT`):** $\text{TAT} = \text{CT} - \text{AT}$
  * **Waiting Time (`WT`):** $\text{WT} = \text{TAT} - \text{BT}$
  * **Response Time (`RT`):** $\text{RT} = \text{First Start Time} - \text{AT}$
  * **Summary Averages:** Average `TAT`, Average `WT`, and Average `RT` printed alongside an ASCII Gantt chart timeline.