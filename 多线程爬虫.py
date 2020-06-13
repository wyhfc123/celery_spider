

from threading import Thread
import requests
from queue import Queue
from lxml import etree
import time
def a(fist_q,url):
    res=requests.get(url)
    et=etree.HTML(res.content.decode("gbk"))
    urls=et.xpath("//*[@id='main']//a/@href")
    for i in urls:
        time.sleep(0.01)
        fist_q.put(i)
        # print("已放入%s"%i)
def b(fist_q,second_q):
    while True:
        time.sleep(0.01)
        res=fist_q.get()
        # print(res)
        # print("已拿到%s" % res)
        resp=requests.get(res)
        resp = resp.content.decode("gbk")
        et = etree.HTML(resp)
        r = et.xpath("//*[@id='list']/dl/dd//a/@href")
        for i in r:
            # print(res+i,'28')
            url=res+i
            second_q.put(url)
            # print( "已放入%s" % url)
def c(second_q):
    while True:
        url=second_q.get()
        # print("已拿到%s" % url)
        # print(url)
        res = requests.get(url)
        et = etree.HTML(res.content.decode("gbk"))
        content = et.xpath("//*[@id='content']/text()")
        s = ""
        for i in content:
            s += i.strip()
        print(s)









if __name__ == '__main__':
    first_q=Queue(2)
    second_q=Queue(2)
    t1=Thread(target=a,args=(first_q,"https://www.52bqg.com/",))
    t2=Thread(target=b,args=(first_q,second_q,))
    t3=Thread(target=c,args=(second_q,))

    t1.start()
    t2.start()
    t3.start()
    t1.join()











