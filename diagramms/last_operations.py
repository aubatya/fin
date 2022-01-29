import matplotlib.pyplot as plt
from fin.db.ORM.query import get_stat
from time import time


def create_diagram(uid=1, period=1):
    data = get_stat(uid, period)
    values = []
    labels = []
    width = 0.55
    for item in data:
        labels.append(item[0])
        labels.append(int(item[1]))

    fig, ax = plt.subplots()

    ax.bar(labels, values, width, label='Total', color="#696969")

    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.set_facecolor("#C0C0C0")

    path = "../resources/{0}.png".format(str(uid) + "/" + str(int(time())))
    plt.savefig(path, facecolor="#FFE4E1")
    # plt.show()

create_diagram()