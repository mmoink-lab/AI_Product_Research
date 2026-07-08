"""
HTTP Client
Production v1
"""

import time
import requests


class HttpClient:

    def __init__(self):

        self.session = requests.Session()

        self.session.headers.update({

            "User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 "
                "(KHTML, like Gecko) "
                "Chrome/138.0 Safari/537.36"

        })

    def get(self, url, params=None, timeout=30):

        response = self.session.get(

            url,

            params=params,

            timeout=timeout

        )

        response.raise_for_status()

        time.sleep(1)

        return response.text

    def close(self):

        self.session.close()