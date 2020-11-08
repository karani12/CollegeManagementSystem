import mysql.connector as mysql

db = mysql.connect(host='localhost', user='root', password='', database='collegemanagement')
command_handler = db.cursor(buffered=True)

def teacher_session():
    print('')
    print("login success welcome teacher ")

    while 1:
        print("")
        print("Teacher's menu")
        print("1. mark student register")
        print("2. view regitser")
        print("3. logout")
        user_option = input(str("option: "))
        if user_option == '1':

            print("")
            print("Mark Student register")
            command_handler.execute("SELECT username FROM users WHERE priviledge = 'student'")
            records = command_handler.fetchall()
            date = input(str("Date : DD/MM/YY :"))

            for record in records:

                record = str(record).replace("'", "")
                record = str(record).replace(",", "")
                record = str(record).replace("(", "")
                record = str(record).replace(")", "")
                #    present|absent|late
                status = input(str("status for" + str(record) + "P/A/L: "))
                query_vals = (str(record), date, status)
                command_handler.execute("INSERT INTO attendance (username,date,status) VALUES(%s,%s,%s)", query_vals)
                db.commit()
                print(record + "marked as" +status)

        elif user_option == '2':
            print("")
            print("viewing register")
            command_handler.execute("SELECT username, date, status FROM attendance")
            records = command_handler.fetchall()
            print('Displaying all register')
            for record in records:
                print(record)

        elif user_option == "3":
            break

        else:
            print("no valid option was selected")





def admin_session():
    print("login success Welcome admin")

    while 1:
        print("")
        print("Admin menu")
        print("1. Register new student")
        print("2. Register new teacher")
        print("3. Delete existing student")
        print("4. Delete existing teacher")
        print("5. Logout")

        user_option = input(str("option :"))

        if user_option == '1':
                print("")
                print("Register new student")
                username = input(str("Student username: "))
                password = input(str("student password"))

                query_vals = (username, password)

                command_handler.execute("INSERT INTO users (username,password,priviledge) VALUES (%s,%s,'student')",
                                        query_vals)
                db.commit()
                print(username + " has been registered as student")
        elif user_option == '2':

                print("")
                print("Register new teacher")
                username = input(str("Student username: "))
                password = input(str("student teacher"))

                query_vals = (username, password)

                command_handler.execute("INSERT INTO users (username,password,priviledge) VALUES (%s,%s,'teacher')",
                                        query_vals)
                db.commit()
                print(username + " has been registered as teacher")
        elif user_option == '3':

            print("")
            print("Delete Existing Student Account")

            username = input(str("student username : "))
            query_vals = (username,'student')
            command_handler.execute("DELETE FROM users WHERE username = %s AND priviledge = %s",query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("user not found")
            else:
                print(username + "has been deleted")
        elif user_option == '4':


            print("")
            print("Delete Existing teachers Account")

            username = input(str("teacher username : "))
            query_vals = (username, 'teacher')
            command_handler.execute("DELETE FROM users WHERE username = %s AND priviledge = %s", query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("user not found")
            else:
                print(username + "has been deleted")
        elif user_option =='5':
            break
        else:
            "no valid option selected"

def auth_teacher():
    print("")
    print("Teacher/'s login")
    print("")
    username = input(str("username: "))
    password = input(str("password: "))
    query_vals = (username, password)
    command_handler.execute("SELECT * FROM users WHERE username = %s AND password = %s AND priviledge = 'teacher'",query_vals)
    db.commit()
    if  command_handler.rowcount <= 0:
        print("invalid input")
    else:
        teacher_session()

def auth_admin():
    print("")
    print("admin login")
    username = input(str("username: "))
    password = input(str("Password: "))

    if username == "admin":
        if password == "password":
            admin_session()
        else:
            print("incorrect password here")
    else:
        print('login details are unrecognised')


def main():
    while 1:
        print('Welcome to the college portal')
        print('')
        print('1. Login  as student')
        print('2. Login  as teacher')
        print('3. Login  as admin')

        user_option = input(str("option: "))

        if user_option == '1':
            print('student')
        elif user_option == '2':
            auth_teacher()
        elif user_option == '3':
            auth_admin()
        else:
            print("invalid option")


main()
