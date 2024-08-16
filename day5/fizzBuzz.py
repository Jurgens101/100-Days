#printing numbers from 1 to 100, if divided by 3 then return fizz, if divided by 5 then return buzz, if divisible by both then return fizzbuzz
for i in range(1,101):
    if i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0: 
        print("Fizz")
    else:
        print(i)
