## ISP Monitor

This project's goal is to monitor home internet providers for latency and packet loss. The server performs a ping and traceroute every five minutes, and displays the results for the user based on their home IP address. Results are held for 24 hours. Anomalous results with packet loss or latency are held for seven days. Monitors for IP addresses that haven't been viewed for seven days are removed from the system.


## Installation requirements

```
pip install -r requirements.txt

*/5 * * * * /home/user/ispmonitor/ispmonitorenv/bin/python3 /home/user/ispmonitor/manage.py get_result

0 * * * * /home/user/ispmonitor/ispmonitorenv/bin/python3 /home/user/ispmonitor/manage.py delete_results_gte_24_hours

0 1 * * * /home/user/ispmonitor/ispmonitorenv/bin/python3 /home/user/ispmonitor/manage.py purge_seven_days
```
