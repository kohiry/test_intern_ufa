#
# from translate import Translator
from datetime import datetime

import pytz


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


class TwoCityInformation:
    # @staticmethod
    # def rename(name: str):
    #     translator = Translator(from_lang="ru", to_lang="en")
    #     return translator.translate(name)

    @staticmethod
    def send(massive):
        if len(massive) < 2:
            return {"result": "not found  all citys"}
        if float(massive[0]["latitude"]) > float(massive[1]["latitude"]):
            massive.append({"Кто сервенее?": "первый город"})
        else:
            massive.append({"Кто сервенее?": "второй город"})
        time_1, time_2 = (pytz.timezone(i["modification date"]) for i in massive[:2])
        city_1, city_2 = (datetime.now(i) for i in [time_1, time_2])
        diff_hours = city_1.hour - city_2.hour
        massive.append({"Одинаковая ли временная зона?": diff_hours})

        return massive

    @staticmethod
    def get(name1: str, name2: str):
        # name_1, name_2 = (TwoCityInformation.rename(i) for i in [name1, name2])
        # print(name_1, name_2)
        massive = []
        with open("RU.txt", "r") as f:
            line = f.readline()
            while line:
                alternativename_line = line.split("\t")[3]
                # name_line = line.split("\t")[1]
                geonameid = line.split("\t")[0]
                # print(name_line)
                if name1 in alternativename_line.split(","):
                    name1 = "zxc"
                    massive.append(GetCity.get(geonameid))
                if name2 in alternativename_line.split(","):
                    name2 = "zxc"
                    massive.append(GetCity.get(geonameid))
                if len(massive) == 2:
                    break
                line = f.readline()
        return TwoCityInformation.send(massive)


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
                if start <= last_step and start + limit > last_step:
                    massive.append(GetCity.transform(line))
                # print(last_step)
                line = f.readline()
        return massive


# print(GetCityPages.get(1, 2))
