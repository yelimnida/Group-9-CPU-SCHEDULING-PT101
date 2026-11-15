import copy


def run_fcfs(processes):
    procs = copy.deepcopy(processes)

    #  this sorts arrival time first then process id if it ties
    procs.sort(key=lambda p: (p["at"], p["pid"]))

    current_time = 0
    gantt = []

    for p in procs:
        # if cpu is waiting for next process, record idle time
        if current_time < p["at"]:
            gantt.append({"pid": "IDLE", "start": current_time, "end": p["at"]})
            current_time = p["at"]

        p["start"] = current_time
        end_time = current_time + p["bt"]

        gantt.append({"pid": p["pid"], "start": current_time, "end": end_time})

        p["ct"] = end_time
        p["tat"] = p["ct"] - p["at"]
        p["wt"] = p["tat"] - p["bt"]
        p["rt"] = p["start"] - p["at"]

        current_time = end_time

    return {"name": "FCFS (First-Come, First-Served)", "processes": procs, "gantt": gantt}