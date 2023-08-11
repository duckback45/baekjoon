s = input()
s += s[0]
count = 0
for i in range(len(s)):
    if s.find("01", i) == i:
        count += 1

print(count)