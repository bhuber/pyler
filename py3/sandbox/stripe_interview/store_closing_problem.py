POSSIBLE_LOG_VALS = {'Y', 'N'}


def compute_penalty(hours_log: str, closing_time: int) -> int:
    log_vals = hours_log.upper().split(' ')
    log_unique_vals = {v for v in log_vals}
    if not log_unique_vals.issubset(POSSIBLE_LOG_VALS):
        raise ValueError("hours_log must contain only 'Y' and 'N'", hours_log)

    return (sum(1 for v in log_vals[:closing_time] if v == 'N') +
            sum(1 for v in log_vals[closing_time:] if v == 'Y'))


def compute_benefit(hours_log: str, closing_time: int) -> int:
    log_vals = hours_log.upper().split(' ')
    log_unique_vals = {v for v in hours_log}
    if not POSSIBLE_LOG_VALS.issubset(log_unique_vals):
        raise ValueError("hours_log must contain only 'Y' and 'N'", hours_log)

    return (sum(1 for v in log_vals[:closing_time] if v == 'Y') +
            sum(1 for v in log_vals[closing_time:] if v == 'N'))


def find_best_closing_time(hours_log: str) -> int:
    all_times = [compute_penalty(hours_log, t)
                 for t in range(0, len(hours_log.split(' ')) + 1)]
    print(all_times)
    return min(enumerate(all_times), key=lambda k: k[1])[0]

def find_best_closing_time2(hours_log: str) -> int:
    all_times = [compute_penalty(hours_log, t)
                 for t in range(0, len(hours_log.split(' ')))]
    #print(all_times)

    min_penalty_idx = 0
    min_penalty_val = 0
    curr_penalty_idx = 0
    curr_penalty_val = 0
    for v in hours_log.split(' '):
        curr_penalty_idx += 1
        curr_penalty_val += 1 if v == 'N' else -1
        print(curr_penalty_val)
        if curr_penalty_val < min_penalty_val:
            min_penalty_val = curr_penalty_val
            min_penalty_idx = curr_penalty_idx

    print('')
    return min_penalty_idx
