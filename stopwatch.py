# stopwatch.py - A simple stopwatch program.
# The stopwatch program will need to use the current time, so you will want to
# import the time module. Your program should also print some brief instruc-
# tions to the user before calling input() , so the timer can begin after the user
# presses enter . Then the code will start tracking lap times.

import time 
# Display the program's instructions.
print ('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch.Press Ctrl-C to quit.')
raw_input() # press ENTER to begin
print 'Started.'
startTime = time.time() # get the first lap's start time.
lastTime = startTime
lapNum = 1

# TODO: Start tracking the lap times.
# Step 2: Track and Print Lap Times
try:
	while True:
		raw_input()
		lapTime = round(time.time() - lastTime,2)
		totalTime = round(time.time() - startTime, 2)
		print 'Lap #%s: %s (%s)' % (lapNum, totalTime, lastTime)
		lapNum += 1
		lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
	print '\nDone.'
# we use except because of KeyboardInterrupt error messages.
# It works when Ctrl-C press.
# Here while loop is a infinite loop.
# it calls the raw_input() and waits for enter
# to end a lap.when user press enter that means lap finished.
# when a lap ends we calculate the laptime.
# we subtract the start time of the lap from current time using time.time()
# We calculate the total time elapsed by subtracting
# the overall start time of the stopwatch, startTime ,from the current time
# setting lastTime to the current time, which
# is the start time of the next lap.



































