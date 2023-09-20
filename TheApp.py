import time as t
import os
import subprocess
from colorama import Fore
import random



ver = "Beta 1.1"


current_dir = os.path.dirname(os.path.realpath(__file__))
vbs_file = "UnknownCMD.vbs"
folder_name = "Err MSGs"
full_path_vbs = os.path.join(current_dir, folder_name, vbs_file)



#Custom Path Files Algorithm




subfolder_name = "Custom paths"

subfolder_path = os.path.join(current_dir, subfolder_name)
file_names = ["1", "2", "3", "4", "5", "6"]



Path1_txt_name = "Path 1.txt"
Path1_txt_file_path = os.path.join(current_dir, subfolder_name, Path1_txt_name)

Path2_txt_name = "Path 2.txt"
Path2_txt_file_path = os.path.join(current_dir, subfolder_name, Path2_txt_name)

Path3_txt_name = "Path 3.txt"
Path3_txt_file_path = os.path.join(current_dir, subfolder_name, Path3_txt_name)


Path4_txt_name = "Path 4.txt"
Path4_txt_file_path = os.path.join(current_dir, subfolder_name, Path4_txt_name)

Path5_txt_name = "Path 5.txt"
Path5_txt_file_path = os.path.join(current_dir, subfolder_name, Path5_txt_name)

Path6_txt_name = "Path 6.txt"
Path6_txt_file_path = os.path.join(current_dir, subfolder_name, Path6_txt_name)




with open(Path1_txt_file_path, 'r') as file:
        lines1 = file.readlines()
        program1_path = lines1[2].strip()


with open(Path2_txt_file_path, 'r') as file:
        lines2 = file.readlines()
        program2_path = lines2[2].strip()


with open(Path3_txt_file_path, 'r') as file:
        lines3 = file.readlines()
        program3_path = lines3[2].strip()




with open(Path4_txt_file_path, 'r') as file:
        lines4 = file.readlines()
        program4_path = lines4[2].strip()


with open(Path5_txt_file_path, 'r') as file:
        lines5 = file.readlines()
        program5_path = lines5[2].strip()


with open(Path6_txt_file_path, 'r') as file:
        lines6 = file.readlines()
        program6_path = lines6[2].strip()






#Def Codes

def shutdown():
    print("Shutting Down Now...")
    t.sleep(0.3)
    os.system("shutdown /s /t 0")


def restart():
    print("Restarting..")
    t.sleep(0.3)
    os.system("shutdown /r /t 0")


def info():
    print("Commands:\n",
          "\n1.off: Shutdowns Your PC\n",

          "2.re: Restarts Your PC\n",

          "3.app: choose a custom app to run(You Must Config one of This Program's Files).\n",
          
          "4.cstm: opens the folder for customizing the app you want to quick-open.\n",

          "5.app 1: open the custom path you typed in the 'Path 1.txt' file.(There are 6 'app' commands, 'app 1', 'app 2', 'app 3', etc.. they all work the same way.)\n",

          "6.info: you literally know what 'info' means.\n",

          "7.rndm: random Path of the 6 custom app paths you configured.\n",

          "\nMore Coming Soon...\n\n")





#Main Loop

