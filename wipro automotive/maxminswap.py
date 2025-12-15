print("Get Max Min Swap Value of given variables")
print("1.Max 2.Min 3.Swap")
a,b=map(int,input("Enter two numbers: ").split(","))
choice=int(input("Enter your choice: "))
if choice==1:
    print("Max value is ",max(a,b))
elif choice==2:
    print("Min value is ",min(a,b))
elif choice==3:
    a,b=b,a
     #print("After swapping %d %d"  %(a,b))
    print(f"After swapping {a} {b}")
else:
    print("Invalid choice")
