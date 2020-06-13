import requests
import time
from lxml import etree
from async_task.tasklist.biquge.tasks import crawl
from celery.result import AsyncResult
from async_task.main import app
def cc(url_list):
    for i in url_list:

        s="https://www.52bqg.com/book_127354/"+i
        print(s,'12')
        # time.sleep(0.1)
        res=crawl.delay(s)

        # print(res.id)
        # print(res.result)
        # print(res)
        # print(type(res))

        res=AsyncResult(id=res.id,app=app)

        #不能还未执行完成就拿到结果
        # time.sleep(1)
        # #拿到异步函数返回的结果
        # print(res.successful())
        print(res.get())


        # 异步获取任务返回值
        # for i in range(100):
        #     time.sleep(1)
        #     async_task = AsyncResult(id=res.id, app=app)
        #
        #     print("async_task.id", async_task.id)
        #     # 判断异步任务是否执行成功
        #     if async_task.successful():
        #         # 获取异步任务的返回值
        #         result = async_task.get()
        #         print(result)
        #         print("执行成功")
        #         break
        #     else:
        #         print("任务还未执行完成")



def start_message():
    res=requests.get("https://www.52bqg.com/book_127354/")
    res=res.content.decode("gbk")
    et=etree.HTML(res)
    r=et.xpath("//*[@id='list']/dl/dd//a/@href")
    return r
if __name__ == '__main__':
    s=start_message()
    cc(s)