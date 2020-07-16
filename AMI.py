import matplotlib.pyplot as plt


def amif(n):
    signal = []
    x = []
    high = 2.5
    low = -2.5
    neutral = 0
    count = 0

    previous = 0

    for i in n:
        if i == 0:
            x.append(count)
            signal.append(neutral)
            count = count+1
            x.append(count)
            signal.append(neutral)
            previous = 0
        else:
            if previous == 0:
                x.append(count)
                signal.append(high)
                count = count+1
                x.append(count)
                signal.append(high)
                previous = 1
            else:
                x.append(count)
                signal.append(low)
                count = count+1
                x.append(count)
                signal.append(low)
                previous = 0
    plt.plot(x,signal)
    plt.show()
    