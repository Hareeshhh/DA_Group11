# Use the Reuqest library
import requests
# Set the target webpage
url = 'https://brickset.com/sets/year-2008'
r = requests.get(url)
# This will get the full page
print(r.text)
