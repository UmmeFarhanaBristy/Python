largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done" : break

    try:
        n = int(num)

    except:
        print('Invalid Input')

    else:
        if largest is None:
            largest = n

        if smallest is None:
            smallest = n

        if largest < n:
            largest = n

        if smallest > n:
            smallest = n



print("Maximum is", largest)
print("Minimum is", smallest)
