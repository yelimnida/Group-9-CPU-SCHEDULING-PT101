# Testing Evidence — Group 9 CPU Scheduling Simulator

Every test case below was executed via `python main.py` using the console interface. A test passes when the Gantt chart timeline, process metrics table, summary averages, and validation prompts match the expected output.

| ID | Test | Result |
| :--- | :--- | :---: |
| TC1 | First-Come, First-Served (FCFS) on staggered arrivals | PASS |
| TC2 | Non-Preemptive Shortest Job First (SJF) scheduling | PASS |
| TC3 | Preemptive Shortest Remaining Time First (SRTF) with CPU idle time | PASS |
| TC4 | Round Robin (RR) time-slicing and ready-queue re-entry (`Q = 2`) | PASS |
| TC5 | Compare All Algorithms summary table (`Option 5`) | PASS |
| TC6 | Re-entering a new process workload (`Option 6`) | PASS |
| TC7 | Input validation catches negative, zero, and non-numeric entries | PASS |
| TC8 | Invalid menu choice is rejected without crashing | PASS |

---

## TC1 - First-Come, First-Served (FCFS) on staggered arrivals

**Scenario:** Enter 3 processes (`P1`: AT=0, BT=6; `P2`: AT=2, BT=4; `P3`: AT=4, BT=2), select Option `1` (FCFS), then exit with `0`.

**Input typed:**

```text
3
0
6
2
4
4
2
1
0
```

**Expected:** Processes execute strictly in arrival order (`P1` → `P2` → `P3`).
Lines that must appear:
- `Algorithm: FCFS (First-Come, First-Served)`
- `| P1 (0-6) | P2 (6-10) | P3 (10-12) |`
- `Average Turnaround Time (TAT): 7.33`
- `Average Waiting Time (WT):     3.33`
- `Average Response Time (RT):    3.33`

**Actual output:**

```text
==========================================
   GROUP 9: CPU SCHEDULING SIMULATOR
==========================================

--- Enter Process Details ---
Number of processes (1-10): 3

Process P1:
  Arrival Time (AT >= 0): 0
  Burst Time   (BT >= 1): 6

Process P2:
  Arrival Time (AT >= 0): 2
  Burst Time   (BT >= 1): 4

Process P3:
  Arrival Time (AT >= 0): 4
  Burst Time   (BT >= 1): 2

Select Scheduling Algorithm:
  [1] FCFS (First-Come, First-Served)
  [2] SJF  (Non-Preemptive Shortest Job First)
  [3] SRTF (Preemptive Shortest Remaining Time First)
  [4] Round Robin
  [5] Compare All Algorithms
  [6] Re-enter Processes
  [0] Exit
Enter choice: 1

==============================================================
Algorithm: FCFS (First-Come, First-Served)
==============================================================

Gantt Chart:
| P1 (0-6) | P2 (6-10) | P3 (10-12) |
0          6           10           12

Process Metrics:
PID     AT      BT      CT      TAT     WT      RT      
--------------------------------------------------------
P1      0       6       6       6       0       0       
P2      2       4       10      8       4       4       
P3      4       2       12      8       6       6       
--------------------------------------------------------
Average Turnaround Time (TAT): 7.33
Average Waiting Time (WT):     3.33
Average Response Time (RT):    3.33

Select Scheduling Algorithm:
  [1] FCFS (First-Come, First-Served)
  [2] SJF  (Non-Preemptive Shortest Job First)
  [3] SRTF (Preemptive Shortest Remaining Time First)
  [4] Round Robin
  [5] Compare All Algorithms
  [6] Re-enter Processes
  [0] Exit
Enter choice: 0
Exiting simulator.
```

**Result: PASS**

---

## TC2 - Non-Preemptive Shortest Job First (SJF) scheduling

**Scenario:** Using the same workload (`P1`: AT=0, BT=6; `P2`: AT=2, BT=4; `P3`: AT=4, BT=2), select Option `2` (SJF), then exit with `0`.

**Input typed:**

```text
3
0
6
2
4
4
2
2
0
```

**Expected:** After `P1` completes at $t = 6$, `P3` (BT=2) is chosen ahead of `P2` (BT=4).
Lines that must appear:
- `Algorithm: SJF (Non-Preemptive Shortest Job First)`
- `| P1 (0-6) | P3 (6-8) | P2 (8-12) |`
- `Average Turnaround Time (TAT): 6.67`
- `Average Waiting Time (WT):     2.67`
- `Average Response Time (RT):    2.67`

**Actual output:**

