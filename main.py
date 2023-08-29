import hashlib
import jwt
import datetime


passhash = hashlib.sha256("whoami".encode()).hexdigest()

def login(password):
    return hashlib.sha256(password.encode()).hexdigest() == passhash 

login_attempt = False

while True:
    password = input("Please enter the password: ")
    if login(password):
        login_attempt = True
        break
    else:
        print("Wrong password. Please enter again.")

if login_attempt:
    print("Login successfull")
    print("Welcome to your password vault")
    with open("data.txt", "r+") as file1:
        while True:
            inpt = input("Enter 1 to read data.\nEnter 2 to add new data:\nEnter 3 to exit the program. \nEnter Here:")

            match inpt:
                case "1":
                    data = file1.read()
                    if len(data) <= 0:
                        print("No stored data. Press 2 to enter data.")
                    else:
                        decoded_data = jwt.decode(data, password, algorithms=['HS256'])
                    print(decoded_data['data'])

                case "2":
                    data = file1.read()
                    if len(data) <= 0:
                        websites = []
                    else:
                        decoded = jwt.decode(data, password, algorithms=["HS256"])
                        websites = decoded['data']

                    data = input("Please enter the website name: ")
                    passwd = input("Please enter the password: ")
                    expiration_date = datetime.datetime.utcnow() + datetime.timedelta(days=340)
                    websites.append({'website': data, 'password': passwd})

                    token_data = {'data': websites}
                    encoded = jwt.encode(token_data, password, algorithm='HS256')
                    file1.seek(0)
                    file1.write(encoded)
                    
                    print("Data added successfully")
                case"3":
                    print("Exiting the program")
                    exit
                case default:
                    print("Invalid choice.Please enter valid choice")
print("THANK YOU FOR USING OUR PASSWORD VAULT")









