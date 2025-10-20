n = -11.0

while True:
    current_input = float(input())

    if current_input == 999:
        break

    if n < -10:
        n = current_input
    else:
        print("{:.2f}".format(current_input - n))
        n = current_input