Failed Login Timeline Analyzer

A Python-based cybersecurity tool that analyzes authentication events and detects repeated failed login attempts occurring within a defined time window.

This project demonstrates basic time-based security event correlation similar to techniques used in Security Operations Center (SOC) monitoring.

Features

- Reads authentication events from a log file
- Extracts timestamps, event types, usernames, and IP addresses
- Tracks failed login attempts by source IP
- Sorts authentication events by timestamp
- Detects repeated failures within a 5-minute window
- Generates an alert when the defined threshold is reached
- Ignores successful login events when counting failed attempts

Detection Rule

The current detection rule generates an alert when:

3 or more failed login attempts occur from the same IP address within 5 minutes.

Example

Sample events:

"2026-09-04 10:00:00,FAILED_LOGIN,john,192.168.1.50"

"2026-09-04 10:01:10,FAILED_LOGIN,john,192.168.1.50"

"2026-09-04 10:03:20,FAILED_LOGIN,john,192.168.1.50"

Result:

"ALERT: 192.168.1.50"

"3 failed logins detected within 5 minutes."

Project Files

- "failed_login_timeline.py" — Main Python analyzer
- "login_events.log" — Sample authentication events
- "README.md" — Project documentation

How It Works

1. Reads authentication events from the log file.
2. Parses each event's timestamp.
3. Collects failed login timestamps for each IP address.
4. Sorts the timestamps chronologically.
5. Compares events within a 5-minute window.
6. Generates an alert when three or more failures occur within that window.

Technologies

- Python
- "datetime"
- "collections.defaultdict"
- Log parsing
- Google Colab
- GitHub

SOC Skills Demonstrated

- Authentication log analysis
- Timestamp parsing
- Time-based event correlation
- Failed-login monitoring
- Basic brute-force detection
- Security alert generation
- Python security automation

Limitations

This project uses a simplified rule-based detection method and sample authentication data. Multiple failed logins do not automatically prove that an attack occurred. Real SOC investigations may also consider usernames, device information, geographic location, asset importance, threat intelligence, and authentication history.

Future Improvements

- Export alerts to CSV
- Include usernames in alert reports
- Add configurable thresholds and time windows
- Detect successful logins following repeated failures
- Add severity classifications
- Correlate activity across multiple security events

Ethical Use

This project is intended for cybersecurity education, defensive security monitoring, and authorized security analysis.

Author

Jawad Hussain

Computer Science Graduate | Aspiring Cybersecurity Analyst
