def sort(list):
    for i in range(len(list)-1):
        for j in range(i):
            if list[j] > list[j+1]:
                # print("lio")
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
            # else:
            #     print("not working")


list = [2, 3, 1, 7, 4, 6, 5, 80, 12, 33, 97, 96]
sort(list)
print(list)
