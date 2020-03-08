pos = 0


def linear_search(list,n):


    for i in range(len(list1)):
        if list[i] == n:
            globals()['pos'] = i
            return True
        else:
            False


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 3

if linear_search(list1, n):
    print("found at ", pos+1)
else:
    print("not found")


