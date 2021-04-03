import pandas as pd
import sqlite3
from sqlite3 import Error

from result import Result

# import requests

URL_CLUB = "http://localhost:8080/api/club/"
URL_RIDER = "http://localhost:8080/api/rider/"


class Club:
    def __init__(self):
        self.team_name = ""
        self.club_name = ""
        self.ico = ""
        self.street = ""
        self.city = ""
        self.zip_code = ""
        self.region = ""
        self.web = ""
        self.facebook = ""
        self.instagram = ""
        self.contact_person = ""
        self.contact_email = ""
        self.contact_phone = ""
        self.bank_account = ""
        self.is_active = "1"
        self.have_track = ""
        self.track_id = ""

    def upgrade_region(self, region):
        if self.region == "Praha":
            self.region = "hlavní město Praha"
        else:
            self.region = self.region + " kraj"

    def set_sql(self):

        self.sql = "INSERT INTO club_club (team_name, club_name, ico, street, city, zip_code, region, web, facebook, instagram, contact_person, contact_email, contact_phone, bank_account, is_active, have_track, track_id) " \
                   "VALUES (' " + self.team_name + " ', ' " + self.club_name + " ', ' " + self.ico + " ', ' " + self.street + " ', ' " + self.city + " ', ' " + self.zip_code + " ',  ' " + self.region + " ',' " + self.web + " ', ' " + self.facebook + " ', ' " + self.instagram + " ', ' " + self.contact_person + " ', ' " + self.contact_email + " ', ' " + self.contact_phone + " ', ' " + self.bank_account + " ', ' " + self.is_active + " ', ' " + self.have_track + " ', ' " + self.track_id + " ') "

        print(self.sql)

    def create_connection(self):
        """ create a database connection to a SQLite database """
        self.conn = None
        try:
            self.conn = sqlite3.connect(r"/home/temp1ar/Development/django-bmx-web/db.sqlite3")
        except Error as e:
            print(e)
        # finally:
        #     if self.conn:
        #         print ("Chyba připojení databáze")

    def write_data(self):

        cur = self.conn.cursor()
        cur.execute(self.sql)
        self.conn.commit()

    def close_connection(self):
        self.conn.close()

    def import_data(self):
        df = pd.read_csv("clubs.csv", delimiter=',')

        for x in range(0, 34):
            self.team_name = df.iloc[x][1]
            self.street = df.iloc[x][4]
            self.city = df.iloc[x][5]
            self.zip_code = df.iloc[x][6]
            self.region = df.iloc[x][7]

            self.contact_person = str(df.iloc[x][11])
            self.contact_email = str(df.iloc[x][12])
            self.contact_phone = str(df.iloc[x][13])

            self.create_connection()
            self.upgrade_region(self.region)
            self.set_sql()
            self.write_data()
            self.close_connection()


