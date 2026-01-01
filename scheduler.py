# scheduler.py
import schedule
import time

from main import run_cycle
from monitor.heartbeat import heartbeat

# основной цикл анализа рынка
schedule.every(5).minutes.do(run_cycle)

# мониторинг, что процесс жив
schedule.every(10).minutes.do(heartbeat)

while True:
    schedule.run_pending()
    time.sleep(1)
