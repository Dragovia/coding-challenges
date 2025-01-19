def contains_non_alpha(city_name):
    for char in city_name:
        if not char.isalpha():
            return True
    return False


# Test
city_name = "New York2"
if contains_non_alpha(city_name):
    print(f"'{city_name}' contains characters outside the range A-Z and a-z.")
else:
    print(f"'{city_name}' only contains characters in the range A-Z and a-z.")