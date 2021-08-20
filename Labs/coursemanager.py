"""
Name:  Audrey Zhu
Assignment: Project 2
Date: 3/4/21
Description:  This program is a course manager that allows users to list,
              add, and drop courses, as well as sort courses in ascending
              or descending order.
"""

def showoptions():
    """
    Displays all options and returns user choice
    :return: the user's choice
    """
    # print the options
    print("Please choose one of the following:")
    print("\t1. List all courses")
    print("\t2. Add a course")
    print("\t3. Drop a course")
    print("\t4. Sort courses in ascending order of course name")
    print("\t5. Sort courses in descending order of course name")
    print("\t6. Exit")

    # get option from user
    opt = input("\nEnter your option: ").strip()

    # check if user entered an invalid choice
    if opt == "" or not opt.isnumeric():
        return 0

    return int(opt)


def displaylist(ls):
    """
    Displays all the courses the user is taking
    :return: none
    """
    if len(ls) == 0:
        print("\nYour course list is empty")
    else:
        print("\nCourse List: ")
        for c in ls:
            print(c)

# ---------- MAIN PROGRAM ----------


# initialize empty list
courselist = []

# when exit is has not been chosen, repeat the following
while True:
    action = showoptions()

    # what to do with action
    if action == 1:
        displaylist(courselist)
    elif action == 2:
        add = input("Enter the course name: ")
        courselist.append(add)
    elif action == 3:
        drop = input("Enter the course name to drop: ")
        if drop in courselist:
            courselist.remove(drop)
        else:
            print("\"{}\" was not found in your course list.\n".format(drop))
        displaylist(courselist)
    elif action == 4:
        courselist.sort()
        displaylist(courselist)
    elif action == 5:
        courselist.sort(reverse=True)
        displaylist(courselist)
    elif action == 6:
        print("\nThank you for using my course manager.")
        break
    else:
        print("\nInvalid Selection. Please try it again.")

    print()