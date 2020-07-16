import matplotlib.pyplot as plt

def nrzif(n):
    signal = []
    x = []
    high = 5
    low = 0
    count = 0

    previous_value = 0

    for i in n:
        if i == 0:
            x.append(count)
            signal.append(previous_value)
            count = count+1
            x.append(count)
            signal.append(previous_value)
        else:
            if previous_value == 0:
                x.append(count)
                signal.append(high)
                count = count+1
                x.append(count)
                signal.append(high)
                previous_value = high
            else:
                x.append(count)
                signal.append(low)
                count = count+1
                x.append(count)
                signal.append(low)
                previous_value = low

    plt.plot(x,signal)
    plt.show()