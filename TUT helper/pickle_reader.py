import os
import pickle

file = open('animals.pydata', 'rb')

data = pickle.load(file)

print(data)

file.close()

for line in data:
    print(line)