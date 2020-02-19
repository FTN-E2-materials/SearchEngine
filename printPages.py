from colors import colors

def printPages(list):
    number = 10 # na googlu ima 10 linkova na jednoj pretrazi
    first = 0
    last = 0

    if number > list.__len__():
        last = list.__len__()
    else:
        last = number

    while True:
        printPage(list, first, last)
        print()
        print(colors.CYAN + "\tBACK (B) \t\t\t\tNEXT (N)" + colors.END)
    #    print(colors.CYAN + "\t\tBACK (B)" + colors.END)
        print(colors.CYAN + "\t\tChange number of pages (C)" + colors.END)
        print(colors.CYAN + "\t\tExit (X)" + colors.END)

        option = input("\t\tEnter: ")

        if option == "N" or option == "n":
            first += number
            last += number
            if last > list.__len__():
                last = list.__len__()
        elif option == "B" or option == "b":
            if first - number < 0:
                first = 0
                last = number
            else:
                last = first
                first -= number
        elif option == "C" or option == "c":
            no = input("Enter number: ")
            if int(no) < 0:
                print(colors.RED + "Error: please enter a postive integer." + colors.END)
            else:
                number = int(no)
                if first + number > list.__len__():
                    last = list.__len__()
                else:
                    if first == list.__len__():
                        last = first
                        first -= number
                    else:
                        last = first + number
        elif option == "x" or option == "X":
            return

def printPage(list, first, last):
    print(colors.BLUE + "\t\tPAGES:" + colors.END)
    print()
    for i in range(first, last, 1):
        print(colors.BLUE + "\t\t" + list._get(i) + colors.END)