```text
==============================================================
Algorithm: SJF (Non-Preemptive Shortest Job First)
==============================================================

Gantt Chart:
| P1 (0-6) | P3 (6-8) | P2 (8-12) |
0          6          8           12

Process Metrics:
PID     AT      BT      CT      TAT     WT      RT      
--------------------------------------------------------
P1      0       6       6       6       0       0       
P2      2       4       12      10      6       6       
P3      4       2       8       4       2       2       
--------------------------------------------------------
Average Turnaround Time (TAT): 6.67
Average Waiting Time (WT):     2.67
Average Response Time (RT):    2.67

Select Scheduling Algorithm:
  [1] FCFS (First-Come, First-Served)
  [2] SJF  (Non-Preemptive Shortest Job First)
  [3] SRTF (Preemptive Shortest Remaining Time First)
  [4] Round Robin
  [5] Compare All Algorithms
  [6] Re-enter Processes
  [0] Exit
Enter choice: 0
Exiting simulator.
```

**Result: PASS**

---

## TC3 - Preemptive Shortest Remaining Time First (SRTF) with CPU idle time

**Scenario:** Enter 3 processes where none arrive at $t = 0$ (`P1`: AT=2, BT=6; `P2`: AT=3, BT=2; `P3`: AT=5, BT=1), select Option `3` (SRTF), then exit with `0`.

**Input typed:**

```text
3
2
6
3
2
5
1
3
0
```

**Expected:** CPU stays `IDLE` from $t = 0$ to $t = 2$, `P1` starts at $t = 2$ and is preempted at $t = 3$ by `P2` (BT=2), followed by `P3` (BT=1) at $t = 5$, and `P1` resumes at $t = 6$.
Lines that must appear:
- `Algorithm: SRTF (Preemptive Shortest Remaining Time First)`
- `| IDLE (0-2) | P1 (2-3) | P2 (3-5) | P3 (5-6) | P1 (6-11) |`
- `Average Turnaround Time (TAT): 4.00`
- `Average Waiting Time (WT):     1.00`
- `Average Response Time (RT):    0.00`

**Actual output:**

```text
==============================================================
Algorithm: SRTF (Preemptive Shortest Remaining Time First)
==============================================================

Gantt Chart:
| IDLE (0-2) | P1 (2-3) | P2 (3-5) | P3 (5-6) | P1 (6-11) |
0            2          3          5          6           11

Process Metrics:
PID     AT      BT      CT      TAT     WT      RT      
--------------------------------------------------------
P1      2       6       11      9       3       0       
P2      3       2       5       2       0       0       
P3      5       1       6       1       0       0       
--------------------------------------------------------
Average Turnaround Time (TAT): 4.00
Average Waiting Time (WT):     1.00
Average Response Time (RT):    0.00

Select Scheduling Algorithm:
  [1] FCFS (First-Come, First-Served)
  [2] SJF  (Non-Preemptive Shortest Job First)
  [3] SRTF (Preemptive Shortest Remaining Time First)
  [4] Round Robin
  [5] Compare All Algorithms
  [6] Re-enter Processes
  [0] Exit
Enter choice: 0
Exiting simulator.
```

**Result: PASS**

---

## TC4 - Round Robin (RR) time-slicing and ready-queue re-entry (`Q = 2`)

**Scenario:** Enter 3 processes (`P1`: AT=0, BT=5; `P2`: AT=1, BT=3; `P3`: AT=2, BT=1), select Option `4` (Round Robin) with Time Quantum = `2`, then exit with `0`.

**Input typed:**

```text
3
0
5
1
3
2
1
4
2
0
```

**Expected:** Newly arrived `P3` (at $t = 2$) enters the ready queue before `P1` is re-queued after its first quantum expires at $t = 2$, and the step trace prints all 6 time slices.
Lines that must appear:
- `Algorithm: Round Robin (Quantum = 2)`
- `| P1 (0-2) | P2 (2-4) | P3 (4-5) | P1 (5-7) | P2 (7-8) | P1 (8-9) |`
- `Round Robin Step Trace:`
- `Average Turnaround Time (TAT): 6.33`
- `Average Waiting Time (WT):     3.33`
- `Average Response Time (RT):    1.00`

**Actual output:**

