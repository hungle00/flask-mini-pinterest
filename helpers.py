import psycopg2
from models import db, Pin, PinDetail
from azures.azure_cv import AzureComputerVision
import config

##### CREATE MODEL  #####
def create_pin(title, image_url, user):
    this_pin = Pin(title=title, image_url=image_url, pin_by=user)
    db.session.add(this_pin)
    db.session.commit()
    return this_pin

def create_pin_detail(pin_id):
    pin = Pin.query.get(pin_id)
    azure_cv = AzureComputerVision(pin.image_url)
    description_results = azure_cv.description_image()
    if description_results is not None:
        pin_detail = PinDetail(caption=description_results.captions[0].text, tags=description_results.tags, pin_id=pin_id)
        db.session.add(pin_detail)
        db.session.commit()
        db.create_all()
    else:
        print("Can't analysis image!")

##### SEARCH BY TAGS  #####
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