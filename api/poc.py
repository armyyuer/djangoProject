# 菜鸟程序员：阿米
import requests
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
    "Cookie": "csrftoken=6Fr3EowxWG2ZJ5hbMQ7rGMyM4BYLRJz3zVpsHa3EJM0T4YfQvhWau6pyqg3nW48N"
}
url = input("监测地址：")
r = requests.get(url, headers=headers)
res = r.content
print(res)
