import time
import webbrowser

no_breaks = 3
break_count = 0
# Open web browser every 30 minutes
print "This program started on "+time.ctime()
while break_count < no_breaks:
    time.sleep(30 * 60)
    webbrowser.open("https://www.youtube.com/watch?v=amtuB-2wGeQ")
    break_count = break_count + 1
