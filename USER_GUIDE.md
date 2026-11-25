# User Guide

## 1. Requirements and running

Python 3.10 or newer (standard library only; no external packages required). From the folder holding `main.py`:

```
python main.py
```

In VS Code or another IDE, open a terminal in the project root (`Group-9-CPU-SCHEDULING-PT101`) and run `python main.py`. Type your inputs in the console and press Enter.

## 2. The menu

```
  [1] FCFS (First-Come, First-Served)
  [2] SJF  (Non-Preemptive Shortest Job First)
  [3] SRTF (Preemptive Shortest Remaining Time First)
  [4] Round Robin
  [5] Compare All Algorithms
  [6] Re-enter Processes
  [0] Exit
```

| Choice | What it does |
|---|---|
| 1 | Run First-Come, First-Served scheduling (processes execute in arrival order). |
| 2 | Run Non-Preemptive Shortest Job First scheduling (picks the shortest Burst Time among arrived processes). |
| 3 | Run Preemptive Shortest Remaining Time First scheduling (preempts if a newly arrived process has a shorter remaining burst). |
| 4 | Run Round Robin scheduling (prompts for a Time Quantum `>= 1` and prints a step-by-step slice trace). |
| 5 | Compare all four algorithms side by side (`Avg TAT`, `Avg WT`, and `Avg RT`) using a specified Time Quantum. |
| 6 | Replace the current process list with a new set of processes (see section 3). |
| 0 | Exit the simulator. |

## 3. Entering processes (startup & choice 6)

All inputs are whole numbers entered one per prompt. The program asks, in order:

| Prompt | What to type | Example |
|---|---|---|
| Number of processes (`1-10`) | one whole number from `1` to `10` | `3` |
| Arrival Time (`AT >= 0`) | whole number `>= 0` for each process `Pi` | `0` |
| Burst Time (`BT >= 1`) | whole number `>= 1` for each process `Pi` | `6` |

(Arrival Time and Burst Time are asked in pairs for `P1`, `P2`, up to `Pn`.)

Rejected input:

- letters, decimals, or symbols: `[!] Invalid input. Enter a whole number.`, then it asks again
- Arrival Time `< 0`: `[!] Value must be >= 0. Try again.`, then it asks again
- Burst Time `< 1` or Time Quantum `< 1`: `[!] Value must be >= 1. Try again.`, then it asks again
- menu choice outside `0–6`: `[!] Invalid choice. Pick 0-6.`, then it re-displays the menu

## 4. Reading the output

**Gantt Chart**

```
Gantt Chart:
| P1 (0-6) | P2 (6-10) | P3 (10-12) |
0          6           10           12
```

Shows the exact order in which processes occupy the CPU, with start and end timestamps aligned underneath. If no process has arrived yet at a given timestamp, the timeline displays `IDLE`.

**Round Robin Step Trace (choice 4)**

```
Round Robin Step Trace:
Step  PID     Time Slice    Executed  Remaining BT  
----------------------------------------------------
1     P1      0 -> 2        2         3             
2     P2      2 -> 4        2         1             
```

Printed only when running Round Robin. Each row tracks a single quantum slice, how many units ran, and how much Burst Time remains. Newly arriving processes enter the ready queue before an unexpired process is placed back at the end of the queue.

**Process Metrics & Averages**

```
PID     AT      BT      CT      TAT     WT      RT      
--------------------------------------------------------
P1      0       6       6       6       0       0       
P2      2       4       10      8       4       4       
--------------------------------------------------------
Average Turnaround Time (TAT): 7.33
Average Waiting Time (WT):     3.33
Average Response Time (RT):    3.33
```

| Column | Meaning | Formula |
|---|---|---|
| `AT` | Arrival Time | Timestamp when the process enters the ready queue |
| `BT` | Burst Time | Total CPU execution time required |
| `CT` | Completion Time | Timestamp when the process finishes execution |
| `TAT` | Turnaround Time | $\text{CT} - \text{AT}$ |
| `WT` | Waiting Time | $\text{TAT} - \text{BT}$ |
| `RT` | Response Time | $\text{First Start Time} - \text{AT}$ |

*(Tie-breaking rule: When two ready processes have identical Burst Time in SJF or Remaining Time in SRTF, the scheduler picks the earliest **Arrival Time (`AT`)** first, followed by ascending **Process ID (`PID`)**.)*

## 5. Example session

Run `python main.py` and enter 3 processes (`P1`: AT=`0`, BT=`6`; `P2`: AT=`2`, BT=`4`; `P3`: AT=`4`, BT=`2`), then choose `2` for SJF:

```
Enter choice: 2

==============================================================
Algorithm: SJF (Non-Preemptive Shortest Job First)
==============================================================

Gantt Chart:
| P1 (0-6) | P3 (6-8) | P2 (8-12) |
0          6          8           12
...
Average Turnaround Time (TAT): 6.67
Average Waiting Time (WT):     2.67
Average Response Time (RT):    2.67
```

More examples with full console outputs are in `TESTING.md`.