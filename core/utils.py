import requests

from typing import Optional


class APIConnector:
    """
    Base for 3rd Party API Connector
    """
    def __init__(self, auth_token: str, auth_token_key: str):
        if auth_token:
            self.__AUTH_TOKEN = auth_token
        else:
            raise ValueError("Authentication token is missing")

        if auth_token_key:
            self.__AUTH_TOKEN_KEY = auth_token_key
        else:
            raise ValueError("Authentication token key is missing")

    def __get_header(self, bearer: Optional[bool] = False) -> dict:
        """
        Method for manipulating API Header

        :return: authentication header
        """
        if bearer:
            return {
                str(self.__AUTH_TOKEN_KEY): 'Bearer ' + self.__AUTH_TOKEN,
                'Content-Type': 'application/json'
            }
        return {
            str(self.__AUTH_TOKEN_KEY): self.__AUTH_TOKEN,
            'Content-Type': 'application/json'
        }

    def get(self, api_url: str, params: Optional[dict] = None, bearer: Optional[bool] = False) -> dict:
        """
        Base/Main GET method for performing GET requests.

        :param api_url: API Endpoint
        :param bearer: Token Type
        :param params: (Optional) API Request parameters in Dictionary Format

        :return:
        """
        return requests.get(
            url=api_url,
            headers=self.__get_header(bearer=bearer),
            params=params,
        ).json()

    def post(self, api_url: str, data: Optional[dict] = None, bearer: Optional[bool] = False) -> dict:
        """
        Base/Main POST method for performing POST requests.

        :param api_url: API Endpoint
        :param bearer: Token Type
        :param data: (Optional) API Request Body containing data parameters in Dictionary Format

        :return:
        """
        header = self.__get_header(bearer=bearer)

        api_response = requests.post(
            url=api_url,
            headers=header,
            json=data,
        )

        if api_response.status_code == 200:
            return {
                "status": True,
                "data": api_response.json()
            }

        return {
                "status": False,
                "reason": str(api_response.status_code) + ' from API. ' + str(api_response.text),
                }

    def delete(self, api_url: str, parameter: Optional[dict] = None) -> dict:
        """
        Base Delete method for the APIs'.
        :param parameter:
        :param api_url:
        :return:
        """
        header = self.__get_header()
        params = parameter

        api_response = requests.delete(
            url=api_url,
            headers=header,
            params=params
        )

        if api_response.status_code == 200:
            response = {
                "status": True,
                "data": api_response.json()
            }
        else:
            response = {
                "status": False,
                "reason": str(api_response.status_code) + ' from API',
            }

        return response
