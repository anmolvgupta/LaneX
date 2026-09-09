import time
import random

class TrafficSignal:
    def __init__(self):
        self.max_green = 50   # Max green light duration (seconds)
        self.min_green = 20   # Min green light duration (seconds)
        self.yellow = 5       # Yellow light duration (seconds)
        self.max_red = 135    # Total cycle duration (seconds)
        self.num_roads = 3    # Number of roads

    def calculate_green_time(self, densities):
        """Assigns green light time based on vehicle densities, ensuring total green time doesn't exceed 120 seconds."""
        total_green_time = 120
        sorted_densities = sorted(enumerate(densities), key=lambda x: x[1], reverse=True)
        max_density_road, _ = sorted_densities[0]
        green_times = [0] * self.num_roads

        # Assign maximum green time to the highest density road
        green_times[max_density_road] = self.max_green

        remaining_time = total_green_time - green_times[max_density_road]
        total_remaining_density = sorted_densities[1][1] + sorted_densities[2][1]

        if total_remaining_density > 0:
            # Proportional distribution based on remaining densities
            green_times[sorted_densities[1][0]] = max(
                (sorted_densities[1][1] * remaining_time) // total_remaining_density, self.min_green)
            green_times[sorted_densities[2][0]] = max(
                (sorted_densities[2][1] * remaining_time) // total_remaining_density, self.min_green)
        else:
            # If densities are equal, split remaining time equally
            green_times[sorted_densities[1][0]] = green_times[sorted_densities[2][0]] = remaining_time // 2

        # If the total green time exceeds 120 seconds, normalize the green times
        total_assigned_green_time = sum(green_times)
        if total_assigned_green_time > total_green_time:
            excess_time = total_assigned_green_time - total_green_time
            # Distribute the excess time proportionally
            for i in range(self.num_roads):
                green_times[i] -= (green_times[i] / total_assigned_green_time) * excess_time

        return green_times

    def get_signal_times(self, densities):
        return self.calculate_green_time(densities)

# Initialize Traffic Signal System
traffic_system = TrafficSignal()

while True:
    # Read car counts from the file
    try:
        with open("car_counts.txt", "r") as f:
            counts = list(map(int, f.read().strip().split(',')))
    except FileNotFoundError:
        counts = [0, 0, 0]

    # Convert car counts to densities (you can adjust the factor as needed)
    road_1_density = counts[0]  # Density for road 1
    road_2_density = counts[1]  # Density for road 2
    road_3_density = counts[2]  # Density for road 3

    densities = [road_1_density, road_2_density, road_3_density]

    # Get green light timings based on densities
    signal_times = traffic_system.get_signal_times(densities)

    # Write the signal times to the file
    with open("signal_times.txt", "w") as f:
        f.write(','.join(map(str, signal_times)))

    # Print results
    print(f"\n🚦 Traffic Densities: {densities}")
    print(f"🟢 Green Light Times: {signal_times}\n")

    time.sleep(5)  # Simulate cycle delay
