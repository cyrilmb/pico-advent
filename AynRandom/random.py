d = {}
s = []
with open("bbcode.txt") as text:
    for line in text:
       (key, val) = line.split()
       d[int(key)] = val
       s = sorted(d.items())
    print(s)