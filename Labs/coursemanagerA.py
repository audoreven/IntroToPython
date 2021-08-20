"""
Name:  Audrey Zhu
Assignment: Project 2
Date: 3/4/21
Description:  This program is a course manager that allows users to list,
              add, and drop courses, as well as sort courses in ascending
              or descending order.
"""


def show_options():
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


def display_list(ls):
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


def bubble_sort(ls, reverse=False):
    """
    Sorts a given list
    :param ls: list to be sorted
    :param reverse: the specified ordering
    :return: the sorted list
    """
    swapped = False
    for i in range(len(ls)):
        for j in range(len(ls)-1-i):
            if not reverse and ls[j] > ls[j+1]:
                ls[j], ls[j+1] = ls[j+1], ls[j]
                swapped = True
            if reverse and ls[j] < ls[j+1]:
                ls[j], ls[j + 1] = ls[j + 1], ls[j]
                swapped = True
        if not swapped:
            break
        swapped = False
    return ls


def linear_search(ls, key):
    """
    Searches a given list for a specific value
    :param ls: list to search for key in
    :param key: what to search for in the list
    :return: the index of key in ls, if key is not in ls, return -1
    """
    for i in range(len(ls)):
        if ls[i] == key:
            return i
    return -1


# ---------- MAIN PROGRAM ----------


# initialize empty list
course_list = []

# when exit is has not been chosen, repeat the following
while True:
    action = show_options()

    # what to do with action
    if action == 1:
        display_list(course_list)
    elif action == 2:
        add = input("Enter the course name: ")
        course_list.append(add)
    elif action == 3:
        drop = input("Enter the course name to drop: ")
        if linear_search(course_list, drop) >= 0:
            course_list.remove(drop)
        else:
            print("\"{}\" was not found in your course list.\n".format(drop))
        display_list(course_list)
    elif action == 4:
        course_list = bubble_sort(course_list)
        display_list(course_list)
    elif action == 5:
        course_list = bubble_sort(course_list, True)
        display_list(course_list)
    elif action == 6:
        print("\nThank you for using my course manager.")
        break
    else:
        print("\nInvalid Selection. Please try it again.")

    print()