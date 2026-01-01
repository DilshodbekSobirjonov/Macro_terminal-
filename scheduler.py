import schedule
import time
from main import scan_news, daily_sentiment, update_channel_description

schedule.every(5).minutes.do(scan_news)
schedule.every(10).minutes.do(update_channel_description)
schedule.every().day.at("21:00").do(daily_sentiment)

while True:
    schedule.run_pending()
    time.sleep(1)
