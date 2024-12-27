marks = [(1,"amara",96),(2,"rajah",34),(3,"rani",49),(4,"fahim",68)]

i=-1
while i < (len(marks)-1):
    i += 1
    if marks[i][2] < 50:
        continue
    print(marks[i][1],end="")