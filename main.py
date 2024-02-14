import phonenumbers
from phonenumbers import geocoder, carrier, timezone

print("Welcome clown")
entered_num = input("please enter a phoen number: ")
#create phonenumbers object
phone_num = phonenumbers.parse(entered_num, None)
print(phone_num)
#you might want to get some information about the location that corresponds to a phone number
print(geocoder.description_for_number(phone_num, "en"))
# for mobile numbers in some countries,
# you can also find out information about which carrier originally owned a phoen number
print(carrier.name_for_number(phone_num, "e"))
# you might also be able to retrieve a list of time zone names that the number potentially belongs to
print(timezone.time_zones_for_number(phone_num))







