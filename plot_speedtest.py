import matplotlib.dates as md
import dateutil
import pandas as pd
import matplotlib.pyplot as plt

def main():

    x = []
    y = []
    for line in open('speedtest.log', 'r'):
        lines = [i for i in line.split("  ")]
        print(lines)
        x.append(lines[0])
        y.append(float(lines[3]))


    dates = [dateutil.parser.parse(s) for s in x]
    print(dates)
    plt.subplots_adjust(bottom=0.2)
    plt.xticks(rotation=25)

    ax=plt.gca()
    ax.set_xticks(dates)

    xfmt = md.DateFormatter('%H:%M')
    ax.xaxis.set_major_formatter(xfmt)


    plt.title("Download speed")
    plt.xlabel('Time')
    plt.ylabel('Mbs/s')
    plt.yticks(y)
    plt.plot(dates, y, "o-")

    plt.show()


if __name__ == '__main__':
    main()

