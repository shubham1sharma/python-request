from urllib.request import urlopen

from time import time
page=urlopen("https://en.wikipedia.org/wiki/HTML")

t1=time()
output=page.read()
t2=time()
page.close()
t=t2-t1
print(round(t,3))
