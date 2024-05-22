from test import number
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

check_phonenum_country = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(check_phonenum_country, "en"))

check_carries = phonenumbers.parse(number)
print(carrier.name_for_number(check_carries, "en"))