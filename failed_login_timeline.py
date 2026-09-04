from datetime import datetime
from collections import defaultdict

LOG_FILE = "login_events.log"
TIME_WINDOW_MINUTES = 5
FAILED_LOGIN_THRESHOLD = 3

failed_logins = defaultdict(list)

try:
    with open(LOG_FILE, "r") as file:
        for line in file:
            parts = line.strip().split(",")

            if len(parts) < 4:
                continue

            timestamp_text = parts[0].strip()
            event_type = parts[1].strip()
            username = parts[2].strip()
            ip_address = parts[3].strip()

            if event_type != "FAILED_LOGIN":
                continue

            timestamp = datetime.strptime(
                timestamp_text,
                "%Y-%m-%d %H:%M:%S"
            )

            failed_logins[ip_address].append(timestamp)

except FileNotFoundError:
    print(f"Error: {LOG_FILE} was not found.")
    exit()

print("=== Failed Login Timeline Analyzer ===")
print()

alerts_found = False

for ip, timestamps in failed_logins.items():
    timestamps.sort()

    for i in range(len(timestamps)):
        window_start = timestamps[i]
        count = 1

        for j in range(i + 1, len(timestamps)):
            difference = timestamps[j] - window_start

            if difference.total_seconds() <= TIME_WINDOW_MINUTES * 60:
                count += 1
            else:
                break

        if count >= FAILED_LOGIN_THRESHOLD:
            print(f"ALERT: {ip}")
            print(
                f"{count} failed logins detected within "
                f"{TIME_WINDOW_MINUTES} minutes."
            )
            print()
            alerts_found = True
            break

if not alerts_found:
    print("No suspicious failed-login timeline detected.")

print()
print("Analysis complete.")
