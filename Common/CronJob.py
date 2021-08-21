from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler

num =0
def job_func():
    num+1
    print("hello World")



if __name__ == '__main__':
    sched = BlockingScheduler()
    print(1)
    sched.add_job(job_func, 'interval', seconds=10)
    



