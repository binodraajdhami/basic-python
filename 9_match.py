month = "january"

match month:
    case "sunday":
        print("Today is Sunday!")

    case "monday":
        print("Today is Monday!")

    case "tuesday":
        print("Today is Tuesday!")

    case "wednesday":
        print("Today is Wedneday")

    case "thursday":
        print("Today is Thursday!")

    case "friday":
        print("Today is Friday!")

    case "saturday":
        print("Today is Saturday!")

    case _:
        print("Invalid Day!")
