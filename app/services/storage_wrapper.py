import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))

from storage import db_manage

db_conn = db_manage.connect()
