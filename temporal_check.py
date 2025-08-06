def is_temporal_overlap(t1_start, t1_end, t2_start, t2_end):
    """
    Check if two time intervals overlap.
    Args:
        t1_start (float): Start of interval 1
        t1_end (float): End of interval 1
        t2_start (float): Start of interval 2
        t2_end (float): End of interval 2
    Returns:
        bool: True if time intervals overlap, False otherwise.
    """
    return not (t1_end < t2_start or t2_end < t1_start)