import sqlalchemy.exc
from flask_apscheduler import APScheduler
import psutil
from datetime import datetime
from app import app
from database import db, Performance

scheduler = APScheduler()


@scheduler.task("cron", id="save_performance", minute="*")
def save_performance():
    parameters = Performance(date=str(datetime.now()), memory_usage=psutil.virtual_memory()[2],
                             CPU_usage=psutil.cpu_percent(), disk_usage=psutil.disk_usage('/')[3])
    with app.app_context():
        try:
            db.session.add(parameters)
            db.session.commit()
            print("Performance saved!")
        except sqlalchemy.exc.IntegrityError:
            print("sqlalchemy.exc.IntegrityError -UNIQUE constraint failed: performance.date!")


scheduler.init_app(app)
scheduler.start()
