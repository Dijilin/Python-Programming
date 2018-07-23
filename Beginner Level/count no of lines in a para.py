import re
import sys
d=sys.stdin.read()
if(len(d)<=1000):
    da=len(re.split('\n',d))
print(da)
