import os
import pickle

# file = open('logs.pydata', 'rb')

# data = pickle.load(file)

# print(data)

# file.close()

# for line in data:
#     dic= line
#     print("\nline: =",line)


def load_dicts(dicts_session):
    file = open('logs.pydata', 'rb')
    data = pickle.load(file)
    file.close()
    for dic in data:
        dicts_session.append(dic)


dicts_session = []
load_dicts(dicts_session)

print(dicts_session,"\n")

for dic in dicts_session:
    print("\n dic:::::",dic)