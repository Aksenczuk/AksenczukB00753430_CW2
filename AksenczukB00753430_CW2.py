def main():
    menu()
    selection()


def menu():
    print("「MAIN MENU」")
    print("1 >>> To see a summary statement\
    \n2 >>> To see a list of employees\
    \n3 >>> To see a report of total salary bill\
    \n4 >>> To see the average salary of all employees\
    \n5 >>> To add a new employee\
    \n6 >>> To see the number of employees grouped by each position\
    \n7 >>> To see which employees earn above an inserted salary threshold\
    \n8 >>> To exit the program\
    \n9 >>> To delete an employee")


def selection():
        selection_loop = True
        print("\n「MAIN MENU」")

        while selection_loop:  # Loops the menu selection until an appropriate answer is inserted
            try:
                user_input = int(input("Menu >>> "))
                if 9 >= user_input >= 1:
                    if user_input == 1:
                        menu_1()
                    elif user_input == 2:
                        menu_2()
                    elif user_input == 3:
                        menu_3()
                    elif user_input == 4:
                        menu_4()
                    elif user_input == 5:
                        menu_5()
                    elif user_input == 6:
                        menu_6()
                    elif user_input == 7:
                        menu_7()
                    elif user_input == 8:
                        menu_8()
                    elif user_input == 9:
                        menu_9()
            except ValueError:  # If the user enters something other than the allowed integers, it will let them know
                print("You must enter an integer between 1 and 9")


def func_1_3_4_7(num):
    count = len(CONTENTS)
    over_salary = 0
    check1 = True

    if num == 1:
        print("Number of records read from file:", count)

    elif num == 3 or num == 4 or num == 7:
        total_salary = 0

        if num == 7:
            over_salary = input("Over what salary threshold would you like employees to be shown? ")
            try:
                if int(over_salary) == over_salary:
                    check1 = True
            except ValueError:
                check1 = False
                print("You must enter an integer")

        for i in range(len(CONTENTS)):  # Splits the contents of CONTENTS to get the salary of each employee
            split_salary = CONTENTS[i]  # and changed the type of the variable from list to int
            s_salary = split_salary.split(',')[-2:-1]
            s_ename = ''.join(split_salary.split(',')[1:2])
            string_salary = ''.join(s_salary)
            salary = int(string_salary)

            if num == 7:
                if check1 is True:
                    if salary > over_salary:  # displays the name & salary of employees who earn about the inserted threshold
                        # str_salary = str(salary)
                        # salary_contents = [i for i in CONTENTS if str_salary in i]
                        print(s_ename+": "+str(salary))
            else:
                total_salary += salary

        if num == 3:  # Prints the total salary bill and formats it into £25,000.00
            print("The total salary bill is: £", format(total_salary, ',.2f'), sep='')

        elif num == 4:  # Prints the average amount employees earn and formats it into £25,000.00
            avg_salary = total_salary / count
            print("Average salary of all employees: £", format(avg_salary, ',.2f'), sep='')

    selection()


def func_5():
    loop = True
    counter_name = 0
    counter_age = 0
    counter_position = 0
    counter_salary = 0
    counter_yrs = 0
    emp_name = " "
    emp_position = ' '
    emp_age = 0
    emp_salary = 0
    emp_yrs = 0
    largest_empid = 0

    for i in range(len(CONTENTS)):
        c_list = CONTENTS[i]
        s_empid = c_list.split(',')[0:1]  # Gets the current largest emp_no and
        string_empid = ''.join(s_empid)  # adds 1 to it for the new employee
        largest_empid = int(string_empid)
        if largest_empid >= largest_empid:
            largest_empid = largest_empid + 1

    while loop:  # Loop for employee details, wont stop until everything is inserted
        if counter_name == 0:
            emp_name = input("Enter the employees' first and last name: ")
            counter_name = 1

        if counter_age == 0:
            emp_age = input("Enter the employees' age: ")
            counter_age = 1

        if counter_position == 0:
            emp_position = input("Enter the employees' position in the company: ")
            counter_position = 1

        if counter_salary == 0:
            emp_salary = input("Enter the employees' salary: £")
            counter_salary = 1

        if counter_yrs == 0:
            emp_yrs = input("Enter the years the employee has worked: ")
            counter_yrs = 1

        if all(x.isalpha() is False or x.isspace() for x in emp_name):  # Checks if the string only has letters
            print("Employee name cannot include digits or be empty")  # and if its empty
            counter_name = 0

        if all(x.isalpha() is False or x.isspace() for x in emp_position):  # Checks if the string only has letters
            print("Employee position cannot include digits or be empty")  # and if its empty
            counter_position = 0

        if emp_age.isdigit() is False:  # Checks if the string only has digits
            print("Employees' age must be a number")
            counter_age = 0

        if emp_salary.isdigit() is False:  # Checks if the string only has digits
            print("Employees' salary must be a number")
            counter_salary = 0

        if emp_yrs.isdigit() is False:  # Checks if the string only has digits
            print("The number of years the employee has worked must be a number")
            counter_yrs = 0

        if emp_age.isdigit():  # Checks if the digit is less than 0
            if int(emp_age) < 0:
                print("The employees' age cannot be less than 0")
                counter_age = 0

        if emp_salary.isdigit():  # Checks if the digit is less than 0
            if int(emp_salary) < 0:
                print("The employees' salary cannot be less than 0")
                counter_age = 0

        if emp_yrs.isdigit():  # Checks if the digit is less than 0
            if int(emp_yrs) < 0:
                print("The employees' years worked cannot be less than 0")
                counter_age = 0
        # ˅˅ Checks if all the validation is done by counting up the flags in the code
        if counter_name + counter_age + counter_position + counter_salary + counter_yrs == 5:
            break
    l_empid = "%03d" % largest_empid  # Makes sure the emp_id has 3 digits

    check = input("Are you sure you want to add the employee\nEmployee Name: " + emp_name
                  + "\nEmployee Age: " + emp_age + "\nEmployee Position: " + emp_position + "\nEmployee Salary: £"
                  + emp_salary + "\nYears the Employee has worked: " + emp_yrs + "\n(Y/N)").upper()

    if check == 'Y':
        new_employee = [l_empid, emp_name, emp_age, emp_position, emp_salary, emp_yrs]  # makes the variables into a list
        n_employee = ', '.join(new_employee)  # Adds a comma between each variable
        # print(n_employee)
        CONTENTS.append(n_employee)  # Adds the new employee to the list CONTENTS
        print("The employee has been successfully added")
    else:
        selection()


