import matplotlib.pyplot as plt


def manf(n):
    signal = []
    x = []
    high = 2.5
    low = -2.5
    count = 0

    for i in n:
        if i == 0:
            x.append(count)
            signal.append(high)
            count = count+0.5
            x.append(count)
            signal.append(high)
            x.append(count)
            signal.append(low)
            count = count+0.5
            x.append(count)
            signal.append(low)
        else:
            x.append(count)
            signal.append(low)
            count = count+0.5
            x.append(count)
            signal.append(low)
            x.append(count)
            signal.append(high)
            count = count+0.5
            x.append(count)
            signal.append(high)
    plt.plot(x,signal)
    plt.show()

