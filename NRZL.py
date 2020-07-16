import matplotlib.pyplot as plt



def nrzlf(n):
    signal = []
    x = []
    high = 5
    low = 0
    count = 0

    for i in n:
        if i == 0:
            x.append(count)
            signal.append(high)
            count = count+1
            x.append(count)
            signal.append(high)
        else:
            x.append(count)
            signal.append(low)
            count = count+1
            x.append(count)
            signal.append(low)




    plt.plot(x,signal)
    plt.show()