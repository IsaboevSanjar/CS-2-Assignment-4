import pandas as pd
import re

# users
panda_user = pd.read_csv('Users.csv')
id = panda_user['ID']
psw = panda_user['PSW']
user_id = {}
for i in range(len(id)):
    user_id[id[i]] = psw[i]
# student-info
panda_info = pd.read_csv("Student_info.csv")
info_id = panda_info["ID"]
info_name = panda_info['Name']
info_surname = panda_info['Surname']
info_age = panda_info['age']
payment_status = panda_info['payment_status']
student_info = {}
for i in range(len(info_id)):
    student_info[info_id[i]] = [info_name[i], info_surname[i], info_age[i], payment_status[i]]
# student-grades
panda_grades = pd.read_csv("Students_grade.csv")
gr_id = panda_grades['ID']
gr_math = panda_grades['Math']
gr_programming = panda_grades['Programming']
gr_database = panda_grades['DataBase']
gr_english = panda_grades['English']
student_grades = {}
for i in range(len(gr_id)):
    student_grades[gr_id[i]] = [gr_math[i], gr_programming[i], gr_database[i], gr_english[i]]
counter = 5


def sign_up():
    info_df = pd.read_csv("Student_info.csv")
    user_df = pd.read_csv("Users.csv")
    last_student = 0
    for index, row in info_df.iterrows():
        last_student = row["ID"]
    last_one = int(re.search(r'\d+', last_student).group()) + 1
    print("You are a student!")
    password = input("Password: ")

    name = input("Name:   ")
    surname = input("Surname:   ")
    age = input("Age:   ")

    print("Successfully singed up!")

    new_user = pd.DataFrame(
        {'ID': [f"st00{last_one}"], 'PSW': [password]}
    )
    user_added_df = user_df.append(new_user, ignore_index=True)
    user_added_df.to_csv("Users.csv", index=False)

    info_user = pd.DataFrame(
        {'ID': [f"st00{last_one}"], 'Name': [name], 'Surname': [surname], 'age': [age], 'payment_status': ["Unpaid"]}
    )
    info_added_df = info_df.append(info_user, ignore_index=True)
    info_added_df.to_csv("Student_info.csv", index=False)


choosing = int(input("Enter 1.Log in or 2.Sign Up   "))


# Changing student grade
def change_grade():
    print("If you want change change student's grade please enter students data and subject")
    grades_df = pd.read_csv("Students_grade.csv")
    students_exist = False
    check = True
    while check:
        ID = input("ID:   ")
        subject = input("Subject:   ")
        grade = input("New grade:   ")
        for index, row in grades_df.iterrows():
            if row["ID"] == ID:
                students_exist = True
                break
        if students_exist:
            grades_df.loc[grades_df['ID'] == ID, subject] = grade
            check = False
        else:
            print("Invalid student ID!!!")
    grades_df.to_csv("Students_grade.csv", index=False)
    print("Grade successfully changed")


# deletes a student from the csv
def delete_student_record():
    # Asking to input student's data
    student_info_df = pd.read_csv('Student_info.csv')
    grades_df = pd.read_csv("Students_grade.csv")
    users_df = pd.read_csv("Users.csv")
    check = True
    while check:
        print("To delete student's record inter student info")
        name = input("Name:   ")
        surname = input("Surname:   ")
        student_id = 0
        for index, row in student_info_df.iterrows():
            if row["Name"] == name and row["Surname"] == surname:
                student_id = row['ID']
                student_info_df = student_info_df.drop(
                    student_info_df.loc[
                        (student_info_df['Name'] == name) & (student_info_df['Surname'] == surname)].index)
        for index, row in grades_df.iterrows():
            if row['ID'] == student_id:
                grades_df = grades_df.drop(
                    grades_df.loc[
                        (grades_df['ID'] == student_id)
                    ].index
                )
        for index, row in users_df.iterrows():
            if row['ID'] == student_id:
                users_df = users_df.drop(
                    users_df.loc[
                        (users_df["ID"] == student_id)
                    ].index
                )
            check = False
            break
        if check:
            print("Student does not exist")
    student_info_df.to_csv('Student_info.csv', index=False)
    grades_df.to_csv("Students_grade.csv", index=False)
    users_df.to_csv("Users.csv", index=False)
    print('Student deleted Successfully')


