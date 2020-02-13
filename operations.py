from mySet import mySet

def callOp(list1, list2, operation):

    retList = mySet()

    if operation == "and":
        retList = list1.__and__(list2)
        return True, retList
    elif operation == "or":
        retList = list1.__or__(list2)
        return True, retList
    elif operation == "not":
        retList = list1.__sub__(list2)
        return True, retList
    elif operation == "":
        retList = list1.__or__(list2)
        return True, retList
    else:
        return False, retList
