# import time
#


class GetCity:
    @staticmethod
    def transform(line: str):
        list_line = line.split("\t")
        answer = {
            "geonameid": list_line[0],
            "name": list_line[1],
            "asciiname": list_line[2],
            "alternatenames": list_line[3],
            "latitude": list_line[4],
            "longitude": list_line[5],
            "feature class": list_line[6],
            "feature code": list_line[7],
            "cc2": list_line[8],
            "admin1 code": list_line[9],
            "admin2 code": list_line[10],
            "admin3 code": list_line[11],
            "admin4 code": list_line[12],
            "population": list_line[13],
            "elevation": list_line[14],
            "dem": list_line[15],
            "timezone": list_line[16],
            "modification date": list_line[17],
        }
        return answer

    @staticmethod
    def get(geonameid: str) -> None:
        # starttime = time.time()
        with open("RU.txt", "r") as f:
            line = f.readline()
            while line:
                # print(line.split("\t")[0])
                if line.split("\t")[0] == geonameid:
                    # print("Find!")
                    return GetCity.transform(line)
                line = f.readline()

        # endtime = time.time()
        # print(endtime - starttime)


class GetCityPages:
    @staticmethod
    def get(number_page: int, limit: int):
        # starttime = time.time()
        start = number_page * limit
        last_step = 0
        massive = []
        with open("RU.txt", "r") as f:
            line = f.readline()
            while line:
                last_step += 1
                if start <= last_step and start + limit >= last_step:
                    massive.append(GetCity.transform(line))
                # print(last_step)
                line = f.readline()
        return massive


print(GetCityPages.get(1, 2))
