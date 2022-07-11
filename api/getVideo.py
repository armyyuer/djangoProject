import os
import requests
import re
import time
#视频视频地址
pathUrl = 'https://vip3.lbbf9.com/20220531/yhCfpgVt/700kb/hls/index.m3u8'
#整个文件夹装
dir = "./dpcq/"

if not os.path.exists(dir):
    os.makedirs(dir)


def getVideo():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
    }
    res = requests.get(pathUrl, headers=headers)
    res.encoding = res.apparent_encoding
    #拿取视频的全部路径列表
    urlList = re.findall(r'\n(.*\.ts)', res.text)
    # print(urlList)
    print(len(urlList))
    count = 0
    count2 = "0"
    for item in urlList:
    #慢慢拿取，假装人为，一共395个文件，没加sleep，我只拿取了170个，加了全拿下来了
        if item[0]=="h":
            item=item
        else:
            item="https://vip3.lbbf9.com"+item
        print(item)
        time.sleep(6)
        count += 1
        res2 = requests.get(item, stream=True, headers=headers)
        res2.encoding = res2.apparent_encoding
        # print(item)
        print(res2.status_code)
        if count<100:
            if count<10:
                count2="00"
            else:
                count2="0"
        else:
            count2="0"
        with open(dir + 'demo{}.mp4'.format(count2+str(count)), "wb") as mp4:
        #边拿边从内存写到硬盘里
            for chunk in res2.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    mp4.write(chunk)


if __name__ == '__main__':
    getVideo()

