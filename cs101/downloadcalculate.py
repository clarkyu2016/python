# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download 
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size 
# is given in megabytes (MB).
def convert_seconds(s):
    h = int(s*1.0) / 3600
    m = int((s - h*3600)*1.0/60)
    s = s- h*3600 - m * 60
    result =''
    if h==1:
        result += str(h)+" hour, "
    else:
        result += str(h)+" hours, "
    if m==1:
        result += str(m)+" minute, "
    else:
        result += str(m)+" minutes, "
    if s==1:
        result += str(s)+" second"
    else:
        result += str(s)+" seconds"
    return result
            
            
def transKB(a,x):
    n = 1024
    if x[1] == "b":
        a = a*1.0/8
    if x[0] == "M":
        a = a*n
    if x[0] =="G":
        a = a*n*n
    if x[0] =="T":
        a = a*n*n*n
    return a

def download_time(a,x,b,y):
    s = 0
    a = transKB(a,x)
    b = transKB(b,y)
    s= a*1.0/b
    return convert_seconds(s)
    



print download_time(1024,'kB', 1, 'MB')
#>>> 0 hours, 0 minutes, 1 second

print download_time(1024,'kB', 1, 'Mb')

#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print download_time(13,'GB', 5.6, 'MB')
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print download_time(13,'GB', 5.6, 'Mb')
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print download_time(10,'MB', 2, 'kB')
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print download_time(10,'MB', 2, 'kb')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable
