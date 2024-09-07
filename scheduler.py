import schedule
import time
from commute_duration import get_route_info

schedule.every(15).minutes.do(get_route_info)

while True:
    schedule.run_pending()
    time.sleep(1)