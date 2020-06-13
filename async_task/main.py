
from celery import Celery



app=Celery("biquge",broker="redis://127.0.0.1:6379/3",backend="redis://127.0.0.1:6379/4")


# #加载配置
# app.config_from_object("async_task.config")

#加载任务
app.autodiscover_tasks(["async_task.tasklist.biquge"])

#  celery -A mycelery.main worker --loglevel=info -P eventlet