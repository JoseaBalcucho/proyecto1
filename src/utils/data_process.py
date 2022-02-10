import configparser
from pathlib import Path
import os
import sys
import requests
import mysql.connector

class Data_process(object):

    def __init__(self):
        CONFIG_FILE = "../config.ini"
        path = Path(__file__)
        self.ROOT_DIR = path.parent.absolute()

        config_path = os.path.join(self.ROOT_DIR, CONFIG_FILE)
        
        config = configparser.ConfigParser()
        config.read(config_path)
        self.config = config
        self.dbconn = self.mysql_conn(config)
        self.dbcursor = self.dbconn.cursor(
            dictionary=True)
        self.dbcursor.execute(
            "SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED")


    def mysql_conn(self, config):
        try:
            dbconn = mysql.connector.connect(
                host=config.get('mysql', 'db_host'),
                user=config.get('mysql', 'db_user'),
                passwd=config.get('mysql', 'db_pass'),
                db=config.get('mysql', 'db_name'))
            return dbconn
        except mysql.connector.Error as e:
            print("Error attempting db connection: %d, %s"
                % (e.args[0], e.args[1]))
            sys.exit(1)
        except Exception as e:
            print("Error connecting to mysql database")


    def get_id(self, id):
        
        sql = """SELECT movieid, title, genres, camponew1
        FROM u227062265_bigdata.movies
        WHERE movieid = '{}' """.format(id)
        print(sql)
        try:
            self.dbcursor.execute(sql)
            result = self.dbcursor.fetchall()
            if result:
                return result
            else:
                return None
        except Exception as e:
            raise Exception(
                e, 409, '', {"message": "Error : database query conflict"})
