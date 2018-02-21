from datetime import *
import os

##
##class Solution(object):
##    def nextClosestTime(self,time):
##        digits=set(time)
##        while True:
##            time = (datetime.strptime(time,"%H:%M")+ timedelta(minutes=1)).strftime("%H:%M")
##            if set(time)<=digits:
##                return time
##    
##    

now = datetime.now()
then = datetime.fromtimestamp(os.path.getmtime("x.cache"))
tdelta = now - then
seconds = tdelta.total_seconds()
