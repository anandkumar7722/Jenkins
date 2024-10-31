# dark_web_scanner.py

import requests
from config import HIBP_API_KEY, USER_AGENT

class DarkWebScanner:
    @staticmethod
    def check_leaked_data(email):
        """
        Checks if the provided email has been involved in a breach by querying 
        the HaveIBeenPwned API.

        Args:
            email (str): The email to check for breaches.

        Returns:
            list: A list of breach data if found, otherwise an empty list.
        """
        url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
        headers = {
            'hibp-api-key': HIBP_API_KEY,
            'User-Agent': USER_AGENT
        }

        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                # Return the list of breaches for this email
                return response.json()
            elif response.status_code == 404:
                # No breaches found for this email
                return []
            else:
                # Handle other HTTP responses
                raise Exception(f"Unexpected status code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error contacting HaveIBeenPwned API: {e}")
            return []
