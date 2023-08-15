a, b = map(str, input().split())

five_to_six_a, five_to_six_b = a.replace('5', '6'), b.replace('5', '6')

six_to_five_a, six_to_five_b = a.replace('6', '5'), b.replace('6', '5')


print(int(six_to_five_a) + int(six_to_five_b), int(five_to_six_a) + int(five_to_six_b))
