import requests
import json
import time
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
pagesize = 15
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
}

posturl = "https://m.ctrip.com/restapi/soa2/13444/json/getCommentCollapseList?_fxpcqlniredt=09031154312127706587&x-traceID=09031154312127706587-1705910281365-1495736"


def getdata():
    with open("xiecheng.csv", "a", newline='', encoding="utf-8") as f:
        f.write('id')
        f.write("\t")
        f.write('评论')
        f.write("\n")
    j = 1
    for i in range(0, pagesize):
        request = {
            'arg': {'channelType': '2',
                    'collapseType': '0',
                    'commentTagId': '0',
                    'pageIndex': str(i),
                    'pageSize': '10',
                    'poiId': '10558849',
                    'sortType': '3',
                    'sourceType': '1',
                    'starType': '0'},

            'head': {'auth': "",
                     'cid': "09031154312127706587",
                     'ctok': "",
                     'cver': "1.0",
                     'extension': [],
                     'lang': "01",
                     'sid': "8888",
                     'syscode': "09",
                     'xsid': ""}
        }

        time.sleep(3)
        html = requests.post(posturl, data=json.dumps(request), headers=headers)
        html.encoding = "utf-8"
        html1 = json.loads(html.text)
        print('正在爬取第'+str(i+1)+'页')
        items = html1['result']['items']
        #保存文件
        with open("香港迪士尼.csv", "a", newline='', encoding="utf-8") as f:
            for k in items:
                # 处理评论
                pinlun = str(k['content']).replace('\n', '')
                f.write(str(k['commentId']))
                f.write("\t")
                f.write(pinlun)
                f.write("\n")
                j += 1


if __name__ == '__main__':
    getdata()
    # 读取CSV文件
    data = pd.read_csv('香港迪士尼.csv', encoding='utf-8', header=None, sep=None, engine='python')
    # 提取第一列数据
    column_data = data.iloc[:, 1]
    s = ''
    for i in column_data:
        s += str(i)

    wc = WordCloud()
    # 生成词云图像

    wc = WordCloud(font_path="C:\Windows\Fonts\Microsoft YaHei UI\msyh.ttc", width=500, height=400, mode="RGBA",
                   background_color=None).generate(s)
    # 显示词云图
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()
