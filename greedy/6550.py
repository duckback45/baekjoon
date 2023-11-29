while True :
  try :
    s, t = input().split()

    count = 0
    start = 0
    for i in range(len(s)):
        for j in range(start, len(t)):
            start = j
            if s[i] == t[j]:
                count += 1
                break

    if count == len(s):
        print('Yes')
    else:
        print('No')

  except :
    break

