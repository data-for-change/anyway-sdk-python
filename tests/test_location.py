from anywaysdk.location import get_location_bounding_box, BoundingBox

def test_location():
    assert (get_location_bounding_box(location="מגדל משה אביב", distance_in_km=1) ==
            BoundingBox(lat_min=32.07476268394081, lon_min=34.793237286926555, lat_max=32.09274911605919, lon_max=34.814465913073455))
