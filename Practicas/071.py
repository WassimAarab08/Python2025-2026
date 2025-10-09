letra ="a"

match letra :
    case "a" |"e"|"u"| "i":
        print("Es vocal")
    case "("|")"|"/"|"%"|"*":
        print("Es un caracter especial")
    case _:
        print("Es consonate ")
