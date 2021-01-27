import datetime



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