import json
import requests
from const import SMS_URL, SMS_TOKEN
number = '998991717799'

text = 'Hello, it\'s Murad'
result = requests.post(SMS_URL, data={'token': SMS_TOKEN,
                             'sms_phone': number,
                             'sms_text': text})
print(result.json())
