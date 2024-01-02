
from custom_components.recycle_app.api import FostPlusApi
api = FostPlusApi()

#print(api.get_zip_code(7540)) #7540-57081
#print(api.get_street('Rue des mésanges', '7540-57081')) #geodata.wallonie.be/id/streetname-7723545

print(api.get_recycling_parks("7540-57081", 3.386506, 50.623147, "fr"))