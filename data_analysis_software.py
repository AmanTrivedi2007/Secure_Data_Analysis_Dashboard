import pandas as pd
import numpy as np
import random
import sys
import datetime
import time
import hashlib
import os
import matplotlib.pyplot as plt

print("Welcome to the Data Analysis Basic Software!")
print("Please enter the required information to log in")
print("This is the login input validator module.")
print("Can you please enter the requested information to login to the system?")

# to generate a random 6-digit OTP
def generate_opt():
    """Generate a random 6-digit OTP."""
    otp = random.randint(100000, 999999)
    return otp

# to generate a random username
def generate_username(input1):
    """Generate a username based on the user's name."""
    letters = [chr(i) for i in range(ord('a'), ord('z')+1)]
    numbers = list(range(0, 10))
    suffix = (
        str(random.choice(numbers)) +         
        random.choice(letters) +              
        random.choice(letters).upper() +      
        str(random.choice(numbers)) +         
        str(random.choice(numbers))           
    )
    no_space_name = input1.replace(" ", "")
    user_name = no_space_name.lower() + suffix
    return user_name

# to generate a random password
def generate_password():
    """Generate a random 4-character password."""
    letters = [chr(i) for i in range(ord('a'), ord('z')+1)]
    numbers = list(range(0, 10))
    password = (
        random.choice(letters).upper() +     
        str(random.choice(numbers)) +        
        random.choice(letters) +              
        str(random.choice(numbers))           
    )
    return password

# admin credentials
admin_name = ['admin1234', 'admin12345', 'admin123456']
admin_password = ['12345', '123456', '1234567']

