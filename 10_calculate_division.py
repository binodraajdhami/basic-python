percentage = 15

match percentage:
    case ptg if ptg >= 80:
        print("Distinction")

    case ptg if 60 <= ptg < 80:
        print("First Division")

    case ptg if 45 <= ptg < 60:
        print("Second Division")

    case ptg if 32 <= ptg < 45:
        print("Third Division")

    case _:
        print("Fail")
