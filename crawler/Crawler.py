import json
import logging
import random
import time
from os import path
from typing import List
import requests
from PIL import Image
from crawler import constants
from crawler.ProfileResponse import ProfileResponse

logging.basicConfig(level=logging.DEBUG)


class Crawler:
    username: str
    enc_password: str
    userId: str
    session_cookies: dict = constants.LOGIN_COOKIES
    session_headers: dict = constants.LOGIN_HEADERS

    def __init__(self, username: str, enc_password: str):
        self.username = username
        self.enc_password = enc_password

    def save_session(self, sessionid: str, csrftoken: str):
        with open(f'session_{self.username}.json', 'w') as session:
            session.write(json.dumps({
                'csrftoken': csrftoken,
                'sessionid': sessionid
            }))

    def login_from_saved_session(self):
        if not path.exists(f'session_{self.username}.json'):
            logging.warning(f'Saved session for {self.username} not found')
            return False

        with open(f'session_{self.username}.json', 'r') as session:
            session = json.loads(session.read())
            self.session_cookies['sessionid'] = session['sessionid']
            self.session_cookies['csrftoken'] = session['csrftoken']
            logging.info(f'Logged from saved session of {self.username} with sessionid={session["sessionid"]}')

        return True

    def login(self, force=False):
        """
        Log into the instagram account
        :param force: Force the connection without trying to look at the saved session
        :param username: The username
        :param enc_password: The encrypted password, you can get it while you log into your account and inspect the loggin request
        :return:
        """

        if not force:
            if self.login_from_saved_session():
                return

        data = {
            'enc_password': self.enc_password,
            'username': self.username,
            'queryParams': '{}',
            'optIntoOneTap': 'false',
            'stopDeletionNonce': '',
            'trustedDeviceRecords': '{}',
        }

        response = requests.post(
            'https://www.instagram.com/accounts/login/ajax/',
            headers=constants.LOGIN_HEADERS,
            cookies=constants.LOGIN_COOKIES,
            data=data
        )

        self.session_cookies = response.cookies.get_dict()
        self.session_headers = constants.LOGIN_HEADERS
        self.session_headers['csrftoken'] = self.session_cookies.get('csrftoken')

        self.save_session(self.session_cookies.get('sessionid'), self.session_cookies.get('csrftoken'))

        if not self.session_cookies.get('sessionid'):
            raise Exception('Could not log into your account', response.json())

        logging.info(
            f'Logged as {self.username}, sessionid={self.session_cookies.get("sessionid")}, csrftoken={self.session_headers.get("csrftoken")}')

    def fetch_profile(self, username: str):
        """
        Fetch the profile of an instagram user
        :param username: The username of the user
        :return: The dict that contains all the user informations
        """

        params = {
            '__a': '1',
            '__d': 'dis',
        }

        response = requests.get(
            f'https://www.instagram.com/{username}/',
            headers=constants.LOGIN_HEADERS,
            params=params,
            cookies=self.session_cookies
        )

        datas: ProfileResponse = ProfileResponse.from_dict(response.json())

        if not datas.graphql.user:
            raise Exception(f"Couldn't fetch {username} profile")

        return datas.graphql.user

    def get_user_id(self, username: str):
        profile = self.fetch_profile(username)
        return profile.id

    def post_image(
            self,
            image_path: str,
            caption: str = '',
            tags: List[str] = [],
            disable_comments: bool = False
    ):
        """
        Post an image on your instagram account
        :param image_path: That relative path to your image
        :param caption: Your image caption
        :param disable_comments: Disable the comment on your post
        :return:
        """

        upload_id = int(time.time() * 1000)
        width = 1024
        height = 1024

        try:
            image_file = open(image_path, "rb")
            image_data = image_file.read()
            image_pil = Image.open(image_file)
            width = image_pil.width
            height = image_pil.height
            image_len = str(len(image_data))
        except Exception as e:
            raise e

        upload_headers = constants.LOGIN_HEADERS | {
            'offset': '0',
            'content-type': 'image/jpeg',
            'content-length': image_len,
            'x-entity-length': image_len,
            'x-entity-name': f'fb_uploader_{upload_id}',
            'x-entity-type': 'image/jpeg',
            'x-instagram-rupload-params': json.dumps({
                "media_type": 1,
                "upload_id": upload_id,
                "upload_media_height": height,
                "upload_media_width": width
            }),
        }

        response = requests.post(
            f'https://i.instagram.com/rupload_igphoto/fb_uploader_{upload_id}',
            headers=upload_headers,
            cookies=self.session_cookies,
            data=image_data
        )

        if 'upload_id' not in response.json():
            raise Exception("Image could't be uploaded", response.json())

        usertags = [
            {
                'position': [random.random(), random.random()],
                'user_id': self.get_user_id(tag)
            } for tag in tags
        ]

        data = {
            'source_type': 'library',
            'caption': caption,
            'upcoming_event': '',
            'upload_id': upload_id,
            'usertags': json.dumps({'in': usertags}) if len(usertags) > 0 else '',
            'custom_accessibility_caption': '',
            'disable_comments': '1' if disable_comments else '0',
            'like_and_view_counts_disabled': '0',
            'igtv_ads_toggled_on': '',
            'igtv_share_preview_to_feed': '1',
            'is_unified_video': '1',
            'video_subtitles_enabled': '0',
        }

        configure_headers = constants.LOGIN_HEADERS | {
            'x-csrftoken': self.session_cookies.get('csrftoken')
        }

        response = requests.post(
            'https://i.instagram.com/api/v1/media/configure/',
            headers=configure_headers,
            cookies=self.session_cookies,
            data=data
        )

        if 'media' in response.json():
            logging.info(f"Imaged uploaded at https://www.instagram.com/p/{response.json()['media']['code']}/")
        else:
            raise Exception("Image could't be uploaded", response.json())

        return response.json()
