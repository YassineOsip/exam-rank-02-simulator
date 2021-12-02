#!/usr/bin/python3

import sqlite3
import logging
import uuid
import hashlib
import termcolor
import pyfiglet
import getpass
import sys

logging.basicConfig(filename="errors.log", filemode="w", level=logging.DEBUG)

print_red = lambda x: termcolor.cprint(x, "red")
print_green = lambda x: termcolor.cprint(x, "green")
print_blue = lambda x: termcolor.cprint(x, "blue")
print_yellow = lambda x: termcolor.cprint(x, "yellow")
colored = lambda x, color: termcolor.colored(x, color)

fig = pyfiglet.Figlet(font="standard")

try:
    conn = sqlite3.connect("ErsDb.db")
except Exception as ex:
    logging.error("can't connect to the database, got this message: %s" % ex)

def help():
    if len(sys.argv) >= 2:
        if sys.argv[1] == "--help":
            print("Help docs")
            sys.exit(0)
        else:
            print("Do you mean: --help")
            sys.exit(0)

def hashPassword(password):
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ":" + salt

def selectByLogin(login):
    try:
        cursor = conn.execute("SELECT LOGIN, PASSWORD FROM USER WHERE LOGIN = '%s'" % login)
        user = cursor.fetchone()
        if user == None:
            return False
        return user
    except Exception as ex:
        logging.error("selectionByLogin failed,got this message : %s" % ex)

def register(login, password):
    try:
        if selectByLogin(login) == False:
            conn.execute("INSERT INTO USER (LOGIN, PASSWORD)\
                            VALUES ('%s', '%s')" % (login, hashPassword(password)))
            conn.commit()
            return True
        else:
            return False
    except Exception as ex:
        logging.error("registration failed,got this message : %s" % ex)

def login(login, password):
    user = selectByLogin(login)
    if user == False:
        return False
    hpassword, salt = user[1].split(":")
    return hpassword == hashlib.sha256(salt.encode() + password.encode()).hexdigest()

def registerCommand():
    login = input(colored("Login: ", "yellow"))
    refill_pass = True
    while refill_pass:
        password = getpass.getpass(colored("Password: ", "yellow"))
        rpassword = getpass.getpass(prompt=colored("Confirm password: ", "yellow"))
        if password == rpassword:
            refill_pass = False
        else:
            print_red("Passwords does not match!")
        if not refill_pass and register(login, password):
            print_green("Congratulation you are registered successfully")
        else:
            if refill_pass == False:
                print_red("User alredy exist!")

def loginCommand():
    global exam_session
    global user
    user_login = input(colored("Login: ", "yellow"))
    user_password = getpass.getpass(colored("Password: ", "yellow"))
    if login(user_login, user_password):
        print_green("logged successfully")
        exam_session = True
        user = selectByLogin(user_login)
        return True
    else:
        print_red("Entered login or password Incorrect!")
        return False

def examshellCommand():
    pass

def timeCommand():
    #print(time.strftime('%H:%M:%S', time.gmtime(time.time() - start)))
    pass

def cloneCommand():
    pass

def grademeCommand():
    pass

def finishCommand():
    pass

def helpCommand():
    pass

def examShell(prompt=colored("==> ", "blue"), exam_title="Exam Rank 02"):
    help()
    run = True
    global exam_session
    global user
    exam_session = False
    user = "Anonymous"
    commands = ["register", "login", "me", "examshell", "time", "clone", "grademe", "finish", "help"]
    print_yellow(fig.renderText("%s" % exam_title))
    while run:
        try:
            command = input(prompt)
            if command in commands:
                if command == "register":
                    registerCommand()
                if command == "login":
                    loginCommand()
                if command == "finish":
                    run = False
                    exam_session = False
                    sys.exit(0)
                if command == "me":
                    if exam_session == True:
                        print_yellow(user[0])
                    else:
                        print_yellow(user)
            else:
                print_red("Command not found please use: ./main --help")
        except (KeyboardInterrupt, EOFError):
            print()
            sys.exit(0)


if __name__ == "__main__":
    examShell()
