import copy


def run_srtf(processes):
    procs = copy.deepcopy(processes)
    n = len(procs)
    completed = 0
    current_time = 0
    gantt = []

    for p in procs:
        p["rem"] = p["bt"]      # reamining bt
        p["start"] = None       # if first time, proess gets the cpu

    while completed < n:
        # look for all arrived processes that still have remaining burst time
        ready = []
        for p in procs:
            if p["rem"] > 0 and p["at"] <= current_time:
                ready.append(p)

        if len(ready) == 0:
            next_arrival = min(p["at"] for p in procs if p["rem"] > 0)
            gantt.append({"pid": "IDLE", "start": current_time, "end": next_arrival})
            current_time = next_arrival
            continue

        # pick process with shortest remaining time if tie then AT
        chosen = ready[0]
        for p in ready:
            if (p["rem"], p["at"], p["pid"]) < (chosen["rem"], chosen["at"], chosen["pid"]):
                chosen = p

        if chosen["start"] is None:
            chosen["start"] = current_time

        # run for 1 time unit; merge with previous Gantt block if same process
        if len(gantt) > 0 and gantt[-1]["pid"] == chosen["pid"] and gantt[-1]["end"] == current_time:
            gantt[-1]["end"] += 1
        else:
            gantt.append({"pid": chosen["pid"], "start": current_time, "end": current_time + 1})

        chosen["rem"] -= 1
        current_time += 1

        if chosen["rem"] == 0:
            chosen["ct"] = current_time
            chosen["tat"] = chosen["ct"] - chosen["at"]
            chosen["wt"] = chosen["tat"] - chosen["bt"]
            chosen["rt"] = chosen["start"] - chosen["at"]
            completed += 1

    return {"name": "SRTF (Preemptive Shortest Remaining Time First)", "processes": procs, "gantt": gantt}