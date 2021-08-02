'''
calculate the time difference between two times
'''
from datetime import datetime
s1='10:33:26'
s2='18:15:49'
FMT='%H:%M:%S'
tdelta=datetime.strptime(s2,FMT)-datetime.strptime(s1,FMT)
print(tdelta)
