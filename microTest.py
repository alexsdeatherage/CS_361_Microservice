
import time
from tkinter import Y


global returnTexT

####################################################
#
#               Functions
#
####################################################
def quit_Services():
    exit_p = 1
    while exit_p == 1:
        try:
            with open("randomCapital.txt","w") as file: #write quit to prng-service.txt
                file.write("1\n")
                file.write("quit")
                file.close()
                #print("writing to count")
                exit_p = 2
        except:
            print("could not open")
            exit_p = 2
            

    print("exiting")


######################################################
def init_Pipe():
    try:
        with open("randomCapital.txt","w") as file: #write start to prng-service.txt
            file.write("0\n")
            file.write("Waiting")
            file.close()
            #print("writing to wordCount")

    except:
        print("could not open")

            
###################################################
def uiProcess():
    run = True
    while (run):
        user_input = input("Would you like to pull a random capital (Y/N) \n")

        if user_input == "N": #check if theyd like to quit
            prompt = True
            while prompt:
                user_input = input("Would you like to exit (Y/N) \n")
                user_input = user_input.capitalize()
                ######### exit #########################################
                if user_input == "Y": #quit program
                    quit_Services()
                    prompt = False
                    run = False

                #######################################################
                elif user_input == "N":
                    print("ok?")
                    prompt = False

                else:
                    print("Invalid Response")

        elif user_input == "Y":
            # count = input("how many words would you like? \n")
            try:
                execute()
                print("Returned Text: ")
                print(returnText)  
                

            except ValueError:
                print("number not provided")

        else:
            print("Invalid Response")

##########################################################
def execute():
    global returnText
    attempt = 1

    while attempt == 1:
        try:
            with open("randomCapital.txt","w") as file: #write run to prng-service.txt
                file.write("1\n")
                file.write("waiting")
                file.close()
                attempt = 2
                
        except:
            print("fail attempt")
            pass

    time.sleep(0.5) #wait 0.5sec for txt file to be updated

    while attempt == 2:
        try:
            with open("randomCapital.txt") as file: #check wordCount.txt for return
                lines = file.readlines()
                
                file.close()
                if int(lines[0]) == 0:
                    text = lines[1]
                    returnText = text
                    attempt = 3

                    with open("randomCapital.txt",'w') as file: #clears contents of wordCount.txt (prevent slow down)
                        file.write("0\n")
                        file.write('waiting') 
                        file.close()
                else:
                    pass
            
        except:
            print("fail attempt 2")
            pass

        time.sleep(0.5) #wait 0.5sec for txt file to be updated

#######################################################################
#
#
#                   MAIN
#
#
#########################################################################
def main():
    init_Pipe() #initialize communication pipeline
    uiProcess() #start ui 

if __name__ == "__main__":
    main()
