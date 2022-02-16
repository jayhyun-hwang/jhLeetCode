def fizzBuzz(n):
    # Write your code here
    for i in range(1, n+1):    
        res = ""
        if i % 3 == 0:
            res += "Fizz"
        if i % 5 == 0:
            res += "Buzz"
        if len(res) < 1:
            res = i
        print(res)

fizzBuzz(15)