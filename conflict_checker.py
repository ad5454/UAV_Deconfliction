from spatial_check import is_spatial_conflict
from temporal_check import is_temporal_overlap

def check_conflicts(primary_mission, simulated_flights):
    conflicts = []
    for sim_flight in simulated_flights:
        for wp_primary in primary_mission['waypoints']:
            for wp_sim in sim_flight['waypoints']:
                if is_spatial_conflict(wp_primary['pos'], wp_sim['pos']) and is_temporal_overlap(
                    wp_primary['t'][0], wp_primary['t'][1], wp_sim['t'][0], wp_sim['t'][1]
                ):
                    conflicts.append({
                        'drone_id': sim_flight['id'],
                        'location': wp_primary['pos'],
                        'time': wp_primary['t']
                    })
    return {
        'status': 'conflict' if conflicts else 'clear',
        'conflicts': conflicts
    }

def query_deconfliction(primary_path, simulated_paths):
    return check_conflicts(primary_path, simulated_paths)