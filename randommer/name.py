import requests
from .randommer import Randommer


class Name(Randommer):
    def get_name(self, api_key: str, nameType: str, quantity: int) -> list:
        '''get name

        Args:
            api_key (str): api key
            nameType (str): nameType
            quantity (str): number of names

        Returns:
            list: list of names
        '''
        url = 'https://randommer.io/api/Name'
        payload = {
            'nameType': nameType,
            'quantity': quantity
        }
        headers = {
            'X-Api-Key': api_key
        }

        response = requests.get(url, params=payload, headers=headers)
        return response.json()
    
    def get_name_suggestions(self, api_key: str, startingWords: str) -> list:
        '''get name suggestions

        Args:
            api_key (str): api key
            startingWords (str): startingWords

        Returns:
            list: list of name suggestions
        '''
        pass
    
    def get_name_cultures(self, api_key: str) -> list:
        '''get available cultures

        Args:
            api_key (str): api key

        Returns:
            list: list of names
        '''
        pass

# key = '9174cdd006f046029c4def5446299088'
# o = Name()
# print(o.get_name(key, 'fullname', 1))