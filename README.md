# UAV_Deconfliction
🚀 Project Overview
This system detects and visualizes potential airspace conflicts between a primary UAV mission and multiple simulated drone trajectories using a hybrid lane-based + 4D deconfliction strategy (3D space + time).
It is built to be modular, testable, and integrates realistic data formats — ideal for pre-flight safety validation.
________________________________________
📦 Dependencies & Versions
✅ Python Version:
•	Python 3.7
Justification: Python 3.7 offers the widest compatibility with legacy packages and is ideal for stable, resource-constrained robotics environments (especially when working with embedded systems or ROS).
________________________________________
✅ Required Packages:
Package	Version	Justification
matplotlib	3.5.3	Ensures stable support for 3D plotting & animation without newer API breakages
numpy	1.21.6	Optimal for Python 3.7, used for vector math & interpolation
________________________________________
🛠️ Setup Instructions
1. Create Virtual Environment (Optional but Recommended):
python3.7 -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
________________________________________
2. Install Dependencies:
pip install matplotlib==3.5.3 numpy==1.21.6 
________________________________________
▶️ How to Run
Run Main System:
python main.py
This will:
•	Load the primary and simulated drone missions from JSON
•	Perform 4D conflict detection
________________________________________
Run Unit Tests:
python test_conflict_checker.py
•	Verifies conflict/no-conflict scenarios
•	Ensures 4D logic works for edge cases
________________________________________
📁 Project Structure
├── main.py                        # Entry point
├── conflict_checker.py           # 4D conflict logic
├── visualizer.py                 # 3D plotting + animation
├── data_ingestion.py             # Loads JSON data
├── test_conflict_checker.py      # Unit tests
├── primary_mission.json          # Main drone path (3D + time)
├── simulated_flights.json        # Multiple other UAVs
├── uav_deconfliction_4D_sim.mp4  # Output animation
________________________________________
📽 Output
•	Static 3D Graphs: All drone paths + conflict points (X)
•	4D Animation: Temporal simulation with all movements visualized
