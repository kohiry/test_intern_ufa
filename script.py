import time


def get(geonameid: str) -> None:
    starttime = time.time()
    with open("RU.txt", "r") as f:
        line = f.readline()
        while line:
            # print(line.split("\t")[0])
            if line.split("\t")[0] == geonameid:
                print("Find!")
            line = f.readline()
    endtime = time.time()
    print(endtime - starttime)


get('12547726')