class Rider:
    def __init__(self):
        self.uci_id = ""
        self.first_name = ""
        self.last_name = ""
        self.date_of_birth = ""
        self.gender = ""
        self.plate = ""
        self.transponder_20 = ""
        self.transponder_24 = ""
        self.club = ""
        self.is_20 = ""
        self.is_24 = ""
        self.is_elite = ""
        self.email = ""
        self.have_girl_bonus = "0"

    def create_connection(self):
        """ create a database connection to a SQLite database """
        self.conn = None
        try:
            self.conn = sqlite3.connect(r"/home/temp1ar/Development/django-bmx-web/db.sqlite3")
        except Error as e:
            print(e)

    def write_data(self):

        cur = self.conn.cursor()
        cur.execute(self.sql)
        self.conn.commit()

    def close_connection(self):
        self.conn.close()

    def set_sql(self):

        items = "uci_id, first_name, last_name, gender, date_of_birth, have_girl_bonus, is_20, is_24, transponder_20, transponder_24, club_id, plate, email, is_active, is_approwe, have_valid_licence, is_elite, is_in_talent_team, is_in_representation, photo"
        values = f"'{self.uci_id}', '{self.first_name}', '{self.last_name}', '{self.gender}', '{self.date_of_birth}', '{self.have_girl_bonus}', '{self.is_20}', '{self.is_24}', '{self.transponder_20}', '{self.transponder_24}', '{self.club}', '{self.plate}', '{self.email}', '1', '1', '1', '{self.is_elite}','0','0', 'static/images/riders/uni.jpeg'"
        self.sql = "INSERT INTO rider_rider (" + items + ") VALUES (" + values + ")"

    def import_data_from_csv(self):
        df = pd.read_csv('riders.csv', delimiter=",")

        for x in range(0, 725):
            self.uci_id = df.iloc[x][1]
            self.first_name = df.iloc[x][8].strip()
            self.last_name = df.iloc[x][9].strip()
            self.date_of_birth = df.iloc[x][7].replace("/", "-")
            self.gender = df.iloc[x][10]
            if self.gender == "M":
                self.gender = "Muž"
                self.have_girl_bonus = "0"
            else:
                self.gender = "Žena"
                self.have_girl_bonus = "1"
            self.is_20 = df.iloc[x][14]
            self.is_24 = df.iloc[x][15]
            self.plate = df.iloc[x][20]
            self.transponder_20 = df.iloc[x][29]
            self.transponder_24 = df.iloc[x][30]
            self.email = df.iloc[x][47]
            self.is_elite = df.iloc[x][48]
            self.club = df.iloc[x][11]
            if self.club == "Bikrosclub Řepy":
                self.club = "36"
            elif self.club == "SC BMX Benátky":
                self.club = "38"
            elif self.club == "TJ BMX Pardubice":
                self.club = "47"
            elif self.club == "TJ Favorit Brno":
                self.club = "42"
            elif self.club == "TJ Slovan Bohnice-BMX":
                self.club = "51"
            elif self.club == "BMX &amp; 4X TEAM OLYMPUS":
                self.club = "54"
            elif self.club == "BMX &amp; 4X Team BRNO":
                self.club = "55"
            elif self.club == "UTOPIA bikes Zábřeh":
                self.club = "52"
            elif self.club == "FALER BIKE team":
                self.club = "49"
            elif self.club == "AUTOKLUB BMX team Dobřany":
                self.club = "66"
            elif self.club == "TJ BMX Třinec":
                self.club = "50"
            elif self.club == "OK TEAM":
                self.club = "64"
            elif self.club == "TUFÍR TEAM":
                self.club = "43"
            elif self.club == "SK Jantar Opava":
                self.club = "44"
            elif self.club == "BMX Bílina":
                self.club = "41"
            elif self.club == "Bike Team Vyškov":
                self.club = "58"
            elif self.club == "AMK BMX Studénka":
                self.club = "56"
            elif self.club == "Nižbor Racing Team":
                self.club = "57"
            elif self.club == "Bikros klub Jeseník":
                self.club = "40"
            elif self.club == "BIKE TEAM Uničov":
                self.club = "39"
            elif self.club == "FOXHOLESHOP.cz":
                self.club = "62"
            elif self.club == "AMK Kemp Hranice":
                self.club = "37"
            elif self.club == "PARDUS TUFO Prostějov":
                self.club = "45"
            elif self.club == "Laguna cycles team":
                self.club = "60"
            elif self.club == "Koloshop cz SK Horní Krupka":
                self.club = "46"
            elif self.club == "B4 Team":
                self.club = "59"
            elif self.club == "CK Slavoj Terezín":
                self.club = "53"
            elif self.club == "BMX Ostrava  ":
                self.club = "65"
            elif self.club == "SK BMX Klatovy":
                self.club = "48"
            elif self.club == "Duratec Team Mariánské lázně":
                self.club = "104"
            elif self.club == "Laguna Bike Team Přerov":
                self.club = "60"
            elif self.club == "BIKESTRIKE.com":
                self.club = "68"
            elif self.club == "BMX MOPED KLUB Protivín":
                self.club = "67"
            else:
                self.club = "105"

            print(
                f'Přidávám jezdce {self.first_name} {self.last_name}, datum narození: {self.date_of_birth}, pohlaví: {self.gender}, transponder20: {self.transponder_20}, transponder24: {self.transponder_24} startovní číslo: {self.plate}')

            self.create_connection()
            self.set_sql()
            self.write_data()
            self.close_connection()


def web_controller():
    while True:
        print("****************************************")
        print("******* CZECH BMX WEB CONTROLLER *******")
        print("****************************************")
        print("(1) Nahrát kluby z cvs do databáze webu")
        print("(2) Nahrát jezdce z motosheets cvs do databáze webu")
        print("(3) Nahrát výsledky na web")
        print("(99) Ukončit program")

        volba = input("Jaká je tvoje volba? ")

        if volba == "99":
            print("Program se ukončuje")
            exit(0)

        elif volba == "1":
            club = Club()
            club.import_data()

        elif volba == "2":
            rider = Rider()
            rider.import_data_from_csv()

        elif volba == "3":
            name = input("Zadej název závodu: ")
            race_id = input("Zadej ID závodu: ")
            ranking_code = input("Zadej kód rankingu (01-MČR, 02-ČP, 03-ČL ML, 04-Volný): ")
            date = input("Zadej datum závodu ve tvaru YYYY-MM-DD: ")
            file = input("Zadej název souboru: ")
            try:
                data = pd.read_excel(file, sheet_name="Results")
                print(data)
            except:
                print("Nastala chyba v načítání dataframu")

            for i in range(1, len(data.index)):
                uci_id = str(data.iloc[i][1])
                category = data.iloc[i][4]
                place = str(data.iloc[i][0])

                result = Result(date, race_id, name, ranking_code, uci_id, place, category)
                result.set_sql()


if __name__ == '__main__':
    web_controller()
