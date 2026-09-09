import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Read car counts from file
def get_car_counts():
    try:
        with open("car_counts.txt", "r") as f:
            counts = list(map(int, f.read().strip().split(',')))
    except FileNotFoundError:
        counts = [0, 0, 0]  # Default counts if file not found
    return counts

# Read signal times assigned by traffic_signal.py
def get_signal_times():
    try:
        with open("signal_times.txt", "r") as f:
            times = list(map(int, f.read().strip().split(',')))
    except FileNotFoundError:
        times = [0, 0, 0]  # Default signal times if file not found
    return times

# Plot update function for the dashboard
def update_dashboard(frame):
    # Get updated car counts and signal times
    car_counts = get_car_counts()
    signal_times = get_signal_times()

    # Update the bar chart with new car counts
    ax1.clear()
    ax1.bar(['Road 1', 'Road 2', 'Road 3'], car_counts, color=['blue', 'green', 'red'])
    ax1.set_title("Car Counts per Road")
    ax1.set_ylim(0, max(car_counts + [5]) + 5)

    # Update the signal timing display
    ax2.clear()
    ax2.text(0.5, 0.8, f"Road 1: {signal_times[0]} sec", ha='center', va='center', fontsize=12)
    ax2.text(0.5, 0.6, f"Road 2: {signal_times[1]} sec", ha='center', va='center', fontsize=12)
    ax2.text(0.5, 0.4, f"Road 3: {signal_times[2]} sec", ha='center', va='center', fontsize=12)
    ax2.set_title("Signal Light Times (Green)")
    ax2.axis('off')  # Hide axis for cleaner look

    plt.tight_layout()

# Create figure and axes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Setup animation
ani = FuncAnimation(fig, update_dashboard, interval=2000)  # Update every 2 seconds

# Show the dashboard
plt.show(block=True)
