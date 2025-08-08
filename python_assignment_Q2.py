import psutil
import time

def monitor_cpu(threshold=80):
    print("Monitoring CPU usage...")
    try:
        while True:
            # Get CPU usage averaged over 1 second
            cpu_usage = psutil.cpu_percent(interval=10)

            # Print CPU usage regardless of threshold
            print("Current CPU usage: {}%".format(cpu_usage))

            # Check if usage exceeds threshold
            if cpu_usage > threshold:
                print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")

            # Sleep for a short time to avoid tight looping
            time.sleep(5)

    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    monitor_cpu(80)
