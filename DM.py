import matplotlib.pyplot as plt

def dmf(n):
    signal = []
    x = []
    high = 2.5
    low = -2.5
    count = 0

    previous_value = high

    for i in n:
        if i == 0:
            if previous_value == high:
                x.append(count)
                signal.append(high)
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
                previous_value = high
            else:
                x.append(count)
                signal.append(low)
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
                previous_value = low
        else:
            x.append(count)
            signal.append(previous_value)
            count = count+0.5
            x.append(count)
            signal.append(previous_value)
            if previous_value == high:
                previous_value = low
            else:
                previous_value = high
            x.append(count)
            signal.append(previous_value)
            count = count+0.5
            x.append(count)
            signal.append(previous_value)

    plt.plot(x,signal)
    plt.show()