def convert_seconds(s):
    h = int(s*1.0) / 3600
    m = int((s - h*3600)*1.0/60)
    s = s- h*3600 - m * 60
    if h != 1:
        if m != 1:
            if s != 1:
                return "%s hours, %s minutes, %s seconds" % (h, m, s)
            else:
                return "%s hours, %s minutes, %s second" % (h, m, s)
        else:
            if s != 1:
                return "%s hours, %s minute, %s seconds" % (h, m, s)
            else:
                return "%s hours, %s minute, %s second" % (h, m, s)            
    else:
        if m !=1:
            if s !=1:
                return "%s hour, %s minutes, %s seconds" % (h, m, s)
            else:
                return "%s hour, %s minutes, %s second" % (h, m, s)
        else:
            if s != 1:
                return "%s hour, %s minute, %s seconds" % (h, m, s)
            else:
                return "%s hour, %s minute, %s second" % (h, m, s)
            
def transKB(a,x):
    print x[1]
    if x[1] == "B":
        a = a
    if x[1] == "b":
        a = a*1.0/8
    if x[0] == "k":
        a = a
    if x[0] == "M":
        a = a*1024
    if x[0] =="G":
        a = a*1024*1024
    if x[0] =="T":
        a = a*1024*1024*1024
    return a

def download_time(a,x,b,y):
    s = 0
    a = transKB(a,x)
    b = transKB(b,y)
    s= a*1.0/b
    return convert_seconds(s)

print download_time(1024,'kB', 1, 'MB')
print download_time(1024,'kB', 1, 'Mb')

