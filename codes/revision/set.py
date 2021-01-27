# class Course:
#     """asd"""
#     def __init__(self, code, name, points):   
#         """asd"""
#         self.code = code
#         self.name = name
#         self.points = points

#     def to_dictionary(self):
#         """asd"""
#         result ={'code': self.code, 'name': self.name, 'points': self.points}
#         return result
#     def __str__(self):
#         """asd"""
#         return "{} ({}) {} points".format(self.code, self.name, self.points)


# course = Course('COSC121', 'Introduction to Programming', 15)
# print("{}, {}, {}".format(course.code, course.name, course.points))
# # print(course)
# # print(sorted(course.to_dictionary().items()))


# result = {}



# # # kjhjk
# # result["sdf"] = "sdff"
# # result[12] = "abcd"
# # print(result)
# # result.items()
# # print(result.items())
# # for i, j in result.items():
# #     print(i,j)

# # for i in result.keys():
# #     print(i,result[i])

# set1 = set()

# set1.add("a")
# print(set1)

def read_data(filename):
    file = open(filename, "r")
    lines = file.read()
    file.close()
    # print(lines)

    list1 = lines.split()
    dict1 = {}
    
    temp = set(list1)
    set1 = list(temp)
    set1.sort()

    for i in  set1:

        count = list1.count(i)
        if count in dict1.keys():
            dict1[count].append(i)
        else:
            dict1[count] = [i]
    return dict1, len(list1)


# Question 23
def print_n_most_common(filename, n):
    """asd"""
    dict1, list_len = read_data(filename)
    
    keys = list(dict1.keys())
    keys.sort()
    
    print( keys)

    i = 1
    print_num = 0
    limit = 0
    while print_num < n and limit < 100 and i  < len(keys)+1:
        limit += 1
        
        for word in dict1[keys[-i]]:
            if(print_num < n):
                print(word, keys[-i])
                print_num += 1
        i += 1





#Z:\\Tutor 2021\\CS121\\codes\\revision\\test1.txt
print_n_most_common('test1.txt', 7)