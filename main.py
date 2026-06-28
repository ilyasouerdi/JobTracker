from services import *


name = input("Name: ")
email = input("Email: ")
password = input("Pasword: ")

new_user = create_user(name,email,password) 