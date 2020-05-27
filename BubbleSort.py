oldlist = [10,22,54,67,54,69,34,22,35]

def BubbleSort(mylist):
    last_item = len(mylist)-1
    for z in range(0, last_item):
        for x in range(0,last_item):
            print(mylist)
            if mylist[x] > mylist[x+1]:
                mylist[x],mylist[x+1] = mylist[x+1],mylist[x]

    return(mylist)

print("Old List:",oldlist)
newList = BubbleSort(oldlist).copy()
print("New List: ",newList)