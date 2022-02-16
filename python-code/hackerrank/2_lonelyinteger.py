def lonelyinteger(a):
    # Write your code here
    dict1 = dict()
    for val in a:
        if val in dict1:
            del dict1[val]
        else:
            dict1[val] = True
    print(list(dict1.keys())[0])

lonelyinteger([1,2,3,4,3,2,1])
