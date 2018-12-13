## Installation requirements

*/5 * * * * /home/me/ispmonitor/ispmonitorenv/bin/python3 /home/me/ispmonitor/manage.py run_ping
*/5 * * * * /home/me/ispmonitor/ispmonitorenv/bin/python3 /home/me/ispmonitor/manage.py delete_results_gte_24_hours
0 1 * * * /home/me/ispmonitor/ispmonitorenv/bin/python3 /home/me/ispmonitor/manage.py delete_stale_monitors

