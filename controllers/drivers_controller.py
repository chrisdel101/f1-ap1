from models import driver_model
from utilities import utils
from slugify import slugify


# make data into arr of dicts
def make_slug_dict(arr):
    result_arr = []
    for item in arr:
        d = {
            'name': str(item.driver_name),
            'name_slug': slugify(str(item.driver_name).lower())
        }
        result_arr.append(d)
    return result_arr


def show_all_drivers():
    arr = driver_model.Driver.query.all()
    return make_slug_dict(arr)


def show_single_driver(name_slug):
    try:
        driver = vars(driver_model.Driver.query.filter_by(
            name_slug=str(name_slug)).first())
        return utils.serialize_row(driver)
    except Exception as e:
        print('error in driver_controller.show_single_driver', e)
