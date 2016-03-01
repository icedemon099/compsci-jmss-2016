total = 0
print("Keep on entering numbers. Enter -1 to finish. ")
while True:
    try:
        text = input("")
        num = float(text)
        if num != -1.0:
            total += float(num)
        else:
            print(total)
            break
    except:
        print("That was not a valid number! Please try again")
