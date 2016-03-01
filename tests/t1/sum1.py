# write a program that reads in 10 numbers, then prints the sum of those
while True:
    try:
        nums = input("Please enter 10 numbers, sepearated by a space. ")
        nums = nums.split()
        total = 0
        if len(nums) == 10:
            for num in nums:
                total += float(num)
        else:
            raise
        print(total)
        break
    except:
        print("That was not a valid seqeunce! Please try again")
