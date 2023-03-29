from . import bot
from telebot import util
#from telebot.util.update_types import message,callback_query,my_chat_member,chat_member,chat_join_request
#import apscheduler
admin='741728025'
#from apscheduler.schedulers.background import BackgroundScheduler
#from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

#job_stores={'defualt':SQLAlchemyJobStore(url="mysql://root:H@r$hit1@localhost:3306/subscription", tablename="jobs")}

if __name__=="__main__":
    #schedule=BackgroundScheduler(job_stores=job_stores,demon=True,timezone="Asia/Kolkata")
    #schedule.add_job(func=tesks.reminder ,kwargs={'bot':bot},trigger='cron',hour='21',minute='36')
    #schedule.start()
    #print(schedule.get_jobs())
    bot.infinity_polling(allowed_updates=['message','callback_query','my_chat_member','chat_member'])
