import psycopg2
import config

#conn = psycopg2.connect(config.SQLALCHEMY_DATABASE_URI)

def connect_db():
    conn = psycopg2.connect(config.SQLALCHEMY_DATABASE_URI)
    cursor = conn.cursor()
    return cursor

def search_tag(keyword):
    cursor = connect_db()
    print("Connection established")
    sql = "SELECT pin_id, image_url, title FROM pin_detail JOIN pin ON pin.id = pin_detail.pin_id WHERE %(keyword)s = ANY (pin_detail.tags)"
    cursor.execute(sql,  {'keyword': keyword})
    rows = cursor.fetchall()
    return rows

# pins = search_tag('text')
# print(pins)

#cursor.close()
#conn.close()