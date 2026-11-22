import copy


def run_sjf(processes):
    procs = copy.deepcopy(processes)
    n = len(procs)
    completed = 0
    current_time = 0
    gantt = []

    for p in procs:
        p["done"] = False

    while completed < n:
        # look for arrived processes that has not finished yet
        ready = []
        for p in procs:
            if not p["done"] and p["at"] <= current_time:
                ready.append(p)

        #if no process arrived, go to next
        if len(ready) == 0:
            next_arrival = min(p["at"] for p in procs if not p["done"])
            gantt.append({"pid": "IDLE", "start": current_time, "end": next_arrival})
            current_time = next_arrival
            continue

        # pick process through shortest BT if its a tie then AT
        chosen = ready[0]
        for p in ready:
            if (p["bt"], p["at"], p["pid"]) < (chosen["bt"], chosen["at"], chosen["pid"]):
                chosen = p

        chosen["start"] = current_time
        end_time = current_time + chosen["bt"]

        gantt.append({"pid": chosen["pid"], "start": current_time, "end": end_time})

        chosen["ct"] = end_time
        chosen["tat"] = chosen["ct"] - chosen["at"]
        chosen["wt"] = chosen["tat"] - chosen["bt"]
        chosen["rt"] = chosen["start"] - chosen["at"]
        chosen["done"] = True

        completed += 1
        current_time = end_time

    return {"name": "SJF (Non-Preemptive Shortest Job First)", "processes": procs, "gantt": gantt}