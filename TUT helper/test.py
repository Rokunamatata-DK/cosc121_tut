import datetime
import time

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


class sessions:
    def __init__(self, start):
        self.start = start
        self.stop= ""
        self.breaks=[]
        self.breaks_mark=None
        self.hours=0
        self.payment=0
        self.paid= False
        self.break_time = 0

    def end_time(self,end):
        self.stop=end
        mins = (self.start-self.stop).seconds/60
        self.hours = round(mins/60,1) - self.break_time
        self.payment = 35 * hours

    def break_start(self,start):
        self.breaks_mark=start
        
    def break_stop(self,end):
       #if break has started
        if  self.breaks_mark !=None:
             #log break
            breaks.append((self.break_start,end))
            mins = (self.breaks_mark-end).seconds/60
            self.break_time += round(mins/60,1)
            self.breaks_mark=None
        else:
            print("break haven't start")
            pass

        



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
        elif choice == '2':
            pass
        elif choice in ['q','quit']:
            print("\nThanks for playing. Bye.")
        else:
            print("\nI didn't understand that choice.\n")
        



x = datetime.datetime.now()
print(x.strftime("%x %X"))


y = datetime.datetime(2021, 1, 26, 0,00,00 )
print(y.strftime("%x %X"))


gap =x-y
hours= gap.seconds/60/60
money = hours * 35

print("gap is",gap.seconds/60/60)
print(money)

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


# make a log of tutor session
def make_log():

time = enter_time("Enter start time")

def make_datetime(time,year=1999,month=1,day=1):
    return datetime.datetime(year, month, day, time[0], time[1], time[2])

start = make_datetime(time)
end = make_datetime(enter_time("Enter end time"))
print (end - start)

