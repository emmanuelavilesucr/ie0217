try:
    event_numbers = [2, 4, 6, 8]
    print(event_numbers[5])


except ZeroDivisionError:
    print("Denominator cannot be 0.")


except IndexError:
    print("Index Out of Bound.")

