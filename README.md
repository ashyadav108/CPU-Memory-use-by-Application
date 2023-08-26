# Application Power Usage Monitor

The **Application Power Usage Monitor** is a Python script that enables monitoring of an application's CPU and memory consumption over time using the `psutil` library.

**NOTE:** 
Estimating the power consumption of a laptop's CPU based solely on its usage can be challenging due to various factors that influence power consumption. Power consumption depends not only on CPU usage but also on factors like the CPU's clock frequency, voltage, architecture, workload type, efficiency, and other hardware components.
## Features

- Real-time monitoring of CPU usage (as a percentage) and memory usage (in megabytes) of a specified application.
- Calculation of average CPU usage based on the number of CPU cores.
- User-friendly input for providing the target application's Process ID (PID).
- Handling of errors, including invalid PIDs and missing processes.

## Requirements

- Python 3.x
- `psutil` library: You can install it using the following command:


## Usage

1. Clone or download this repository to your local machine.
2. Open PyCharm and create a new Python project.
3. Copy and paste the script provided in `application_power_usage_monitor.py` into a new Python file within your PyCharm project.
4. Ensure you have the required `psutil` library installed by running:
5. In the Python file, run the script by clicking the "Run" button or right-clicking in the editor and selecting "Run".
6. Follow the on-screen instructions to provide the Process ID (PID) of the application you want to monitor.
7. Press `Ctrl + C` within the terminal or PyCharm console to stop monitoring.

## How It Works

1. The script takes a target PID as input and initiates monitoring of the application's resource usage.
2. It records the initial CPU and memory usage of the application.
3. Within a loop, it calculates the change in CPU and memory usage over a one-second interval.
4. The script calculates and displays the elapsed time, average CPU usage (across all cores), and memory usage.
5. The monitoring process continues until manually stopped.

## Contributing

Contributions to this project are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request in this repository.

## License

This project is licensed under the [MIT License](LICENSE).



