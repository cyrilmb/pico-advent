d = {}
s = []
with open("bbcode.txt") as text:
    for line in text:
       (key, val) = line.split()
       d[int(key)] = val

s = sorted(d.items())

def divide(l, n):
    result = []
    start = 0
    while start < len(l):
        result.append(l[start:start + n])
        start += n
        n += 1
    return result

n = 1
pyramid = divide(s, n)

last_words = [sublist[-1] for sublist in pyramid]

print(last_words)