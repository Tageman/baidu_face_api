# -*- coding:utf-8 -*-
# author:rxg
"""
requests api :
不要直接使用因为在里面有信息这边没有做马赛克掉
建议直接申请百度云之后自己申请信息

"""

from urllib import urlencode
import requests
import base64

class BaiDu_Face_API():

    def __init__(self,face_url,img_url,token_url,token_data):
        self.face_url = face_url     # face api url
        self.img_url = img_url    # img url localhost
        self.token_url = token_url  # get access token url
        self.token_data = token_data  # get token data


    def get_access_token(self):

        headers = {
            'Content-Type': 'application/json;charset=UTF-8'
        }
        access_token_response = requests.post(self.token_url, data=self.token_data, headers=headers)
        return access_token_response.json()['access_token']

    def get_img_base64(self):
        with open(self.img_url,'rb') as file:
            ls_f = base64.b64encode(file.read())
            return ls_f

    def requests_baidu_api(self):
        headers = {
            'Content-type': 'application/x-www-form-urlencoded'
        }
        face_params = {"face_fields":"age,beauty,expression,faceshape,gender,glasses,landmark,race,qualities","image":self.get_img_base64(),"max_face_num":1}
        params = urlencode(face_params)
        url = self.face_url + "?access_token=" + self.get_access_token()
        response = requests.post(url, data=params, headers=headers)
        print response.json()


if __name__ == '__main__':
    face_url = 'https://aip.baidubce.com/rest/2.0/face/v2/detect'
    img_url = '/Users/ydz/Desktop/test/baidu_face/Experiment/helo.jpg'
    token_url = 'https://aip.baidubce.com/oauth/2.0/token'
    token_data = {'grant_type': 'client_credentials', 'client_id': '8mYFHwy0MncggZIKr8uGrVVE','client_secret': 'EGBG1PSMBhBgCfdHgwYiaFGVOr1IS7sw'}
    BaiDu_Face_API(face_url,img_url,token_url,token_data).requests_baidu_api()
