from settings import URL, API_KEY, card_msg, welcome
from getUpdates import getUpdates
from time import sleep
import requests
import random

def bot(chat_id: str, text: str, parse_mode = "HTML"):
    url = f'{URL}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': text,
        'parse_mode': parse_mode
    }
    headers = {
        'X-Api-Key': API_KEY
    }
    r = requests.get(url, params=params, headers=headers)
    return r.json()
id = -1

while True:
    ldata = getUpdates()
    update_id = ldata['update_id']

    if id != update_id:
        chat_id = ldata['message']['chat']['id']
        text = ldata['message']['text']

        if text == '/start':
            bot(chat_id, welcome)

        elif text == '/card':
            from randommer.card import Card
            from dateutil import parser
            card = Card()
            reply = card.get_card(API_KEY)
            datetime_object = parser.parse(reply['date'])
            msg = card_msg.format(
                type=reply['type'],
                name = reply['fullName'],
                number = reply['cardNumber'],
                cvv = reply['cvv'],
                pin = reply['pin'],
                date = datetime_object.strftime('%Y-%m-%d')
                )
            bot(chat_id, msg)

        elif text == '/finance':
            from randommer.finance import Finance
            fi = Finance()
            crypto_types = fi.get_crypto_address_types(API_KEY)
            random_crypto = random.choice(crypto_types)
            crypto = fi.get_crypto_address(random_crypto, API_KEY)
            msg = f'📍Crypto address: {crypto.get("address")} \n\n💵Type: {crypto["type"]}'
            bot(chat_id, msg)

        elif text == '/misc':
            from randommer.misc import Misc
            m = Misc()
            miscs = m.get_cultures(API_KEY) #dicts in list 
            randomly = random.choice(miscs)
            code = randomly['code']
            topic = m.get_random_address(api_key=API_KEY, number=5, culture=code)
            msg = f'🗺<b>Please of Culture:</b> {randomly["name"]}\n\
<b>🌐Culture code:</b> {code} \n\n\
 <b><i>Addresses:</i></b>\n\n\
     1️⃣ {topic[0]} \n\n\
     2️⃣ {topic[1]} \n\n\
     3️⃣ {topic[2]} \n\n\
     4️⃣ {topic[3]} \n\n\
     5️⃣ {topic[4]} \n              ______________________'
            bot(chat_id=chat_id, text=msg)

        elif text == '/name':
            from randommer.name import Name
            ob = Name()
            name = ob.get_name(API_KEY, 'fullname', 1)[0]
            msg = f'👤<b>Fullname:</b> {name}'
            bot(chat_id=chat_id, text=msg)

        elif text == '/phone':
            from randommer.phone import Phone
            ob = Phone()
            ph_numbers = ob.generate(API_KEY, 'uz', 5)
            msg = f"<b> 5 random phone numbers </b> \n\n\
 📞 🇺🇿{ph_numbers[0]} \n\n\
 📞 🇺🇿{ph_numbers[1]} \n\n\
 📞 🇺🇿{ph_numbers[2]} \n\n\
 📞 🇺🇿{ph_numbers[3]} \n\n\
 📞 🇺🇿{ph_numbers[4]} \n        …… ……………… …… \
        "
            bot(chat_id, msg)

        elif text == '/social_number':
            from randommer.social_number import SocialNumber
            ob = SocialNumber()
            social_number = ob.get_SocialNumber(API_KEY)
            msg = f'📟<b>Generate a social \n\
    security number:</b>\n\n<pre> {social_number} </pre>'
            bot(chat_id, msg)

        elif text == '/text':
            from randommer.text import Text
            ob = Text()
            text = ob.generate_LoremIpsum(API_KEY, 'business', 'words', 34)
            msg = f'<b><em>📩 Lorem Ipsum message: </em></b>\n\n\ {text}'
            bot(chat_id, msg)
        
        else:
            bot(chat_id, '😞 Oh no. For information, use the menus below: \n /start,  /card,  /finance,  /misc,  /name, \n /phone,  /social_number,  /text')

        id = update_id

    sleep(0.7)
