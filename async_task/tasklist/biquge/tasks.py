from async_task.main import app
from lxml import etree
import requests
@app.task(name="crawl")
def crawl(url):
    res=requests.get(url)
    et=etree.HTML(res.content.decode("gbk"))
    content=et.xpath("//*[@id='content']/text()")
    print(content,"9**********************")
    s=""
    for i in content:
        s+=i.strip()

    return s
