class Result:
    """ Class to save results to website """
    def __init__(self, date, race_id, name, ranking_code, uci_id, place, category):
        self.date = date
        self.race_id = race_id
        self.name = name
        self.ranking_code = ranking_code
        self.uci_id = uci_id
        self.place = place
        self.category = category
        self.point = 0

    def get_ranking_points(self):

        result_point = 0

        # RANKING CODE 1 - Mistrovství ČR
        if self.ranking_code == "1":
            if self.place == "1":
                result_point = 350
            elif self.place == "2":
                result_point = 300
            elif self.place == "3":
                result_point = 250
            elif self.place == "4":
                result_point = 200
            elif self.place == "5":
                result_point = 190
            elif self.place == "6":
                result_point = 180
            elif self.place == "7":
                result_point = 170
            elif self.place == "8":
                result_point = 160
            elif self.place == "9" or self.place == "10":
                result_point = 125
            elif self.place == "11" or self.place == "12":
                result_point = 120
            elif self.place == "13" or self.place == "14":
                result_point = 115
            elif self.place == "15" or self.place == "16":
                result_point = 110
            elif self.place == "17" or self.place == "18" or self.place == "19" or self.place == "20":
                result_point = 90
            elif self.place == "21" or self.place == "22" or self.place == "23" or self.place == "24":
                result_point = 80
            elif self.place == "25" or self.place == "26" or self.place == "27" or self.place == "28":
                result_point = 70
            elif self.place == "29" or self.place == "30" or self.place == "31" or self.place == "32":
                result_point = 90

        # RANKING CODE 2 - Český pohár
        elif self.ranking_code == 2:
            if self.place == "1":
                result_point = 150
            elif self.place == "2":
                result_point = 130
            elif self.place == "3":
                result_point = 115
            elif self.place == "4":
                result_point = 100
            elif self.place == "5":
                result_point = 90
            elif self.place == "6":
                result_point = 80
            elif self.place == "7":
                result_point = 75
            elif self.place == "8":
                result_point = 70
            elif self.place == "9" or self.place == "10":
                result_point = 65
            elif self.place == "11" or self.place == "12":
                result_point = 60
            elif self.place == "13" or self.place == "14":
                result_point = 55
            elif self.place == "15" or self.place == "16":
                result_point = 50
            elif self.place == "17" or self.place == "18" or self.place == "19" or self.place == "20":
                result_point = 40
            elif self.place == "21" or self.place == "22" or self.place == "23" or self.place == "24":
                result_point = 35
            elif self.place == "25" or self.place == "26" or self.place == "27" or self.place == "28":
                result_point = 30
            elif self.place == "29" or self.place == "30" or self.place == "31" or self.place == "32":
                result_point = 25

        # RANKING CODE 3 - Česká liga, Moravská liga
        elif self.ranking_code == 3:
            if self.place == "1":
                result_point = 90
            elif self.place == "2":
                result_point = 70
            elif self.place == "3":
                result_point = 60
            elif self.place == "4":
                result_point = 50
            elif self.place == "5":
                result_point = 40
            elif self.place == "6":
                result_point = 30
            elif self.place == "7":
                result_point = 25
            elif self.place == "8":
                result_point = 20
            elif self.place == "9" or self.place == "10":
                result_point = 15
            elif self.place == "11" or self.place == "12":
                result_point = 10
            elif self.place == "13" or self.place == "14":
                result_point = 8
            elif self.place == "15" or self.place == "16":
                result_point = 6

        # RANKING CODE 4 - Volný závod
        else:
            if self.place == "1":
                result_point = 60
            elif self.place == "2":
                result_point = 45
            elif self.place == "3":
                result_point = 40
            elif self.place == "4":
                result_point = 35
            elif self.place == "5":
                result_point = 30
            elif self.place == "6":
                result_point = 25
            elif self.place == "7":
                result_point = 20
            elif self.place == "8":
                result_point = 15
            elif self.place == "9" or self.place == "10":
                result_point = 8
            elif self.place == "11" or self.place == "12":
                result_point = 6
            elif self.place == "13" or self.place == "14":
                result_point = 4
            elif self.place == "15" or self.place == "16":
                result_point = 2

        return result_point

    def set_sql(self):

        self.point = self.get_ranking_points()

        items = "rider, place, points, category, event, name, date"
        values = f"'{self.uci_id}','{self.place}','{self.point}','{self.category}','{self.race_id}','{self.name}','{self.date}'"
        self.sql = "INSERT INTO result_result (" + items + ") VALUES (" + values + ")"
        print(self.sql)

    def write_to_sqlite(self):
        cur = self.conn.cursor()
        cur.execute(self.sql)
        self.conn.commit()

    def create_connection(self):
        """ create a database connection to a SQLite database """
        self.conn = None
        try:
            self.conn = sqlite3.connect(r"/home/temp1ar/Development/django-bmx-web/db.sqlite3")
        except Error as e:
            print(e)

    def close_connection(self):
        self.conn.close()