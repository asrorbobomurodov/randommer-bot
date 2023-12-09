import requests
from .randommer import Randommer

class Phone(Randommer):
    def generate(self, api_key: str, CountryCode: str, Quantity: int) -> list:
        '''get bulk telephone numbers for a country

        Args:
            api_key (str): api key
            CountryCode (str): CountryCode ex: 'uz'
            Quantity (str): Quantity

        Returns:
            list: list of phone numbers
        '''
        url = 'https://randommer.io/api/Phone/Generate'

        payload = {
            "CountryCode": CountryCode,
            "Quantity": Quantity
        }
        headers = {
            'X-Api-Key': api_key
        }

        r = requests.get(url, params=payload, headers=headers)

        return r.json()
    
    def get_IMEI(self, api_key: str, Quantity: int) -> list:
        '''get bulk imei

        Args:
            api_key (str): api key
            Quantity (str): Quantity

        Returns:
            list: list of phone numbers
        '''
        pass
    
    def is_valid(self, api_key: str, telephone: str, CountryCode: str) -> bool:
        '''get bulk imei

        Args:
            api_key (str): api key
            telephone (str): phone number
            CountryCode (str): CountryCode ex: 'uz'

        Returns:
            bool: is valid
        '''
        pass
    
    def get_countries(self, api_key: str) -> list:
        '''get countries

        Args:
            api_key (str): api key

        Returns:
            list: lsit of countries
        '''
        pass

# ob = Phone()
# key = '9174cdd006f046029c4def5446299088'
# print(ob.generate(key, 'uz', 5))