def func_9():
    deleted = 0
    check1 = True
    try:
        user_emp = int(input("Enter the employee number of the employee you wish to delete: "))
        check1 = True
    except ValueError:
        check1 = False
        print("You must enter an integer")

    if check1 is True:
        emp_no = "%03d" % user_emp  # Makes sure the emp_id has 3 digits

        for i in range(len(CONTENTS)):  # Goes through the list to compare the user input to the emp_id's
            emp_list = CONTENTS[i]
            s_empno = emp_list.split(',')[0:1]
            string_empno = ''.join(s_empno)
            if emp_no == string_empno:  # Compares user input to CONTENTS' emp_id's
                print(emp_list)
                check = input('Are you sure you want to delete this employee? (Y/N): ').lower()
                if check == 'y':
                    del CONTENTS[int(user_emp) - 1]  # Deletes the employee from the list CONTENTS
                    deleted = 1
                    break
        if deleted == 0:  # If user input is not in the list CONTENTS
            if user_emp not in CONTENTS:
                print('This employee number does not exist on this system')
        selection()
    # Delete based on emp no?
    # Delete based on name? (2 ppl could have the same name)
    # Delete based on index
    # Double check if user wants to delete
    # Del CONTENTS{INDEX}


def menu_1():
    print("\n「MENU 1」")
    num = 1
    func_1_3_4_7(num)


def menu_2():
    print("\n「MENU 2」")
    # Calculate the number of employees by counting the number of rows
    print('\n'.join(map(str, CONTENTS)))
    selection()


def menu_3():
    print("\n「MENU 3」")
    num = 3
    func_1_3_4_7(num)


def menu_4():
    print("\n「MENU 4」")
    num = 4
    func_1_3_4_7(num)


def menu_5():
    print("\n「MENU 5」")
    func_5()


def menu_6():
    print("\n「MENU 6」")
    role_dict = {}

    for i in range(len(CONTENTS)):  # Goes through the list CONTENTS to find all the roles
        split_roles = CONTENTS[i]
        s_role = split_roles.split(',')[3:4]

        for role in s_role:

            if role in role_dict:  # If the role exists in role_dict adds 1 to the amount of people
                role_dict[role] = int(role_dict[role]) + 1
            else:  # Adds new roles into the dictionary role_dict
                role_dict[role] = 1

    for key, value in role_dict.items():  # Displays the amount of people in each role
        print(key + ': ', value)
    selection()


def menu_7():
    print("\n「MENU 7」")
    num = 7
    func_1_3_4_7(num)


def menu_8():
    loop = True
    print("\n「MENU 8」")

    while loop:
        check = input("Are you sure you want to close the program?(Y/N)\
        \nOption >>> ").upper()
        if check == 'Y':
            exit()  # Closes the program
        elif check == 'N':
            selection()
        else:
            print("You must insert either 'Y' or 'N'")


def menu_9():
    print("\n「MENU 9」")
    func_9()


with open("CW2_Emp_Dataset.txt") as text:  # Reads in the text file and saves it into a list
    CONTENTS = text.read().splitlines()[1:]
main()
