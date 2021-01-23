# import matplotlib.pyplot as plt
# from random import randint

# names = ['Peter', 'Nikau', 'Ava', 'Harper', 'Ella', 'Sophie' ]
# num_names = len(names)
# data = [randint(0, 500) for _ in range(num_names)]  # Some random numbers for testing

# axes = plt.axes()
# axes.bar(range(num_names), data, tick_label=names)
# axes.set_title("Crunchie bars per annum")
# axes.set_xlabel("Name")
# axes.set_ylabel("Crunchie bars")
# plt.show()




test1 = 35.71
test2 = 16.67
labs = 80
assignment = 80
for exam in range(100):
    mark = test1*0.1 + test2*0.1 + labs*0.1 + assignment*0.15 + exam*0.55
    invig = (test1*0.1 + test2*0.1 + exam*0.55)/0.75
    print(f'{exam} -> overall={mark:.1f}    test+exam avg = {invig:.2f}')