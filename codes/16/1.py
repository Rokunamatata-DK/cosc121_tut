import datetime


def max_temp(path ):
    """ad"""
    doc = open(path,'r')
    data = doc.readlines()
    new_data = []
    doc.close()
    
    for item in data:
        list1 = item.split()
        list1[0] = int(list1[0])
        list1[-1] = float(list1[-1])
        new_data.append(list1)
    
    for month in range(1,12+1,1):
        max_t = []
        for line in new_data:
            if month == line[0]:
                max_t.append(line[-1])
        if len(max_t) == 0:
            print("No data in", month)
        else:
            print(max(max_t))
        
             
       
    


def max_temp2(path ):
    """ad"""
    file = open(path,'r')
    data = []
    list_t = []
    for line in file:
        print(line)
        list1 = line.split()
        print(list1)
        list1[0] = int(list1[0])
      
        list1[-1] = float(list1[-1])
        data.append(list1)
    print(data)    
    for i in range(1,13,1):
        t1 = []
        for j in range(0,len(data)):
            # print(data[j]) every line in data
            if data[j][0] == i:
                t = data[j][-1]
                t1.append(t)
        list_t.append(t1)
    print(list_t)
    month = 1
    for item in list_t:
        if not item:
            print("month: ", month ,"empty list")
        else:
            print("month: ", month ,max(item))
        month += 1
       
    
def write_result(input_path,output_path):
    """take data from input file and reformat into output file"""
    input_file=open(input_path,'r')
    output_file = open(output_path,'w')
    #read all data from input
    data = input_file.readlines()
    input_file.close()
    
    #set init result
    result = []
    #for every line in data
    for item in data:
        #convert str into numberic
        list1 = item.split()
        list1[0] = int(list1[0])
        list1[-1] = float(list1[-1])
        #add into result
        result.append(list1)
    
    final_result=[]
    #classfiy into 12 month
    for month in range(1,12+1,1):
        #temp var to store tmepture
        max_t = []
        for line in result:
            if month == line[0]:
                max_t.append(line[-1])
        if len(max_t) == 0:
            final_result.append((month,"NA"))
            # print("No data in", month)
        else:
            # print(max(max_t))
            final_result.append((month,max(max_t)))

    #conver list to text
    output_text="Mon:\tTemp\n"
    for (month,temp) in final_result:
        # print(month,temp)
        x = datetime.datetime(2018, month, 1)
        output_text+= x.strftime("%b")+":\t"+temp.__str__()+"C\n"

    #write into file
    # print(final_result)
    # print(output_text)
    output_file.write(output_text)
    
    output_file.close()



# max_temp2('Z:\Tutor 2021\cosc212\code\mean_temperature.txt')


# write_result('Z:\Tutor 2021\cosc212\code\mean_temperature.txt'\
#     ,'Z:\Tutor 2021\cosc212\code\mean_temperature_output.txt')

