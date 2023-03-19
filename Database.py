from pyairtable import Table, Base


class Database:
    def __init__(self, api_key: str, base_id: str):
        self.__api_key = api_key
        self.__base_id = base_id
        self.__base = Base(api_key, base_id)

    def statistic(self) -> dict:
        """

        :return: dict of
        """
        return {"prisoners_count": len(self.__base.all("prisoners")),
                "friends_count": len(self.__base.all("users")),
                "tasks": len(self.__base.all("tasks"))}


if __name__ == "__main__":
    import toml

    config = toml.load("secrets.toml")
    db = Database(config["api_key"], config["base_id"])
    print(db.statistic())
