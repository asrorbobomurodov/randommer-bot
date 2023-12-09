import requests
from .randommer import Randommer


class Text(Randommer):
    def generate_LoremIpsum(self, api_key: str, loremType: str, type: str, number: int) -> str:
        '''Generate lorem ipsum

        Args:
            api_key (str): api key
            loremType (str): loremType (normal or bussines)
            type (str): type (words or paragraphs)
            number (int): number

        Returns:
            str: Lorem text
        '''
        
        url = f'{Randommer().get_url()}Text/LoremIpsum'

        payload = {
            'loremType': loremType,
            'type': type,
            'number': number
        }
        headers = {
            'X-Api-Key': api_key
        }

        response = requests.get(url, params=payload, headers=headers)
        return response.json()
    
# ob = Text()
# key = "9174cdd006f046029c4def5446299088"
# print(ob.generate_LoremIpsum(key, 'normal', 'words', 3))