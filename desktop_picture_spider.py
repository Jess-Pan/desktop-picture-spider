from urllib import request
import requests
from lxml import etree
import os

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
    'Referer': 'http://simpledesktops.com/browse/'
}

pictures = []


def get_page(url, header):
    text = requests.get(url, headers=header)
    page = text.content.decode('utf-8')

    return page


def syncHtml(page):
    html = etree.HTML(page)
    imgs = html.xpath('//img[@src]')
    for img in imgs:
        title = format(img.xpath('./@title'))[2:-2].split(' ')[0]
        url = format(img.xpath('./@src')).split('.')
        src1 = format(url[0] + '.' + url[1] + '.' + url[2] + '.' + url[3])
        src = src1.split('\'')[1]
        type = format("." + url[3])

        picture = {
            'title': title,
            'src': src,
            'type': type
        }
        pictures.append(picture)

    return pictures


if __name__ == '__main__':

    for i in range(1, 21, 1):
        page = get_page(url='http://simpledesktops.com/browse/' + format(i) + "/", header=header)
        pictures = syncHtml(page)
        print("已成功爬取第" + format(i) + "页内容！")
        for picture in pictures:

            imgName = format("%s" % picture['title']).replace('/', '')
            if os.path.exists(format(
                    'C:\\Users\\27414\\Pictures\\Saved Pictures\\' + "%s" % picture['title'] + "%s" % picture["type"])):
                print("%s" % picture['title'] + " 已存在 :)")
            else:
                print("当前正在下载 " + imgName + ", 请稍后... ...")
                request.urlretrieve("%s" % picture["src"], format(
                    'C:\\Users\\27414\\Pictures\\Saved Pictures\\' + imgName + "%s" % picture["type"]))
                print(imgName + " 下载完成！")

