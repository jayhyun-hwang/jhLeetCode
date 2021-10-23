def sol():
    n = 1260
    count = 0
    
    array = [500,100,50,10]

    for coin in array:
        count += n 
        n %= coin
    print(count)

print(sol())