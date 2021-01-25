def print_summary(filename):
    """ASD"""
    file = open(filename)
    data = file.readlines()
    file.close()
    
    #for each(every) line in data
    for line in data:
        #split line in to a list of 2 items
        display= line.split(": ")
        #split secound item in display by ,
        nums=display[1].split(',')
        #set init(create new empty) sum
        sum=0
        #for each num in nums
        for num in nums:
            #add up a sum
            sum += int(num)
        #print display first item(the date) and calcute the avg by sum/number of temps
        
        print(display[0]+": {:1f}".format(sum/len(nums)))
    
print_summary("Z:\\Tutor 2021\\CS121\\codes\\revision\\asd.txt")