import time


def get(geonameid):
    starttime = time.time()
    with open("RU.txt", "r") as f:
        line = f.readline()
        while line:
            if line.split("\t")[0] == geonameid:
                print("Find!")
            line = f.readline()
    endtime = time.time()
    print(endtime - starttime)


get(12547745)