# Main loop to handle user input and actions
while True:
    print("\nPlease enter the requested information:")
    print("Enter 1 to create a new account")
    print("Enter 2 to login to your account")
    print("Enter 3 to exit the system")
    choice = input("Enter your response: ")
    
    if choice == "1":
        print("------ You have chosen to create a new account ------")
        input1 = input("Please enter your name: ")

        # Validate name
        if input1 == "":
            print("You have entered an empty name. Please try again.")
            continue
        elif len(input1) < 3:
            print("You have entered less than 3 characters. Please try again.")
            continue
        elif len(input1) > 20:
            print("You have entered more than 20 characters. Please try again.")
            continue

        # Ensure username file exists
        if not os.path.exists("userName.txt"):
            with open("userName.txt", "w") as file:
                pass

        # Read existing usernames safely
        with open("userName.txt", "r") as file:
            existing_usernames = {line.strip() for line in file if line.strip()}

        # Generate a unique username
        while True:
            User_name = generate_username(input1)
            if User_name not in existing_usernames:
                break

        input2 = input("Please enter your email: ")
        email_parts = input2.lower()
        input3 = input("Please enter your phone number: ")

        print("-------- Your account has been created successfully --------")

        password = generate_password()

        print(f"Your username is: {User_name}")
        print(f"Your password is: {password}")

        # Save username
        with open("userName.txt", "a") as file:
            file.write(User_name + "\n")
        
        # Save hashed password using hashlib + salt
        salt = os.urandom(16)
        hashed_password = hashlib.sha256(salt + password.encode('utf-8')).hexdigest()
        stored_value = salt.hex() + '$' + hashed_password + '\n'
        with open("hashed_passwords.txt", "a") as file:
            file.write(stored_value)

        # Logging
        with open("login_input_username_passward.txt", "a") as file:
            log = f"Your generated username is {User_name} and your password is {password} and you have logged in with the account {email_parts}\n"
            file.write(log)
        with open("login_input_username.txt", "a") as file:
            loge = f"Your generated username is {User_name}\n"
            file.write(loge)

    elif choice == "2":
        print("------ You have chosen to login to your account ------")
        input4 = input("Please enter your username: ")

        # Read usernames safely
        if os.path.exists("userName.txt"):
            with open("userName.txt", "r") as file:
                usernames = [line.strip() for line in file if line.strip()]
        else:
            usernames = []

        if input4 in usernames:
            print("Username is correct")
            input5 = input("Please enter your password: ")

            # Read hashed passwords safely
            if os.path.exists("hashed_passwords.txt"):
                with open("hashed_passwords.txt", "r") as file:
                    hashed_passwords = [line.strip() for line in file if line.strip()]
            else:
                hashed_passwords = []

            try:
                user_index = usernames.index(input4)

                # Check for missing password entry
                if user_index >= len(hashed_passwords):
                    print("Password entry missing for this username. Please contact admin.")
                    continue

                stored_value = hashed_passwords[user_index].strip()

                # Ensure correct format before splitting
                if '$' not in stored_value:
                    print("Stored password format error. Please contact admin.")
                    continue

                salt_hex, stored_hash = stored_value.split('$')
                salt = bytes.fromhex(salt_hex)

                input_hash = hashlib.sha256(salt + input5.encode('utf-8')).hexdigest()
                if input_hash == stored_hash:
                    print("Password is correct")
                    otp = str(generate_opt())
                    start_time = time.time()

                    print("Your OTP is:", otp)
                    print("You have 60 seconds to enter the OTP")

                    input6 = input("Please enter your generated OTP: ")
                    current_time = time.time()
                    time_elapsed = current_time - start_time

                    if time_elapsed > 60:
                        print("Time out, please try again")
                        continue
                    elif input6 == otp:
                        print("OTP is correct. You have successfully logged in.")
                        print("please tell em what si your file name which you want to do analysis on")

                        while True:    
                            print("please make sure that the file is csv file ")
                            print("please make sure the file is in the fromate of \n column1 ,column2,column3,column4,comlumn5")
                            print("also make suer that the file should include the header")
                            print("please make sure that the file should contain the data fro 4 quaters for each year")

                            user_input_to_continue = input("do you wan to continue? (yes/no): ")

                            if user_input_to_continue.lower() == 'yes':
                                file_name = input("Enter the file name (with .csv extension): ")
                                try:
                                    data = pd.read_csv(file_name)
                                    print("Data loaded successfully.")
                                    array = data.to_numpy()
                                except FileNotFoundError:
                                    print("File not found. Please check the file name and try again.")
                                    continue
                                except pd.errors.EmptyDataError:
                                    print("The file is empty. Please provide a valid file.")
                                    continue
                                except Exception as e:
                                    print(f"An error occurred: {e}")
                                    continue
                                
                                print("You can now perform data analysis on the loaded data.")
                                print("you can perfrom the following operations on the data:")
                                print("1. Please enter 1 to view the whole data")
                                print("2.please enter 2 to view the total revenue genrated each year")
                                print("3.please enter 3 if you want to view average revenue genrated each year")
                                print("4.please enter 4 if you want to see the graph average revenue genrrated each \n year VS year in the from of bar garph")
                                print("5.please enter 5 if you want to see the graph of revenue genrated each \n year VS year in the from of line graph")
                                print("6.please enter 6 to exit the data analysis software")

                                VIEW_INPUT = input("please enter your choice: ")

                                if VIEW_INPUT == '1':
                                    print("Displaying the whole data:")
                                    print(data)
                                elif VIEW_INPUT == '2':
                                    yearly_revenue = np.sum(array[:,1:],axis=1)
                                    print("Total revenue generated each year:\n", yearly_revenue)
                                elif VIEW_INPUT == '3':
                                    average_revenue = np.mean(array[:,1:],axis=1)
                                    print("Average revenue generated each year:\n", average_revenue)
                                elif VIEW_INPUT == '4':
                                    average_revenue = np.mean(array[:,1:],axis=1)
                                    years = array[:,0]
                                    plt.bar(years, average_revenue)
                                    plt.xlabel('Year')
                                    plt.ylabel('Average Revenue')
                                    plt.title('Average Revenue Generated Each Year')
                                    plt.show()
                                elif VIEW_INPUT == '5':
                                    yearly_revenue = np.sum(array[:,1:],axis=1)
                                    years = array[:,0]
                                    plt.plot(years,yearly_revenue)
                                    plt.xlabel('Year')
                                    plt.ylabel('Total Revenue')
                                    plt.title('Total Revenue Generated Each Year')
                                    plt.show()
                                elif VIEW_INPUT == '6':
                                    print("Exiting the data analysis software. Thank you!")
                                    sys.exit()
                                else:
                                    print("Invalid input. Please try again.")
                                    continue                                        
                            elif user_input_to_continue.lower() == 'no':
                                print("Exiting the data analysis software. Thank you!")
                                sys.exit()
                            else:
                                print("Invalid input. Please enter 'yes' or 'no'.")
                                continue
                    else:
                        print("Invalid OTP, please try again")
                        continue
                else:
                    print("You have entered wrong password. Please restart.")
                    continue
            except IndexError:
                print("Error: Password data not found. Please contact admin.")
                continue
        else:
            print("You have entered wrong username.")
            continue

    elif choice =="3":
        print("------ You have chosen to exit the system ------")
        print("Thank you for using the system")
        break
    else:
        print("You have entered wrong input. Please try again.")
        continue

    print("----------------------------------------------")