def change_info_in_2files():
    print("If you want to change student's grade and payment status fill out the inputs:")
    grades_df = pd.read_csv("Students_grade.csv")
    payment_df = pd.read_csv("Student_info.csv")
    student_exist = False
    check = True
    while check:
        id = input("Student id:   ")
        subject = input("Subject:   ")
        grade = input("New grade:   ")
        payment_stat = (input("1.Paid 2.Unpaid  "))

        if payment_stat == "1":
            payment_stat = "Paid"
        else:
            payment_stat = "Unpaid"

        for index, row in grades_df.iterrows():
            if row["ID"] == id:
                student_exist = True
                break
        if student_exist:
            grades_df.loc[grades_df['ID'] == id, subject] = grade
            payment_df.loc[payment_df['ID'] == id, "payment_status"] = payment_stat
            check = False
        else:
            print("Invalid student ID!!!")

    grades_df.to_csv("Students_grade.csv", index=False)
    payment_df.to_csv("Student_info.csv", index=False)
    print("Grade and Payment status successfully changed")


def failed_students():
    print("Failed Students")
    failed_list = []
    failed_students = []
    for i in student_grades.keys():
        if sum(student_grades[i]) / 4 <= 60:
            failed_list.append(i)
    info = pd.read_csv("Student_info.csv")
    for index, row in info.iterrows():
        for id in failed_list:
            if row["ID"] == id:
                failed_students.append({row['ID'], row['Name'], row['Surname']})
                break
    for fail in failed_students:
        print(fail)


def high_graded_students():
    print("High Graded Students")
    high_list = []
    high_students = []
    for i in student_grades.keys():
        if sum(student_grades[i]) / 4 >= 86:
            high_list.append(i)
    info = pd.read_csv("Student_info.csv")
    for index, row in info.iterrows():
        for id in high_list:
            if row["ID"] == id:
                high_students.append({row['ID'], row['Name'], row['Surname']})
                break
    for fail in high_students:
        print(fail)


def login_admin():
    print("You are an admin")
    print("1. Delete students' records")
    print("2. Change grades")
    # double
    print("3. Change info in 2 csv files (student_info, student_grades")
    print("4. Find failed students")
    print("5. Find high graded students")
    choose = int(input("Enter which task do you want to do:   "))
    if choose == 1:
        delete_student_record()
    elif choose == 2:
        change_grade()
    elif choose == 3:
        change_info_in_2files()
    elif choose == 4:
        failed_students()
    elif choose == 5:
        high_graded_students()


def loginStudent(my_id):
    print("Your records:")
    print(student_info[my_id])


if choosing == 1:
    while counter != 0:
        my_id = input("INPUT YOUR ID:   ")
        my_psw = input("INPUT YOUR PASSWORD:    ")
        loginner = False
        # looping though from csv to check the user is exist
        for i in user_id:
            if i == my_id and user_id[i] == my_psw:
                loginner = True
                if i.__contains__("ad"):
                    login_admin()
                    counter = 0
                    break
                elif i.__contains__("st"):
                    loginStudent(my_id)
                    counter = 0
                    break
        if not loginner:
            print("Wrong password or login!!!")
            counter -= 1
            # giving 5 chance to try to enter username and password
            if counter == 0:
                sign_up1 = (input("Enter 1 to sign up:   "))
                if sign_up1 == "1":
                    sign_up()
                else:
                    print("You did not want to sign up")
                    break
elif choosing == 2:
    sign_up()
else:
    print("You did not choose neither 1 nor 2")
