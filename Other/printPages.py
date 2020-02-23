from Other.colors import colors

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
        print(colors.CYAN + "BACK (B)" + colors.END)
        print(colors.CYAN + "NEXT (N)" + colors.END)
    #    print(colors.CYAN + "\t\tBACK (B)" + colors.END)
        print(colors.CYAN + "Change number of pages (C)" + colors.END)
        print(colors.CYAN + "Exit (X)" + colors.END)
        print()
        option = input("Your input: ")

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
    print(colors.BLUE + "RANK & PAGES:" + colors.END)
    print()
    for i in range(first, last, 1):
        print(colors.BLUE + "%5s" % (str(i + 1)) + ".", "%10.2f " % list[i].getRang(), list[i].getPage() + colors.END)
