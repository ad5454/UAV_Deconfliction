from data_ingestion import load_mission_data, load_simulated_flights
from conflict_checker import query_deconfliction
from visualizer import plot_3d_trajectories, animate_and_save_flights

primary_mission = load_mission_data("data/primary_mission.json")
simulated_flights = load_simulated_flights("data/simulated_flights.json")

result = query_deconfliction(primary_mission, simulated_flights)
print("Conflict Check Result:", result["status"])
for conflict in result["conflicts"]:
    print(f"Conflict with {conflict['drone_id']} at {conflict['location']} during t={conflict['time']}")


plot_3d_trajectories(primary_mission, simulated_flights, result["conflicts"])
animate_and_save_flights(primary_mission, simulated_flights, result["conflicts"], save_path="uav_deconfliction_4D_sim.mp4")
