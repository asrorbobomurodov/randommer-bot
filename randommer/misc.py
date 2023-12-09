import requests
from .randommer import Randommer


class Misc(Randommer):
    def get_cultures(self, api_key: str) -> list:
        '''get available misc cultures

        Args:
            api_key (str): api key

        Returns:
            list: list of cultures
        '''
        url = 'https://randommer.io/api/Misc/Cultures'
        headers = {
            "X-Api-Key": api_key
        }
        r = requests.get(url, headers=headers)
        return r.json()
    
    def get_random_address(self, api_key: str, number: int, culture='en') -> list:
        '''get available misc cultures

        Args:
            api_key (str): api key
            number (str): number
            culture (str): culture

        Returns:
            list: random address
        '''
        url = 'https://randommer.io/api/Misc/Random-Address'

        headers = {
            'X-Api-Key': api_key
        }

        payload = {
            'number': number,
            'culture': culture
        }
        response = requests.get(url, params=payload, headers=headers)
        return response.json()

# m = Misc()
# key = '9174cdd006f046029c4def5446299088'
# print(m.get_random_address(key, 5))