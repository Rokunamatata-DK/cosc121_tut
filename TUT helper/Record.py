import datetime


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



class Record:
    def __init__(self, start_time, student="default", course="default"):
        self.start_time = start_time
        self.student = student
        self.course = course
        self.total_mins=0
        self.sessions=[]
        self.stop=start_time

    def end_tut(self):
        self.stop=datetime.datetime.now()
    
    def display(self):
        print(self.start_time, " and ", self.stop, "last: ",(self.stop-self.start_time))