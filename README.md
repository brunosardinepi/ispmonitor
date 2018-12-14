## Installation requirements

*/5 * * * * /home/user/ispmonitor/ispmonitorenv/bin/python3 /home/user/ispmonitor/manage.py run_ping
*/5 * * * * /home/user/ispmonitor/ispmonitorenv/bin/python3 /home/user/ispmonitor/manage.py delete_results_gte_24_hours
0 1 * * * /home/user/ispmonitor/ispmonitorenv/bin/python3 /home/user/ispmonitor/manage.py purge_seven_days

