def compute_penalty(hours_log: str, closing_time: int) -> int:
    # TODO: Input validation
    log_vals = hours_log.upper().split(' ')
    return (sum(1 for v in log_vals[:closing_time] if v == 'N') +
            sum(1 for v in log_vals[closing_time:] if v == 'Y'))


def find_best_closing_time(hours_log: str) -> int:
    return min(((t, compute_penalty(hours_log, t))
                for t in range(0, len(hours_log.split(' ')) + 1)),
               key=lambda k: k[1])[0]


def find_best_closing_time2(hours_log: str) -> int:
    """
    Using compute_penalty() results in a sub-optimal O(n^2) algorithm
    If we write it from scratch, we can do it in O(n)
    """
    if len(hours_log) == 0:
        return 0

    min_penalty_idx = 0
    min_penalty_val = 0
    curr_penalty_idx = 0
    curr_penalty_val = 0
    for v in hours_log.split(' '):
        curr_penalty_idx += 1
        # When moving the hour idx to the right, if we encounter 'N',
        # then penalty for lhs increases, and rhs remains the same.
        # If we encounter 'Y', then penalty for lhs remains the same, and
        # penalty for rhs decreases.
        # Note curr_penalty_val is wrong, but it's off by a constant amount,
        # i.e. the sum of 'Y' in hours_log, so min_penalty_idx will still be
        # correct
        curr_penalty_val += 1 if v == 'N' else -1
        if curr_penalty_val < min_penalty_val:
            min_penalty_val = curr_penalty_val
            min_penalty_idx = curr_penalty_idx

    return min_penalty_idx
