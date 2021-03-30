import mr4mp

from time import sleep
from flask import Flask
from progress import Progress

app = Flask(__name__)

progress = Progress(stages=333)


def m(x):
    sleep(0.05)
    return [x[0]*2]


@app.route('/status')
def get_status():
    html = '<meta http-equiv="refresh" content="50">' \
           '%s%%' \
           '<div style="width: 100%%; background-color: #ddd;">' \
           '<div style="width: %s%%; height: 20px; background-color: #bc0">' \
           '</div></div>' \
        % tuple([progress]*2)
    return html, 206


@app.route('/start')
def start():

    xs = [[x0] for x0 in range(0, 1000)]

    pool = mr4mp.pool()
    result = pool.mapconcat(m, xs, progress=progress.hook, stages=progress.stages)
    pool.close()

    html = '<pre>' + str(result) + '</pre>'
    return html, 200
