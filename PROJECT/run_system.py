import subprocess

# Use venv python
python_path = r"venv\Scripts\python.exe"

# Start all scripts
subprocess.Popen([python_path, "car_counting1.py"])
subprocess.Popen([python_path, "car_counting2.py"])
subprocess.Popen([python_path, "car_counting3.py"])
subprocess.Popen([python_path, "traffic_signal.py"])
subprocess.Popen([python_path, "dashboard.py"])

# Keep main running
input("Press ENTER to stop...")