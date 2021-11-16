# Main menu

import functions

while True:
          
    functions.main_menu()
          
    choice = input("Choose an option: ")
    if choice == "1":
        functions.check_port()
    elif choice == "2":
        functions.check_ip()
    elif choice == "3":
        functions.check_os()
    elif choice == "4":
        quit()





