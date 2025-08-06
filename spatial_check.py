import numpy as np

def is_spatial_conflict(p1, p2, threshold=5.0):
    return np.linalg.norm(np.array(p1) - np.array(p2)) < threshold
