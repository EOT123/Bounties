# 10/30/17
# Always positive - No matter negative/positive input=positive
print("")
print("_______________________________________")
print("Positive Numbers")
print("_______________________________________")
print("")
while True:
    num = int(input('Enter A Number To Be Positive: '))
    if num > 0:
        print("Your Positive Number Is:", num)
    elif num < 0:
        print("Your Positive Number Is: ", -num)
    print("_______________________________")
    print("")
# Done
