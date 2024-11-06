# Write a script to print all events from a logfile that happen between 'Test 
# event' and 'Check event'. The log file format is: YYYY-MM-DD hh:mm:ss TEXT. 
# For example, given the logfile:

# 2013-08-25 07:11:55 Normal event
# 2013-08-25 07:33:22 Normal event
# 2013-08-25 07:40:55 Test event
# 2013-08-25 07:40:58 Test event
# 2013-08-25 07:41:32 A event
# 2013-08-25 07:44:13 B event
# 2013-08-25 07:44:13 C event
# 2013-08-25 07:44:13 D event
# 2013-08-25 07:48:55 Check event
# 2013-08-25 07:50:52 Normal event
# 2013-08-25 07:51:10 Test event
# 2013-08-25 07:51:13 E event
# 2013-08-25 07:51:30 Check event

# Output should be:

# 2013-08-25 07:41:32 A event
# 2013-08-25 07:44:13 B event
# 2013-08-25 07:44:13 C event
# 2013-08-25 07:44:13 D event
# 2013-08-25 07:51:13 E event

log = '''
2013-08-25 07:11:55 Normal event
2013-08-25 07:33:22 Normal event
2013-08-25 07:40:55 Test event
2013-08-25 07:40:58 Test event
2013-08-25 07:41:32 A event
2013-08-25 07:44:13 B event
2013-08-25 07:44:13 C event
2013-08-25 07:44:13 D event
2013-08-25 07:48:55 Check event
2013-08-25 07:50:52 Normal event
2013-08-25 07:51:10 Test event
2013-08-25 07:51:13 E event
2013-08-25 07:51:30 Check event
'''

def getEvents(log):
    capture = False
#    with f as open(logFile):
#        for line in log:
    for line in log.splitlines():
        logText = line[20:]
        if (logText == 'Test event'):
            capture = True
            continue
        if (logText == 'Check event'):
            capture = False
        if capture:
            print line
            
getEvents(log)
