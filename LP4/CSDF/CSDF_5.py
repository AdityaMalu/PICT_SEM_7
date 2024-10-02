import re
from datetime import datetime

# Sample event class to store log details
class LogEvent:
    def __init__(self, timestamp, log_level, message):
        self.timestamp = timestamp
        self.log_level = log_level
        self.message = message

    def __repr__(self):
        return f"[{self.timestamp}] {self.log_level}: {self.message}"

# Log Capturing: Function to read logs from a file
def read_logs_from_file(log_file):
    logs = []
    with open(log_file, 'r') as file:
        for line in file:
            # Example log line format: '2023-10-01 12:00:01 [ERROR] Error message'
            match = re.match(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[(\w+)\] (.+)", line)
            if match:
                timestamp = datetime.strptime(match.group(1), "%Y-%m-%d %H:%M:%S")
                log_level = match.group(2)
                message = match.group(3)
                logs.append(LogEvent(timestamp, log_level, message))
    return logs

# Event Correlation: Correlate events by time proximity or event type
def correlate_events(logs, event_type="ERROR", time_window_seconds=60):
    correlated_events = []
    for i, event in enumerate(logs):
        if event.log_level == event_type:
            # Find related events within the time window
            for j in range(i-1, -1, -1):
                time_diff = (event.timestamp - logs[j].timestamp).total_seconds()
                if time_diff <= time_window_seconds:
                    correlated_events.append((logs[j], event))
                else:
                    break
    return correlated_events

# Main function to demonstrate log capturing and event correlation
def main():
    log_file = 'system.log'  # Specify the log file path

    # Capture logs from the log file
    logs = read_logs_from_file(log_file)

    # Correlate events based on event type and time proximity
    correlated_events = correlate_events(logs, event_type="ERROR", time_window_seconds=60)

    # Output the correlated events
    for event_pair in correlated_events:
        print("Correlation found:")
        print(f"Related Event: {event_pair[0]}")
        print(f"Error Event: {event_pair[1]}\n")

if __name__ == "__main__":
    main()
