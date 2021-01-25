import os
import pickle




################### FUNCTIONS ##############################################################
# return false when fail, list of time when success
def check_is_time(ls_time):
    """check if the input is valid time data"""
    result = []
    # if len if list is less then 3, fail
    if len(ls_time) != 3:
            print("error: not 3 number")
            return False
    else:
        for t in ls_time:
            t= t.strip()
            #if is not digit, fail
            if t.isdigit() != True:
                print("error: not a number")
                return False
            #if is a digit, convert into a int and added to result
            else:
                result.append(int(t))
        # if hour is not within 0 to 24,fail
        if result[0] not in range(0,24+1,1):
            print("error: hour has to be within 0 to 24")
            return False
        # if min or sec in not within 0 to 60,fail
        elif result[1] not in range(0,60+1,1) or result[2] not in range(0,60+1,1):
            print("error: minute or second has to be within 0 to 60")
            return False
    # all passed, return result data
    return result

# return false when fail, list of time when success
def enter_time(messge):
    print(messge,"\nEnter q or quit to quit")
    ls_time = False
    # limit time of errer
    error_limiter = 0
    while ls_time == False and error_limiter < 10:
        new = input("enter start time as hour:min:sec :")
        # when input q , return false and break
        if new in ["q","quit"]:
            return False
        ls_time = check_is_time(new.split(":"))
        error_limiter +=1
    # pass the check and return data
    return ls_time



#'animals.pydata'
def open_file(filename):
    file = open(filename, 'rb')

    data = pickle.load(file)

    print(data)

    file.close()

    for line in data:
        print(line)

def display_title_bar():
    # Clears the terminal screen, and displays a title bar.
    # os.system('clear')
              
    print("\t***********************************************")
    print("\t***  Hello -- Tutor helper -- Manual logger ***")
    print("\t***********************************************")
    
def get_user_choice():
    # Let users know what they can do.
    print("\n[1] See a list of logs.")
    print("[2] log a new one.")
    print("[3] manage logs")
    print("[q] Quit.")
    
    return input("What would you like to do? ")
    
def show_logs():
    # Shows the names of everyone who is already in the list.
    print("\nHere are the people I know.\n")
    for name in names:
        print(name.title())
        
def get_new_name():
    # Asks the user for a new name, and stores the name if we don't already
    #  know about this person.
    new_name = input("\nPlease tell me this person's name: ")
    if new_name in names:
        print("\n%s is an old friend! Thank you, though." % new_name.title())
    else:
        names.append(new_name)
        print("\nI'm so happy to know %s!\n" % new_name.title())


### MAIN PROGRAM ###
# This program asks the user for some time(date), and stores them.

# Make an empty list to store new animals in.
# sessions = []

# # Create a loop that lets users store new new.
# new_time = ''
# while new_time != 'quit':
#     print("\nPlease tell me a new animal to remember.")
#     new_time = input("Enter 'quit' to quit: ")
#     if new_time != 'quit':
       
#         sessions.append(new_time)

# # Try to save the animals to the file 'animals.pydata'.
# try:
#     file_object = open('animals.pydata', 'wb')
#     pickle.dump(sessions, file_object)
#     file_object.close()
#     print("\nI will remember the following animals: ")
#     for animal in sessions:
#         print(animal)
# except Exception as e:
#     print(e)
#     print("\nI couldn't figure out how to store the animals. Sorry.")


# Set up a loop where users can choose what they'd like to do.
def main():
    times = []

    choice = ''
    display_title_bar()

    while choice not in ['q','quit']:    
        
        choice = get_user_choice()
        
        # Respond to the user's choice.
        display_title_bar()
        if choice == '1':
           pass
        # log new record
        elif choice == '2':
            pass
        elif choice in ['q','quit']:
            print("\nBye human")
        else:
            print("\nI didn't understand that choice.\n")
        
main()