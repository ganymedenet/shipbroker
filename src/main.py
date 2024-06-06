import json
import time

from utils.sql import DBClient
from owner_searcher import OwnerSearcher


class ShipManager:
    def __init__(self):
        self.db = DBClient()
        self.owner_searcher = OwnerSearcher()

    def get_ships(self):
        sql = "SELECT * FROM ships;"

        sql = "SELECT row_to_json(sh) FROM (SELECT * FROM ships) sh;"

        res = self.db.exec_sql(sql_req=sql, one=False)

        return res

    def update_ship(self, ship_id, data):
        owner_json = json.dumps(data["owner"]).replace("'", "''")
        manager_json = json.dumps(data["manager"]).replace("'", "''")

        sql = f"""UPDATE ships SET 
                owner = '{owner_json}'::jsonb,
                manager = '{manager_json}'::jsonb
                WHERE id = '{ship_id}'
        """
        # print(sql)
        self.db.exec_sql_comm(sql)

    def run(self):
        ships = self.get_ships()

        for ship in ships:
            ship = ship[0]

            data = self.owner_searcher.get_data(ship["general"]["imo"])
            # print(data)
            self.update_ship(ship_id=ship["id"], data=data)

            print(f"Ship {ship['id']} has been updated!\n")
            time.sleep(0.5)

        print("DONE")


if __name__ == "__main__":
    sm = ShipManager()
    sm.run()
