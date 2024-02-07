from datetime import datetime, timedelta

# https://strftime.org/

date = datetime.now() + timedelta(days=1)

date = date.strftime('%Y%m%d')

print(date)
