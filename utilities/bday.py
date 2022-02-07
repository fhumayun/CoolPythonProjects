from datetime import datetime
now = datetime.now()
bday = datetime(now.year, 2, 1)
if bday < now:
    bday = datetime(now.year + 1, 2, 1)
diff = bday - now
print(diff.days)