while True:

    command = input("\nEnter a command *Case Sensitive* (or 'exit' to quit)\n\nfor help, enter 'help': ")
    if command == "exit":
        break

    elif command == "help":
        info()

    elif command == "off":
        shutdown()


    elif command == "re":
        restart()

    elif command == "calc":
        subprocess.Popen("C:\Windows\System32\calc.exe")



    #custom App Paths(Line 97 - 167)
    elif command == "cstm":
        os.system(f'explorer "{subfolder_path}"')


    #hidden command
    elif command == '& C:/Users/r33dh/AppData/Local/Programs/Python/Python311/python.exe "d:/Raad Desk/unity/vs code/Python/Commands to make life easier(.py)/TheApp.py"':
        break
    

    elif command == "app 1":
       
        if program1_path == '"Path"':
            print("Custom Path Not Changed, Opening Folder To Change it...")
            t.sleep(2)
            os.system(f'explorer "{subfolder_path}"')
        else:
            os.system(program1_path)

    

    elif command == "app 2":
        if program2_path == '"Path"':
            print("Custom Path Not Changed, Opening Folder To Change it...")
            t.sleep(2)
            os.system(f'explorer "{subfolder_path}"')
        else:
            os.system(program2_path)


    elif command == "app 3":
        if program3_path == '"Path"':
            print("Custom Path Not Changed, Opening Folder To Change it...")
            t.sleep(2)
            os.system(f'explorer "{subfolder_path}"')
        else:
            os.system(program3_path)


    elif command == "app 4":
       
        if program4_path == '"Path"':
            print("Custom Path Not Changed, Opening Folder To Change it...")
            t.sleep(2)
            os.system(f'explorer "{subfolder_path}"')
        else:
            os.system(program4_path)

    

    elif command == "app 5":
        if program5_path == '"Path"':
            print("Custom Path Not Changed, Opening Folder To Change it...")
            t.sleep(2)
            os.system(f'explorer "{subfolder_path}"')
        else:
            os.system(program5_path)


    elif command == "app 6":
        if program6_path == '"Path"':
            print("Custom Path Not Changed, Opening Folder To Change it...")
            t.sleep(2)
            os.system(f'explorer "{subfolder_path}"')
        else:
            os.system(program6_path)


    elif command == "rndm":
        selected_file = random.choice(file_names)
        
        if selected_file == "1":
            if program1_path == '"Path"':
                print("Custom Path Not Changed, Opening Folder To Change it...")
                t.sleep(2)
                os.system(f'explorer "{subfolder_path}"')
            else:
                os.system(program1_path)


        elif selected_file == "2":
            if program2_path == '"Path"':
                print("Custom Path Not Changed, Opening Folder To Change it...")
                t.sleep(2)
                os.system(f'explorer "{subfolder_path}"')
            else:
                os.system(program2_path)


        elif selected_file == "3":
            if program3_path == '"Path"':
                print("Custom Path Not Changed, Opening Folder To Change it...")
                t.sleep(2)
                os.system(f'explorer "{subfolder_path}"')
            else:
                os.system(program3_path)


        elif selected_file == "4":
            if program4_path == '"Path"':
                print("Custom Path Not Changed, Opening Folder To Change it...")
                t.sleep(2)
                os.system(f'explorer "{subfolder_path}"')
            else:
                os.system(program4_path)


        elif selected_file == "5":
            if program5_path == '"Path"':
                print("Custom Path Not Changed, Opening Folder To Change it...")
                t.sleep(2)
                os.system(f'explorer "{subfolder_path}"')
            else:
                os.system(program5_path)


        elif selected_file == "6":
            if program6_path == '"Path"':
                print("Custom Path Not Changed, Opening Folder To Change it...")
                t.sleep(2)
                os.system(f'explorer "{subfolder_path}"')
            else:
                os.system(program6_path)
        

        print("selected file is: Path ", selected_file)



    elif command == "app":
            if program1_path == '"Path"' and program2_path == '"Path"' and program3_path == '"Path"' and program4_path == '"Path"' and program5_path == '"Path"' and program6_path == '"Path"':
                print("No Custom Paths Changed, Opening Folder To Change them...")
                t.sleep(2)
                os.system(f'explorer "{subfolder_path}"')


            else:
                app_selection = input("What Path Shortcut Do You Want to open?(app 1, app 2, app 3, etc...): ")
                if app_selection == "app 1":
                    if program1_path == '"Path"':
                        print("Path Not Changed.")
                        t.sleep(1)
                        os.system(f'explorer "{subfolder_path}"')
                    else:    
                        os.system(program1_path)

                elif app_selection == "app 2":
                    if program2_path == '"Path"':
                        print("Path Not Changed.")
                        t.sleep(1)
                        os.system(f'explorer "{subfolder_path}"')
                    else:    
                        os.system(program2_path)


                elif app_selection == "app 3":
                    if program3_path == '"Path"':
                        print("Path Not Changed.")
                        t.sleep(1)
                        os.system(f'explorer "{subfolder_path}"')
                    else:    
                        os.system(program3_path)
                
                elif app_selection == "app 4":
                    if program4_path == '"Path"':
                        print("Path Not Changed.")
                        t.sleep(1)
                        os.system(f'explorer "{subfolder_path}"')
                    else:    
                        os.system(program4_path)

                elif app_selection == "app 5":
                    if program5_path == '"Path"':
                        print("Path Not Changed.")
                        t.sleep(1)
                        os.system(f'explorer "{subfolder_path}"')
                    else:    
                        os.system(program5_path)
                
                elif app_selection == "app 6":
                    if program6_path == '"Path"':
                        print("Path Not Changed.")
                        t.sleep(1)
                        os.system(f'explorer "{subfolder_path}"')
                    else:    
                        os.system(program6_path)

                
                else:
                    print(Fore.RED, "Unknown Selection.\n", Fore.WHITE)
                    t.sleep(2)
                    pass


    
    #other Commands
    
    elif command == "info":
        print("\nINFO:\n\n\nV ", ver, "\n\n\n'Commands To Make Life Easier', A program By Raad.\n")

    elif command == "Die":
        break

    

    #---------------------------------------------------------------------------


    else:
        print(Fore.RED + "\nUnknown Command.\n" + Fore.WHITE)
        subprocess.run(['cscript', full_path_vbs], shell=True)

