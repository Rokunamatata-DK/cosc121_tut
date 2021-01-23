import datetime

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