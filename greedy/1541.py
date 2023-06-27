#1541 잃어버린 괄호
math = input()
math += '+'
arr = []
number = ''
last_symbol = ''
for word in list(math):
    if word.isdigit():
        number += word
    else:
        if len(last_symbol) != 0 and last_symbol == '-':
            arr.append(int(number) * -1)
        else:
            arr.append(int(number))

        number = ''

        if last_symbol == '-' and word == '+':
            last_symbol = last_symbol
        else:
            last_symbol = word

print(sum(arr))

def solution() :
    math = '10+10-100-100+300+100-1000+100-100'
    math += '+'
    arr = []
    number = ''
    last_symbol = ''
    for word in list(math):
        if word.isdigit():
            number += word
        else:
            if len(last_symbol) != 0 and last_symbol == '-':
                arr.append(int(number) * -1)
            else:
                arr.append(int(number))

            number = ''

            if last_symbol == '-' and word == '+':
                last_symbol = last_symbol
            else:
                last_symbol = word

    print(sum(arr))

if __name__ == "__main__" :
    solution()


'''
arr = input().split('-')
s = 0
for i in arr[0].split('+'):
    s += int(i)
for i in arr[1:]:
    for j in i.split('+'):
        s -= int(j)
print(s)
'''
