# LaneX 🚦

### AI-Based Smart Traffic Signal Indication

LaneX is an AI-based traffic management project that uses YOLOv9 object
detection and a custom tracker to detect and count cars from three road
video feeds. The detected vehicle counts are stored and used to
calculate green-light timings for three roads according to traffic
density.

## Features

-   🚗 Vehicle detection using YOLOv9
-   🎯 Basic vehicle tracking with unique IDs
-   📹 Processing of three road videos
-   📊 Live dashboard for vehicle counts and calculated green-light
    timings
-   🚦 Traffic signal timing calculation based on traffic density
-   💾 Shared text files for communication between modules

## Project Structure

``` text
PROJECT/
├── car_counting1.py
├── car_counting2.py
├── car_counting3.py
├── dashboard.py
├── run_system.py
├── traffic_signal.py
├── traffic_signal - Copy.py
├── tracker.py
├── yolov9c.pt
├── road1.mp4
├── road2.mp4
├── road3.mp4
├── car_counts.txt
└── signal_times.txt
```

## How It Works

``` text
Road Videos
    ↓
YOLOv9 Vehicle Detection
    ↓
Vehicle Tracking & Counting
    ↓
car_counts.txt
    ↓
Traffic Density Analysis
    ↓
Green-Light Time Calculation
    ↓
signal_times.txt
    ↓
Dashboard
```

The traffic controller assigns a maximum of 50 seconds to the road with
the highest detected vehicle count. The remaining 70 seconds are
distributed between the other two roads according to their relative
vehicle counts.

## Requirements

-   Windows / Linux / macOS
-   Python 3.10 recommended
-   YOLOv9 model file: `yolov9c.pt`
-   Project videos: `road1.mp4`, `road2.mp4`, `road3.mp4`

Python packages:

``` bash
pip install ultralytics opencv-python matplotlib pandas
```

## Installation

Open a terminal in the project directory:

``` bash
cd "C:\Users\Anmol Gupta\OneDrive\Desktop\Lanex\PROJECT"
```

Create a virtual environment:

``` bash
py -3.10 -m venv venv
```

Activate it:

``` bash
venv\Scripts\activate
```

Install dependencies:

``` bash
python -m pip install ultralytics opencv-python matplotlib pandas
```

Verify the important packages:

``` bash
python -c "import cv2, pandas, matplotlib; from ultralytics import YOLO; print('All packages OK')"
```

## Run the Project

Run the complete system from the project directory:

``` bash
venv\Scripts\python run_system.py
```

The controller starts the three vehicle-counting programs, dashboard,
and traffic-signal calculation program.

## Run Individual Components

Vehicle detection:

``` bash
venv\Scripts\python car_counting1.py
venv\Scripts\python car_counting2.py
venv\Scripts\python car_counting3.py
```

Traffic timing calculation:

``` bash
venv\Scripts\python traffic_signal.py
```

Dashboard:

``` bash
venv\Scripts\python dashboard.py
```

## Output Files

### `car_counts.txt`

Stores the current detected car counts for the three roads:

``` text
road1,road2,road3
```

### `signal_times.txt`

Stores the calculated green-light duration for each road:

``` text
road1,road2,road3
```

## Traffic Signal Logic

For three road densities:

1.  The road with the highest vehicle count receives **50 seconds**.
2.  The remaining **70 seconds** are divided between the other two
    roads.
3.  If both remaining roads have zero vehicles, the 70 seconds are split
    equally.
4.  The calculated timings are written to `signal_times.txt`.

## Important Current Project Notes

-   `traffic_signal.py` currently calculates and prints signal timings;
    it does **not** contain a graphical red/yellow/green signal UI.
-   `dashboard.py` displays green-light timings and vehicle-count graphs
    rather than a three-light traffic-signal graphic.
-   The current `run_system.py` launches the components using `python`;
    when working inside the virtual environment, using the venv Python
    directly is safer.
-   `car_counting2.py` and `car_counting3.py` currently use
    `cv2.waitKey(0)`, which pauses video processing until a key is
    pressed. For continuous playback, this should be changed to
    `cv2.waitKey(1)`.
-   The supplied counting scripts map the videos as follows:
    `car_counting1.py` → `road3.mp4`, `car_counting2.py` → `road2.mp4`,
    and `car_counting3.py` → `road1.mp4`.

These are current implementation details of the supplied project and can
be improved in future versions.

## Future Improvements

-   Add a visual traffic-signal panel showing red, yellow, and green
    states.
-   Connect the active signal state directly to the calculated timing.
-   Improve multi-road synchronization.
-   Use more robust vehicle tracking.
-   Add support for real CCTV/live camera feeds.
-   Improve signal scheduling and fairness between roads.
-   Add a web-based monitoring interface.

## License

This project is intended for educational and project demonstration
purposes. Add an appropriate open-source license before publishing if
required.
