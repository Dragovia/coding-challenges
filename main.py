import re
def has_non_alpha_char(city_name):
  """Detects if a city_name includes characters outside of the a-z and A-Z ranges."""
  if re.search(r'[^a-zA-Z]', city_name):
    return True
  else:
    return False
# Example usage
city_name = "San José"
if has_non_alpha_char(city_name):
  print("The city name contains a non-alphabetical character.")
else:
  print("The city name contains only alphabetical characters.")