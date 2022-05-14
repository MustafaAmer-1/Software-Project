import configparser, os
import mysql.connector

PATH = os.path.dirname(__file__)

def get_config(file_name='config.ini', section="mysqlDB"):
    config = configparser.ConfigParser()
    config.read(os.path.join(PATH, file_name))
    mysqlConfig = config[section]
    return mysqlConfig

def connect():
    mysqlConfig = get_config()
    return mysql.connector.connect(
        host=mysqlConfig['host'],
        user=mysqlConfig['user'],
        passwd=mysqlConfig['pass'],
        database=mysqlConfig['db'],
        port=mysqlConfig['port']
    )
