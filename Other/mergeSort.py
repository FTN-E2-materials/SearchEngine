def mergeSort(listForSort):

    if len(listForSort) > 1:

        middle = len(listForSort) // 2
        left = listForSort[:middle]
        right = listForSort[middle:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):

            if left[i].getRang() > right[j].getRang():
                listForSort[k] = left[i]
                i += 1
            else:
                listForSort[k] = right[j]
                j += 1
            k+=1


        while i < len(left):
            listForSort[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            listForSort[k] = right[j]
            j += 1
            k += 1
