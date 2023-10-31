# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


keyStr = input(" ")

print(keyStr)

for n in keyStr:
    if keyStr[n].isalpha():
        print(keyStr[n])
    if keyStr[n].isalpha() == False:
        keyStr[n] = 'y'
        print(keyStr[n])



# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
