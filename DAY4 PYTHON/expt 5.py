import re
str ="she sells sea shells at sea shore"
p1="sea"
rep=' ocean '
ns=re.sub(p1,rep,str,1)
print(ns)
