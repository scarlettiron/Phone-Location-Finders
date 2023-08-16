import phonenumbers
from phonenumbers import geocoder

number = "+19123621020"

ch_number = phonenumbers.parse(number,"CH")
final = geocoder.description_for_number(ch_number, "en")

print(f"number: {final}")