n = input()

alphabet = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

result = 0
for i in range(len(n)):
    for j in alphabet:
            if n[i] in j:
                result += alphabet.index(j) + 3

print(result)