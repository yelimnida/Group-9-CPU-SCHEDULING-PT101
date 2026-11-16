import copy


def run_round_robin(processes, quantum):
    procs = copy.deepcopy(processes)
    procs.sort(key=lambda p: (p["at"], p["pid"]))

    n = len(procs)
    for p in procs:
        p["rem"] = p["bt"]
        p["start"] = None

    ready_queue = []
    gantt = []
    rr_trace = []

    current_time = 0
    next_index = 0
    completed = 0
    step = 1

    #  processes arriving at time 0
    while next_index < n and procs[next_index]["at"] <= current_time:
        ready_queue.append(procs[next_index])
        next_index += 1

    while completed < n:
        if len(ready_queue) == 0:
            next_time = procs[next_index]["at"]
            gantt.append({"pid": "IDLE", "start": current_time, "end": next_time})
            current_time = next_time
            while next_index < n and procs[next_index]["at"] <= current_time:
                ready_queue.append(procs[next_index])
                next_index += 1
            continue

        current_proc = ready_queue.pop(0)

        if current_proc["start"] is None:
            current_proc["start"] = current_time

        run_time = min(quantum, current_proc["rem"])
        start_slice = current_time
        end_slice = current_time + run_time

        current_proc["rem"] -= run_time
        current_time = end_slice

        gantt.append({"pid": current_proc["pid"], "start": start_slice, "end": end_slice})
        rr_trace.append({
            "step": step,
            "pid": current_proc["pid"],
            "start": start_slice,
            "end": end_slice,
            "ran": run_time,
            "rem": current_proc["rem"]
        })
        step += 1

        # add new arrived processes and then put the current process back in line
        while next_index < n and procs[next_index]["at"] <= current_time:
            ready_queue.append(procs[next_index])
            next_index += 1

        if current_proc["rem"] > 0:
            ready_queue.append(current_proc)
        else:
            current_proc["ct"] = current_time
            current_proc["tat"] = current_proc["ct"] - current_proc["at"]
            current_proc["wt"] = current_proc["tat"] - current_proc["bt"]
            current_proc["rt"] = current_proc["start"] - current_proc["at"]
            completed += 1

    return {
        "name": f"Round Robin (Quantum = {quantum})",
        "processes": procs,
        "gantt": gantt,
        "quantum": quantum,
        "rr_trace": rr_trace
    }