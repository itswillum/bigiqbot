
from commands import arguments
import requests

response = requests.get('http://flipacoinapi.com/json')
arguments.messageReturn = response.text.split('"')[1]
