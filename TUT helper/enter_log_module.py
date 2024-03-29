import datetime

import pickle


class Session:
    def __init__(self, start):
        self.start = start
        self.stop= ""
        self.breaks=[]
        self.breaks_mark=None
        self.hours=0
        self.payment=0
        self.paid= False
        self.break_time = 0

    def __str__(self):
        return "this Session started at: {}, ended at: {}, hours number is: {} \
            \nwith total break time of: {}, payment will be: {}"\
            .format(self.start.strftime("%x %X"), self.stop.strftime("%x %X"), \
                self.hours.__str__(), self.break_time.__str__(), self.payment.__str__())
    
    def to_dict(self):
        dict_session =  {"start":self.start, "stop":self.stop, "breaks":self.breaks,\
             "hours":self.hours, "payment":self.payment, "paid":self.paid,\
                  "break_time": self.break_time }
        return dict_session

    def end_time(self,end):
        self.stop=end
        mins = (self.stop-self.start).seconds/60
        self.hours = round(mins/60,1) - self.break_time
        self.payment = round( 35 * self.hours,1)

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

        



        





# return false when fail, list of time when success
def check_is_time(ls_time):
    """check if the input is valid time data"""
    result = []
    if len(ls_time)==2:
        ls_time.append("00")
    # if len if list is less then 3, fail
    if len(ls_time) != 3:
            print("error: must input 2 or 3 number separated by ':' ")
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
def enter_time(message):
    print("\n[q] Quit.")
    ls_time = False
    # limit time of errer
    error_limiter = 0
    while ls_time == False and error_limiter < 10:
        new = input(message+" as hour:min:sec :")
        # when input q , return false and break
        if new in ["q","quit"]:
            return False
        ls_time = check_is_time(new.split(":"))
        error_limiter +=1
    # pass the check and return data
    return ls_time

#3 item list to datetime with default date
def make_datetime(time,year=1999,month=1,day=1):
    if time == False:
        return False
    else:
        return datetime.datetime(year, month, day, time[0], time[1], time[2])

# make a log of tutor session, return T/F
def make_log(list_sessions):
    
    start = make_datetime(enter_time("1: Enter a start time"))
    end = make_datetime(enter_time("2: Enter end time"))
    # if both return valid
    if start!= False and end != False:
        # init new session class
        new_log= Session(start)
        # end session
        new_log.end_time(end)
        # return value
        list_sessions.append(new_log.to_dict())
        return True
    else:
        print("progress canceled, no data added")
        return False
    # print(new_log.__str__())
  
def load_dicts(dicts_session):
    file = open('logs.pydata', 'rb')
    data = pickle.load(file)
    file.close()
    for dic in data:
        dicts_session.append(dic)





def input_new_log(override = False):
    list_session = []

    #################override switch##############
    if override == False:
        load_dicts(list_session)
    #################override switch##############

    if make_log(list_session) == True:
  
        file_object = open('logs.pydata', 'wb+')
        pickle.dump(list_session, file_object)
        file_object.close()
        print("\nI will store the following log: ")
        print(list_session[-1])

if __name__ == '__main__':
    input_new_log(True)
    