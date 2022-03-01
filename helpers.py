from models import db, Pin, PinDetail
from azures.azure_cv import AzureComputerVision

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
def search_tag(keyword):
    pin_details = PinDetail.query.filter(PinDetail.tags.contains([keyword])).all()
    pins = [pin_detail.pin for pin_detail in pin_details]
    return pins