from flask import Flask, request
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/time_remaining")
def calculate_time():
    date_format = "%Y-%m-%d %H:%M:%S"
    target_time = request.args.get('target_time')
    print(target_time)
    target_date = datetime.strptime(target_time, date_format).date()
    current_time = datetime.now()
    time_difference = calculate_time_diff(current_time, target_date)
    hours = time_difference.seconds // 3600
    minutes = (time_difference.seconds // 60) % 60
    return "距离指定时间还有 " + hours + " 小时 " + minutes + " 分钟"


def calculate_time_diff(start_time, target_time):
    time_difference = target_time - start_time
    return time_difference
