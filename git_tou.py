users = ('sarthak', 'shivam', 'sachin', 'sana', 'ankush', 'srvm')
keys = ('sarthak123', 'shivam123', 'sachin123', 'sana123', 'ankush123', 'srvm123')

def login():
    user = input("Enter your username: ")
    if user in users:
        index = users.index(user)  
        password = input("Enter your password: ")
        if password == keys[index]:  
            print("Login successful!🔥 ")
        else:
            print("Incorrect password.")
    else:
        print("Username not found. 💔💔")

login()