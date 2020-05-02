import csv
print("<-----Login-System----->")

def sign_up():
    print("<---fill_up_your_data--->")

    usr_name = input("Enter Your Name ---> ")
    usr_email = input("Enter Your Email ---> ")
    usr_username = input("Create Your username ---> ")
    usr_password = input("Create Your Password---> ")
    usr_password_confirm = input("Confirm Your Password---> ")

    if usr_password != usr_password_confirm:
        sign_up()
    else:
        usr_data = [usr_name,usr_email,usr_username,usr_password]

    with open("usr_data.csv","a") as data_file:
        fwriter = csv.writer(data_file)
        fwriter.writerow(usr_data)
        print("Your account created successfully")

def log_in():
    data = []
    usr_username = input("Enter Your username ---> ")
    usr_password = input("Enter Your Password---> ")

    with open("usr_data.csv","r") as data_file:
        reader = csv.reader(data_file)
        for row in reader:
            if usr_username and usr_password in row:
                data = row
                print("wrlcome back, ",data[0])

def checker():
    print()
    print("(1) Sign Up  or (2) Log in")
    usr_input = int(input("------>  "))
    if usr_input == 1: 
        sign_up()
    else:
         log_in()

checker()
