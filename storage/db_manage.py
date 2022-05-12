import configparser
import mysql.connector

def get_config(file_name='config.ini', section="mysqlDB"):
    config = configparser.ConfigParser()
    config.read(file_name)
    mysqlConfig = config[section]

def connect():
    mysqlConfig = get_config()
    return mysql.connector.connect(
        host=mysqlConfig['host'],
        user=mysqlConfig['user'],
        passwd=mysqlConfig['pass'],
        database=mysqlConfig['db'],
        port=mysqlConfig['port']
    )
