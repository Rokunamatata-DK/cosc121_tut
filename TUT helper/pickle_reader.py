# import os
import pickle

def load_dicts(dicts_session):
    file = open('logs.pydata', 'rb')
    data = pickle.load(file)
    file.close()
    for dic in data:
        dicts_session.append(dic)


dicts_session = []
load_dicts(dicts_session)

print(dicts_session,"\n")

sums=0

for dic in dicts_session:
    print("\n dic:::::",dic)
    sums += dic['payment']


print("sum is : ",sums)