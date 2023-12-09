import requests
from .randommer import Randommer


class SocialNumber(Randommer):
    def get_SocialNumber(self, api_key: str) -> str:
        '''get SocialNumber

        Args:
            api_key (str): api key

        Returns:
            str: number as str
        '''
        url = 'https://randommer.io/api/SocialNumber'
        headers = {
            'X-Api-Key': api_key
        }
        r = requests.get(url, headers=headers)
        return r.json()
    
# ob = SocialNumber()
# key = '9174cdd006f046029c4def5446299088'
# print(ob.get_SocialNumber(key))
