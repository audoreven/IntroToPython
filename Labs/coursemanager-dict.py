"""
Name:  Audrey Zhu
Assignment: Project 3
Date: 4/17/21
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


def displaylist(dictionary, keys):
    """
    Displays all the courses the user is taking
    :return: none
    """
    if len(keys) == 0:
        print("\nYour course list is empty")
    else:
        print("\n{:15}{:10}{:50}".format("Course Name", "Units", "Semester Taken"))
        for elem in keys:
            print("{:15}{:10}{:50}".format(elem, str(dictionary[elem][0]), dictionary[elem][1]))


# ---------- MAIN PROGRAM ----------


# initialize empty dictionary
courselist = {}

# when exit is has not been chosen, repeat the following
while True:
    action = showoptions()

    # what to do with action
    if action == 1:
        displaylist(courselist, courselist.keys())
    elif action == 2:
        # ask for course name
        add = input("Enter the course name: ")

        # check if the units is number
        try:
            # if it is continue
            units = float(input("Enter the number of units: "))
        except ValueError:
            # if not, exit
            print("\nNumber of units must be a number \n")
            continue

        # ask for sem
        sem = input("Enter the semester taken: ")
        courselist[add] = (units, sem)

    elif action == 3:
        # ask for course to drop
        drop = input("Enter the course name to drop: ")

        # check if course is in dictionary
        try:
            # drop if it is
            courselist.pop(drop)
        except KeyError:
            # error if it is not
            print("\"{}\" was not found in your course list.".format(drop))

        # display list
        displaylist(courselist, courselist.keys())
    elif action == 4:
        displaylist(courselist, sorted(courselist.keys()))
    elif action == 5:
        displaylist(courselist, sorted(courselist.keys(), reverse=True))
    elif action == 6:
        print("\nThank you for using my course manager.")
        break
    else:
        print("\nInvalid Selection. Please try it again.")

    print()
