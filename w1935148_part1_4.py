# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1935148
# Date: 22/11/2022

def get_student_id():  # Function that asks and validates the Students IDs, then returns it as a string.
    while True:
        ids = input("Introduce student id: ")
        if len(ids) != 8 or ids[0] != "w":
            print("Student ID Incorrect")
        else:
            break
    return ids


def histogram(p, t, r, e):  # Function that receives the counters of the module results to then prints them in a histogram
    count = "*"
    # For printing the histogram I used the function '"""' for arrangement and 'f' to use other values inside the
    # print()
    print(f"""
    -----------------------------------------
    Histogram
    Progress {p} : {count * p}
    Trailer {t} : {count * t}
    Retriever {r} : {count * r}
    Exclude {e} : {count * e}
    -----------------------------------------
          """)


def part_2(r):  # Function that receives the list with lists of the results of all students
    print("Part 2")
    #  Then prints the list using a for loop and with the structure asked
    for i in range(len(r)):
        print(r[i][0] + " - " + str(r[i][1]) + ", " + str(r[i][2]) + ", " + str(r[i][3]))


def part_3(w):  # Function that creates and writes the results in a text file
    #  Then with a for loop the results are written on it
    with open('file.txt', 'w') as f:
        for i in range(len(w)):
            f.write(w[i][0] + " - " + str(w[i][1]) + ", " + str(w[i][2]) + ", " + str(w[i][3]))
            f.write("\n")


def part_4(dic):  # Function that receives the dictionary and prints it with the structure asked
    print("Part 4")
    for i, j in dic.items():
        print(i + " : " + j[0] + " - " + str(j[1]) + ", " + str(j[2]) + ", " + str(j[3]))


def create_lists(pass_cred, defer_cred, fail_cred, outcome):  # Function that creates the list with the results on it
    l = []
    l.extend([outcome, pass_cred, defer_cred, fail_cred])
    return l


def more_data():  # Function that asks the user if they want to include more sets of data, returns a Boolean
    while True:
        print("Would you like to enter another set of data?")
        choice = input("Enter 'y' for yes or 'q' to quit and view reviews: ")
        if choice == "y":
            return False
        elif choice == "q":
            print()
            return True
        else:
            print("Wrong input")


def get_credits(phrase):  # Function that asks and validates the credits introduced by the user
    valid = [0, 20, 40, 60, 80, 100, 120]
    while True:
        try:
            credit = int(input(phrase))
            if credit not in valid:
                print("Out range")
                credit = get_credits(phrase)
        except:
            print("Only Integers")
        else:
            return credit


def main():  # Main Program

    #  Variables
    results = []
    students = {}
    progress = 0
    trailer = 0
    retriever = 0
    exclude = 0

    while True:
        print()
        student_id = get_student_id()
        pass_c = get_credits("Please enter your credits at pass: ")
        defer_c = get_credits("Please enter your credits at defer: ")
        fail_c = get_credits("Please enter your credits at fail: ")

        while pass_c + defer_c + fail_c != 120:  # If the total of credits isn't 120 keeps on asking for them
            print("Total Incorrect")
            print("")
            pass_c = get_credits("Please enter your credits at pass: ")
            defer_c = get_credits("Please enter your credits at defer: ")
            fail_c = get_credits("Please enter your credits at fail: ")

        if pass_c == 120:  # If the pass credits are 120 the student pass
            progress += 1  # The counter goes up
            print("Progress")
            results.append(create_lists(pass_c, defer_c, fail_c, "Progress"))  # The list is created and appended
            students[student_id] = "Progress", pass_c, defer_c, fail_c  # The values of key and

        elif pass_c == 100:  # If the pass credits are 100 the student progress Module Trailer
            trailer += 1
            print("Progress (module trailer)")
            results.append(create_lists(pass_c, defer_c, fail_c, "Progress (module trailer)"))
            students[student_id] = "Progress (module trailer)", pass_c, defer_c, fail_c

        elif fail_c >= 80:  # If the fail credits are less or equal to 80 the result is Exclude
            exclude += 1
            print("Exclude")
            results.append(create_lists(pass_c, defer_c, fail_c, "Exclude"))
            students[student_id] = "Exclude", pass_c, defer_c, fail_c

        else:  # The rest of the inputs totals will be module retriever
            retriever += 1
            print("Do not progress - module retriever")
            results.append(create_lists(pass_c, pass_c, defer_c, "Module retriever"))
            students[student_id] = "Module retriever", pass_c, defer_c, fail_c

        print()

        if more_data():  # The user is asked if they want to continue or not
            break

    #  All the functions are called after the program is done
    histogram(progress, trailer, retriever, exclude)
    part_2(results)
    print()
    part_3(results)
    part_4(students)




main()
