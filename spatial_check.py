import numpy as np

def is_spatial_conflict(p1, p2, threshold=5.0):
    return np.linalg.norm(np.array(p1) - np.array(p2)) < threshold

# ------------------ temporal_check.py ------------------
def is_temporal_overlap(t1_start, t1_end, t2_start, t2_end):
    return not (t1_end < t2_start or t2_end < t1_start)