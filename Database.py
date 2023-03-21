from pyairtable import Table, Base
import random


class Database:
    def __init__(self, api_key: str, base_id: str):
        self.__api_key = api_key
        self.__base_id = base_id
        self.__base = Base(api_key, base_id)

    def statistic(self) -> dict:
        """
        :return: dict of statistic data
        """
        all_prisoners = sorted(self.__base.all("prisoners"),
                               key=lambda x: x["fields"]["friendsCount"])

        return {"prisoners_count": len(all_prisoners),
                "friends_count": len(self.__base.all("users")),
                "tasks": len(self.__base.all("tasks")),
                "less_friends": all_prisoners[:3]}

    def get_random_prisoner(self) -> dict:
        data = self.__base.all("prisoners")
        return data[random.randint(0, len(data))]

    def get_prisoners_by_city(self) -> dict:
        data = self.__base.all("prisoners")
        city_base = self.__base.all("city")
        cities = {i["fields"]["city"][0] if "city" in i["fields"] else "None" for i in data}
        id_to_name = dict()
        for i in cities:
            for j in city_base:
                if j["id"] == i:
                    id_to_name[i] = j["fields"]["name"]
                    break
        city_prisoners = dict()
        city_prisoners["None"] = list()
        for i in data:
            if "city" in i["fields"]:
                if id_to_name[i["fields"]["city"][0]] in city_prisoners:
                    city_prisoners[id_to_name[i["fields"]["city"][0]]].append(i)
                else:
                    city_prisoners[id_to_name[i["fields"]["city"][0]]] = [i, ]
            else:
                city_prisoners["None"].append(i)
        return city_prisoners

    def find_prisoner(self, string):
        data = self.__base.all("prisoners")
        answer = []
        for i in data:
            if "name" in i["fields"] and string.lower() in i["fields"]["name"].lower():
                answer.append(i)
            if "prison" in i["fields"] and string.lower() in i["fields"]["prison"][0].lower():
                answer.append(i)
        return answer

    def get_page(self, nick):
        data = self.__base.all("prisoners")
        for i in data:
            if "shortName" in data[i]["fields"] and nick in data[i]["fields"]["shortName"]:
                return i


if __name__ == "__main__":
    import toml

    config = toml.load("secrets.toml")
    db = Database(config["api_key"], config["base_id"])
    print(db.statistic())
