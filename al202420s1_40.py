def list_operation(nlist):
    for i in range(len(nlist)):
        if i % 2 == 0:
            nlist[i] = nlist[i] **2
        else:
            nlist[i] = nlist[i] + 3

    return nlist
numbers = [1,2,3,4,5]
output = list_operation(numbers)
print(output)