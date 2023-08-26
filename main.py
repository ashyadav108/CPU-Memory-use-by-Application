import psutil
import time


def get_application_power_usage(pid):
    process = psutil.Process(pid)
    previous_time = time.time()
    previous_cpu_usage = process.cpu_percent()
    previous_memory_usage = process.memory_info().rss

    while True:
        current_time = time.time()
        elapsed_time = current_time - previous_time

        current_cpu_usage = process.cpu_percent()
        cpu_usage_percent = (current_cpu_usage - previous_cpu_usage) / psutil.cpu_count()

        current_memory_usage = process.memory_info().rss
        memory_usage = current_memory_usage - previous_memory_usage

        previous_time = current_time
        previous_cpu_usage = current_cpu_usage
        previous_memory_usage = current_memory_usage

        print(f"Elapsed Time: {elapsed_time:.2f}s")
        print(f"CPU Usage: {cpu_usage_percent:.2f}%")
        print(f"Memory Usage: {memory_usage / (1024 ** 2):.2f} MB")
        print("-" * 30)

        time.sleep(1)  # Adjust the sleep interval as needed


if __name__ == "__main__":
    try:
        # Take the target PID from the user as input
        target_pid = int(input("Enter the PID of the application you want to monitor: "))

        get_application_power_usage(target_pid)
    except ValueError:
        print("Invalid PID. Please enter a valid numerical PID.")
    except psutil.NoSuchProcess:
        print("Process not found.")
    except KeyboardInterrupt:
        print("Monitoring stopped.")
