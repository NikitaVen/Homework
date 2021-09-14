
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



def length(str):
    len = 0
    for i in str:
        len += 1
    return len


while(True):
    temp = str(input("Enter your string(ex to exit): "))
    if temp.strip() == "ex":
        break
    else:
        print("string length is " + str(length(temp)))
