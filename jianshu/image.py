# -*- coding: utf-8 -*-
'''
File Name: jianshu/image.py
Author: JackeyGao
mail: junqi.gao@shuyun.com
Created Time: 五  1/ 8 14:50:27 2016
'''
import requests, shutil, re, sys
from jianshu.settings import DEFAULT_REQUEST_HEADERS as headers
from jianshu.db import Image

reload(sys)
sys.setdefaultencoding('utf-8')

images = Image.select().execute()

def get_image_name(url):
    group = re.findall('\d+-\w+.\w+', url)
    if not group:
        return None
    image_name = group[0]
    if 'imageMogr' in image_name:
        image_name = image_name.replace('?imageMogr2', '.jpg')

    return image_name

def request_image(url):
    image_name = get_image_name(url)
    print(u"正在下载 %s" % image_name)
    try:
        response = requests.get(url, headers=headers, 
                    stream=True,
                    timeout=100
                   )
        if not response.status_code == 200:
            return False

        with open('output/images/%s' % image_name, 'w' ) as f:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, f)
        return True
    except Exception as e:
        print(u"下载失败 %s" % image_name)
        return False

def request_images():
    return map(request_image, [ i.url for i in images ])

if __name__ == '__main__':
    request_images()
