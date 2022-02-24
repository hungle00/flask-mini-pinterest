from app import db, app
from models import db, Pin, PinDetail, User
db.app = app
db.init_app(app)

from azures.azure_cv import AzureComputerVision
# from azures.storage import BlobStorage

# blob_storage = BlobStorage()
# images = blob_storage.get_blob_items()
# for image in images:
#     this_pin = Pin(image_url=image, pin_by=User.query.first())
#     db.session.add(this_pin)
#     db.session.commit()

#print(images)

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

pins = Pin.query.all()
for pin in pins:
    #print(pin.to_json())
    pin_detail = pin.to_json()['pin_detail']
    if pin_detail is not None:
        print(pin_detail)
    if pin_detail is None:
        create_pin_detail(pin.id)


#create_pin_detail(1)