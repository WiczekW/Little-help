import datetime

def validate(date, start_date, end_date):
   return start_date < date < end_date


date = datetime.date.today()
start_date = datetime.date(1995, 1, 1)
end_date = datetime.date(2025, 1, 18)


