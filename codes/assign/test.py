"""a program that prints a summary of the albums in a given file"""
import os.path

class Album:
    """Stores the information about an album"""
    
    def __init__(self, album_id, name, band, cost):
        """The data that forms an album, note that:
        - album_id is a int
        - cost is a float
        - the rest are strings
        """
        self.album_id = album_id
        self.name = name
        self.band = band
        self.cost = cost
        self.total_sold = 0

    def add_to_sold(self, count):
        """Adds to the internal album counter of the album"""
        if count >= 0:
            self.total_sold += count
        else:
            template = "Attempt to add {} to Album: {}. VALUE MUST NOT BE NEGATIVE"
            raise ValueError(template.format(count, self.album_id))
                             
    def __str__(self):
        output = ""
        output += "Album Name: {}\n".format(self.name)
        output += "Band: {}\n".format(self.band)
        output += "Purchase Price: ${:.2f}".format(self.cost)
        return output
    
    def __repr__(self):
        return "<<{}>>".format(self.album_id)


     
def extract_album(lines, index):
    """ takes a list of lines and an index into that list 
    and returns an instance of an Album"""
    data = lines[index:]
    list1 = []
    res = []
    
    for i in range(len(data)):
        if "<album>" in data[i]:
            list2 = []
            
            list2.append(data[i+1].strip("\n"))
            list2.append(str(data[i+2].strip("\n")))
            list2.append(str(data[i+3].strip("\n")))
            list2.append(float(data[i+4].strip("\n")))
            
            list1.append(list2)
    for i in range(len(list1)):
        id_num = str(list1[i][0])
        name = str(list1[i][1])
        band = str(list1[i][2])
        cost = list1[i][3]
        my_album = Album(id_num, name, band, cost)
        res.append(my_album)

    return res[0]

def extract_all_albums(lines):
    """ takes a list of lines and an index into that list 
    and returns an instance of an Album"""
    acc = extract_album(lines, 0)
    data = lines
    list1 = []
    res = {}
    
    for i in range(len(data)):
        if "<album>" in data[i]:
            list2 = []
            
            list2.append(data[i+1].strip("\n"))
            list2.append(str(data[i+2].strip("\n")))
            list2.append(str(data[i+3].strip("\n")))
            list2.append(float(data[i+4].strip("\n")))
            
            list1.append(list2)
    for i in range(len(list1)):
        id_num = int(list1[i][0])
        name = str(list1[i][1])
        band = str(list1[i][2])
        cost = list1[i][3]
        my_album = Album(id_num, name, band, cost)
        res[id_num] = my_album
    return res

def extract_all_sale(line):
    """ takes a list of lines and an index into that list 
    and returns an instance of an sales"""
    list1 = []
    res = {}
    
    start = 0
    stop = 0
 

    for i in range(len(line)):
        if "<sales>" in line[i]:
            start = i+1

        if "</sales>" in line[i]:
            stop = i

    for i in range(start, stop, 1):
        # print("sale: ",line[i])
        list1 = line[i].split(',')
        

        if list1[1] in res:
            res[list1[1]] = int(res[list1[1]])+ int(list1[2])
        else:
            res[list1[1]] = int(list1[2])
    
    # print(res.__str__())
    return res

def rank(sold):
    """"rank the record by sale number"""
    if sold >= 50000 and sold < 100000:
        return "Gold"
    elif sold >= 100000 and sold < 500000:
        return "Platinum"
    elif sold >= 500000:
        return "Diamond"
    else:
        return ""

def sort_print(display):
    """print by the order of sold number"""
    keys = list(display.keys())
    for i in range(len(keys)):
        keys[i] = int(keys[i])
    keys.sort()
    keys.reverse()
    for i in range(len(keys)):
        print(display[keys[i]])



def print_graph(sales):
    """print graph of sales"""
    print()
    print("Sales Bar Graph")
    print("------------------------------")
    print("  ID  Freq Graph")
    sorted_sales = sorted(sales, key=sales.get, reverse=True)
    total = sum(list(sales.values()))
    # print(sorted_sales)
    # print(total)
    bar_sales = {}
   
    


    for i in sorted_sales: 

        # print(int(sales[i]/total*100))

        print("{:>4}{:>5}% {}".\
            format(i, int(sales[i]/total*100).__str__(),\
                 int(sales[i]/total*100)*'='))
    
   
def main():
    """a program that prints a summary of the albums in a given file"""
    filename = None
    while filename is None:
        filename = input('Enter a data file name: ')
        if not os.path.isfile(filename):
            print('Invalid File Name Entered!')
            filename = None    
    file = open(filename)
    content = file.read()
    file.close()

    lines = content.splitlines()
    albums = extract_all_albums(lines)
    sales = extract_all_sale(lines)

    print("\nAlbum Catalogue Summary")
    print("------------------------------------------------------------")
    print("ID   ALBUM NAME                        # SOLD    CERTIFICATE")

    display = {}

    for album_id, album in sorted(albums.items()):
        display[sales[album_id.__str__()]] = "{:<5}{:<30}{:>10}{:>15}".\
            format(album_id, album.name, sales[album_id.__str__()], \
                rank(int(sales[album_id.__str__()])))
    sort_print(display)
    print_graph(sales)
main()