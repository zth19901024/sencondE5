import time

def pomodoro_timer(work_minutes, break_minutes, cycles):
    for cycle in range(cycles):
        print("Cycle {}: Work for {} minutes".format(cycle + 1, work_minutes))
        time.sleep(work_minutes * 60)  # convert minutes to seconds
        print("Break for {} minutes".format(break_minutes))
        time.sleep(break_minutes * 60)  # convert minutes to seconds

if __name__ == "__main__":
    work_time = 25  # 设置工作时间（分钟）
    break_time = 5   # 设置休息时间（分钟）
    num_cycles = 4   # 设置工作/休息循环次数

    pomodoro_timer(work_time, break_time, num_cycles)