```text
Enter choice: 4
Enter Time Quantum (>= 1): 2

==============================================================
Algorithm: Round Robin (Quantum = 2)
==============================================================

Gantt Chart:
| P1 (0-2) | P2 (2-4) | P3 (4-5) | P1 (5-7) | P2 (7-8) | P1 (8-9) |
0          2          4          5          7          8          9

Round Robin Step Trace:
Step  PID     Time Slice    Executed  Remaining BT  
----------------------------------------------------
1     P1      0 -> 2        2         3             
2     P2      2 -> 4        2         1             
3     P3      4 -> 5        1         0             
4     P1      5 -> 7        2         1             
5     P2      7 -> 8        1         0             
6     P1      8 -> 9        1         0             

Process Metrics:
PID     AT      BT      CT      TAT     WT      RT      
--------------------------------------------------------
P1      0       5       9       9       4       0       
P2      1       3       8       7       4       1       
P3      2       1       5       3       2       2       
--------------------------------------------------------
Average Turnaround Time (TAT): 6.33
Average Waiting Time (WT):     3.33
Average Response Time (RT):    1.00

Select Scheduling Algorithm:
  [1] FCFS (First-Come, First-Served)
  [2] SJF  (Non-Preemptive Shortest Job First)
  [3] SRTF (Preemptive Shortest Remaining Time First)
  [4] Round Robin
  [5] Compare All Algorithms
  [6] Re-enter Processes
  [0] Exit
Enter choice: 0
Exiting simulator.
```

**Result: PASS**

---

## TC5 - Compare All Algorithms summary table (`Option 5`)

**Scenario:** Using workload `P1` (AT=0, BT=6), `P2` (AT=2, BT=4), `P3` (AT=4, BT=2), select Option `5` (Compare All Algorithms) with Time Quantum = `2`, then exit with `0`.

**Input typed:**

```text
3
0
6
2
4
4
2
5
2
0
```

**Expected:** Side-by-side comparison table displays `Avg TAT`, `Avg WT`, and `Avg RT` for all four algorithms.
Lines that must appear:
- `ALGORITHM COMPARISON SUMMARY`
- `FCFS (First-Come, First-Served)            7.33      3.33      3.33`
- `SJF (Non-Preemptive Shortest Job First)   6.67      2.67      2.67`
- `SRTF (Preemptive Shortest Remaining Time First)6.67      2.67      2.67`
- `Round Robin (Quantum = 2)                 8.00      4.00      1.33`

**Actual output:**

```text
Enter choice: 5
Enter Time Quantum for Round Robin (>= 1): 2

====================================================================
ALGORITHM COMPARISON SUMMARY
====================================================================
Algorithm                                 Avg TAT   Avg WT    Avg RT    
--------------------------------------------------------------------
FCFS (First-Come, First-Served)            7.33      3.33      3.33      
SJF (Non-Preemptive Shortest Job First)   6.67      2.67      2.67      
SRTF (Preemptive Shortest Remaining Time First)6.67      2.67      2.67      
Round Robin (Quantum = 2)                 8.00      4.00      1.33      
====================================================================

Select Scheduling Algorithm:
  [1] FCFS (First-Come, First-Served)
  [2] SJF  (Non-Preemptive Shortest Job First)
  [3] SRTF (Preemptive Shortest Remaining Time First)
  [4] Round Robin
  [5] Compare All Algorithms
  [6] Re-enter Processes
  [0] Exit
Enter choice: 0
Exiting simulator.
```

**Result: PASS**

---

## TC6 - Re-entering a new process workload (`Option 6`)

**Scenario:** Enter an initial 1-process workload (`P1`: AT=0, BT=5), choose Option `6` to replace it with 2 processes (`P1`: AT=0, BT=3; `P2`: AT=1, BT=2), run FCFS (`1`), then exit with `0`.

**Input typed:**

```text
1
0
5
6
2
0
3
1
2
1
0
```

**Expected:** Old process list is replaced cleanly and FCFS computes metrics for the new 2-process workload.
Lines that must appear:
- `--- Enter Process Details ---`
- `| P1 (0-3) | P2 (3-5) |`
- `Average Turnaround Time (TAT): 3.50`
- `Average Waiting Time (WT):     1.00`

**Actual output:**

```text
Enter choice: 6

--- Enter Process Details ---
Number of processes (1-10): 2

Process P1:
  Arrival Time (AT >= 0): 0
  Burst Time   (BT >= 1): 3

Process P2:
  Arrival Time (AT >= 0): 1
  Burst Time   (BT >= 1): 2

Select Scheduling Algorithm:
  [1] FCFS (First-Come, First-Served)
  [2] SJF  (Non-Preemptive Shortest Job First)
  [3] SRTF (Preemptive Shortest Remaining Time First)
  [4] Round Robin
  [5] Compare All Algorithms
  [6] Re-enter Processes
  [0] Exit
Enter choice: 1

==============================================================
Algorithm: FCFS (First-Come, First-Served)
==============================================================

Gantt Chart:
| P1 (0-3) | P2 (3-5) |
0          3          5

Process Metrics:
PID     AT      BT      CT      TAT     WT      RT      
--------------------------------------------------------
P1      0       3       3       3       0       0       
P2      1       2       5       4       2       2       
--------------------------------------------------------
Average Turnaround Time (TAT): 3.50
Average Waiting Time (WT):     1.00
Average Response Time (RT):    1.00

Select Scheduling Algorithm:
  [1] FCFS (First-Come, First-Served)
  [2] SJF  (Non-Preemptive Shortest Job First)
  [3] SRTF (Preemptive Shortest Remaining Time First)
  [4] Round Robin
  [5] Compare All Algorithms
  [6] Re-enter Processes
  [0] Exit
Enter choice: 0
Exiting simulator.
```

