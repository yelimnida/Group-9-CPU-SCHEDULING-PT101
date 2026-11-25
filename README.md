# Group 9 — CPU Scheduling Simulator (PT 101)

A console-based CPU Scheduling Simulator built with Python featuring a modular architecture that separates core scheduling algorithms from the command-line user interface.

## Group 9 Members

* **Calingasan, Yael John**
* **Mercado, Jove**
* **Panganiban, Jhanel**
* **Panganiban, Kerk Daniel**

## Documentation & Deliverables

* [**User Guide (`USER_GUIDE.md`)**](USER_GUIDE.md) — Setup requirements, interactive menu controls, input rules, and output interpretation.
* [**Testing Evidence (`TESTING.md`)**](TESTING.md) — Verified test cases (`TC1`–`TC8`) comparing expected vs. actual console outputs and input validation checks.

## Repository Structure

```text
Group-9-CPU-SCHEDULING-PT101/
├── algorithms/
│   ├── __init__.py
│   ├── fcfs.py              # First-Come, First-Served (Non-Preemptive)
│   ├── sjf.py               # Shortest Job First (Non-Preemptive)
│   ├── srtf.py              # Shortest Remaining Time First (Preemptive)
│   └── round_robin.py       # Round Robin (Preemptive with Time Quantum)
├── main.py                  # Console application entry point and menu interface
├── README.md                # Project overview and documentation links
├── USER_GUIDE.md            # Console execution and usage manual
├── TESTING.md               # Test cases and verification outputs
└── .gitignore               # Ignores __pycache__/ and local temporary files
```

## Quick Start

### Prerequisites

* **Python 3.10+** installed on Windows, macOS, or Linux.
* Uses only the Python standard library—no external packages are required.

### How to Run

1. Clone or download this repository and open a terminal inside `Group-9-CPU-SCHEDULING-PT101`.
2. Run the simulator:
   ```bash
   python main.py
   ```
3. Enter the number of processes (`1`–`10`) along with each process's **Arrival Time (`AT >= 0`)** and **Burst Time (`BT >= 1`)**, then select an option from the menu:
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