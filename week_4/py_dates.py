# Write a Python program to subtract five days from current date.
from datetime import datetime, timedelta
today = datetime.now()
result = today - timedelta(5)
    
print( result )

# Write a Python program to print yesterday, today, tomorrow.
from datetime import datetime, timedelta
today = datetime.now()
yesterday = today - timedelta(1)
tomorrow = today + timedelta(1)
print (yesterday, today, tomorrow)

# Write a Python program to drop microseconds from datetime.
import datetime
today = datetime()
without_microseconds = today.strftime('%Y-%m-%d %H:%M:%S')

print(without_microseconds)

# Write a Python program to calculate two date difference in seconds.

import datetime
date1 = input()
date2 = input()

date1 = datetime.strptime(date1, '%Y-%m-%d %H:%M:%S')
date2 = datetime.strptime(date2, '%Y-%m-%d %H:%M:%S')

time_diff = date2 - date1
diff_in_sec = time_diff.total_seconds()

print (diff_in_sec)