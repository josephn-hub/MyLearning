import pandas as pd
import datetime
from datetime import date
import logging

logging.basicConfig(level=logging.DEBUG)

dt = pd.date_range('01-01-2023', '01-31-2023')
idx = pd.DatetimeIndex(dt)
print(idx)


today_date = datetime.datetime.today()
logging.info(today_date)

format_date = today_date.strftime('%Y/%m/%d')

format_date_strptime = datetime.datetime.strptime(format_date, '%Y/%M/%d')
logging.info(format_date)
logging.info(type(format_date))
logging.info(format_date_strptime)


