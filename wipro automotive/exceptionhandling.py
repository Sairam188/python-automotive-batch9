try:
 num=int(input("Enter a number: "))
 result=10/num
 print(f"result is :{result}" )
except ZeroDivisionError:
    print("You cannot divide by zero")
except ValueError:
    print("The divisor is non numeric")
finally:
    print("Program ended")
