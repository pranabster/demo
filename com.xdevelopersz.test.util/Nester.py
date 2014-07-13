def printList(theList):
    for item in theList:
        if isinstance(item, list):
            printList(item)
        else:
            print(item)    