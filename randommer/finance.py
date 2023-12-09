import requests
from .randommer import Randommer

class Finance(Randommer):
    def get_crypto_address_types(self, api_key: str) -> list:
        '''get available crypto types

        Args:
            api_key (str): api key

        Returns:
            list: list of types
        '''
        
        url = 'https://randommer.io/api/Finance/CryptoAddress/Types'

        headers = {
            "X-Api-Key": api_key
        }

        r = requests.get(url, headers=headers)
        return r.json()

    def get_crypto_address(self, crypto_type: str, api_key: str) -> dict:
        '''get available crypto address

        Args:
            crypto_type (str): crypto type
            api_key (str): api key

        Returns:
            dict: crypto address
        '''
        url = self.get_url() + 'Finance/CryptoAddress'
        payload = {
            'cryptoType': crypto_type
        }
        headers = {
            'X-Api-Key': api_key
        }

        response = requests.get(url, params=payload, headers=headers)
        return response.json()

    def get_countries(self, api_key: str) -> list:
        '''get available countries

        Args:
            api_key (str): api key

        Returns:
            list: crypto address
        '''
        pass

    def get_iban_by_country_code(self, country_code: str, api_key: str) -> dict:
        '''get available countries

        Args:
            country_code (str): country code
            api_key (str): api key

        Returns:
            dict: idan data
        '''
        pass

# f = Finance()
# lst = f.get_crypto_address_types('9174cdd006f046029c4def5446299088')
# print(type(lst))