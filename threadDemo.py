''' 
At u, we define a function that we want to use in a new thread. To create
a Thread object, we call threading.Thread() and pass it the keyword argu-
ment target=takeANap v. This means the function we want to call in the new
thread is takeANap() . Notice that the keyword argument is target=takeANap ,
not target=takeANap() . This is because you want to pass the takeANap() func-
tion itself as the argument, not call takeANap() and pass its return value.
After we store the Thread object created by threading.Thread() in threadObj ,
we call threadObj.start() w to create the new thread and start executing the
target function in the new thread. When this program is run, the output
will look like this

'''

import threading, time 
print 'Start of Program.'

def takeANap():
	time.sleep(5)
	print 'Wake Up!'
threadObj = threading.Thread(target = takeANap)
threadObj.start()

print 'End of Program.'

''' 
This can be a bit confusing. If print('End of program.') is the last line of
the program, you might think that it should be the last thing printed. The
reason Wake up! comes after it is that when threadObj.start() is called, the tar-
get function for threadObj is run in a new thread of execution. Think of it as
a second finger appearing at the start of the takeANap() function. The main
thread continues to print('End of program.') . Meanwhile, the new thread
that has been executing the time.sleep(5) call, pauses for 5 seconds. After it
wakes from its 5-second nap, it prints 'Wake up!' and then returns from the
takeANap() function. Chronologically, 'Wake up!' is the last thing printed by
the program.
Normally a program terminates when the last line of code in the file
has run (or the sys.exit() function is called). But threadDemo.py has two
threads. The first is the original thread that began at the start of the pro-
gram and ends after print('End of program.') . The second thread is created
when threadObj.start() is called, begins at the start of the takeANap() func-
tion, and ends after takeANap() returns.
A Python program will not terminate until all its threads have termi-
nated. When you ran threadDemo.py, even though the original thread had
terminated, the second thread was still executing the time.sleep(5) call.


'''











