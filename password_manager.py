
pwd = input("What is the master password? ")

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passwd = data.split("|")
            print(user, passwd)



def add():
    name = input("username: ")
    pwd = input("password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + pwd + "\n")

while True:
    mode = input("Do you want to view or add or quit? view/add/quit ").lower()
    if mode == "q":
        break
    if mode == "view" or mode == "v":
        print("view")
        view()
    if mode == "a" or mode == "add":
        print("add")
        add()

else:
    print("invalid option")