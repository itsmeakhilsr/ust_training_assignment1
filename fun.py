def fun(a):
    try:
        result = 100 / a 
        print("this is function 1")
        print("Result:", result)
        return a 
    except ZeroDivisionError:
        print("Error: Division by zero!")
        return None

print(fun(30))
