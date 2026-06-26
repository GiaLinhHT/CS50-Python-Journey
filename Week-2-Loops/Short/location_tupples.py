import sys
def main():
    coordinates_tupple = (42.376,-71.115)
    coordinates_list = [42.376,-71.115]
    latitude, longitude = coordinates_tupple
    print(f"Latitude:{coordinates_tupple[0]}")
    print(f"Latitude:{latitude}")
    print(f"Longitude:{coordinates_tupple[1]}")
    print(f"Longitude:{longitude}")
    print(f"{sys.getsizeof(coordinates_tupple)} bytes") #less use of data than using list 
    print(f"{sys.getsizeof(coordinates_list)} bytes")
#use list when u need to change your data, use tupple for more effcient of memory but cannot change data inside
main()