import urllib2
import time

t1 = time.time()
print(t1)
print("Open Success")
urllib2.urlopen("http://1.1.1.3/ajaxlogout?_t=1505955898355").read()
while(1):
    t2 = time.time()
    if t2-t1 == 1200:
        t1 = t2
        print(t2)
        urllib2.urlopen("http://1.1.1.3/ajaxlogout?_t=1505955898355").read()