**Result: PASS**

---

## TC7 - Input validation catches negative, zero, and non-numeric entries

**Scenario:** Attempt to enter non-numeric text (`abc`), negative Arrival Time (`-1`), zero Burst Time (`0`), and zero Time Quantum (`0`).

**Input typed:**

```text
abc
1
-1
0
0
4
4
0
2
0
```

**Expected:** Every invalid entry displays a clear error prompt and re-asks without crashing.
Lines that must appear:
- `[!] Invalid input. Enter a whole number.`
- `[!] Value must be >= 0. Try again.`
- `[!] Value must be >= 1. Try again.`

**Actual output:**

```text
==========================================
   GROUP 9: CPU SCHEDULING SIMULATOR
==========================================

--- Enter Process Details ---
Number of processes (1-10): abc
  [!] Invalid input. Enter a whole number.
Number of processes (1-10): 1

Process P1:
  Arrival Time (AT >= 0): -1
  [!] Value must be >= 0. Try again.
  Arrival Time (AT >= 0): 0
  Burst Time   (BT >= 1): 0
  [!] Value must be >= 1. Try again.
  Burst Time   (BT >= 1): 4

Select Scheduling Algorithm:
  [1] FCFS (First-Come, First-Served)
  [2] SJF  (Non-Preemptive Shortest Job First)
  [3] SRTF (Preemptive Shortest Remaining Time First)
  [4] Round Robin
  [5] Compare All Algorithms
  [6] Re-enter Processes
  [0] Exit
Enter choice: 4
Enter Time Quantum (>= 1): 0
  [!] Value must be >= 1. Try again.
Enter Time Quantum (>= 1): 2

==============================================================
Algorithm: Round Robin (Quantum = 2)
==============================================================

Gantt Chart:
| P1 (0-4) |
0          4

Round Robin Step Trace:
Step  PID     Time Slice    Executed  Remaining BT  
----------------------------------------------------
1     P1      0 -> 2        2         2             
2     P1      2 -> 4        2         0             

Process Metrics:
PID     AT      BT      CT      TAT     WT      RT      
--------------------------------------------------------
P1      0       4       4       4       0       0       
--------------------------------------------------------
Average Turnaround Time (TAT): 4.00
Average Waiting Time (WT):     0.00
Average Response Time (RT):    0.00

Select Scheduling Algorithm:
  [1] FCFS (First-Come, First-Served)
  [2] SJF  (Non-Preemptive Shortest Job First)
  [3] SRTF (Preemptive Shortest Remaining Time First)
  [4] Round Robin
  [5] Compare All Algorithms
  [6] Re-enter Processes
  [0] Exit
Enter choice: 0
Exiting simulator.
```

**Result: PASS**

---

## TC8 - Invalid menu choice is rejected without crashing

**Scenario:** Enter an out-of-range menu option (`9`) and text (`xyz`) at the main menu before exiting with `0`.

**Input typed:**

```text
1
0
3
9
xyz
0
```

**Expected:** Invalid menu choices trigger a warning message and re-display the menu prompt safely.
Lines that must appear:
- `[!] Invalid choice. Pick 0-6.`
- `Exiting simulator.`

**Actual output:**

```text
Enter choice: 9
  [!] Invalid choice. Pick 0-6.

Select Scheduling Algorithm:
  [1] FCFS (First-Come, First-Served)
  [2] SJF  (Non-Preemptive Shortest Job First)
  [3] SRTF (Preemptive Shortest Remaining Time First)
  [4] Round Robin
  [5] Compare All Algorithms
  [6] Re-enter Processes
  [0] Exit
Enter choice: xyz
  [!] Invalid choice. Pick 0-6.

Select Scheduling Algorithm:
  [1] FCFS (First-Come, First-Served)
  [2] SJF  (Non-Preemptive Shortest Job First)
  [3] SRTF (Preemptive Shortest Remaining Time First)
  [4] Round Robin
  [5] Compare All Algorithms
  [6] Re-enter Processes
  [0] Exit
Enter choice: 0
Exiting simulator.
```

**Result: PASS**