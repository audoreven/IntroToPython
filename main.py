# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name} ')  # Press Ctrl+F8 to toggle the breakpoint.
    list1 = [x for x in range(1, 5)]
    list2 = [2*x for x in list1]
    list3 = [x for x in list2 if x < 4]
    list3.append(1)
    list3.sort()

    print(list1)
    print(list2)
    print(list3)

    sent = "Hello, my name is Audrey";
    words = sent.split()
    print(words)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
