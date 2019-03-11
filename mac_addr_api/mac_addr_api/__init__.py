import os
from flask import Flask
from threading import Thread
import sys
from . import api

app = Flask(__name__, instance_relative_config=True)

try:
    os.makedirs(app.instance_path)
except OSError:
    pass

app.register_blueprint(api.bp)

try:
    thr = Thread(target=api.update_macdb)
    thr.daemon = True
    thr.start()
except (KeyboardInterrupt, SystemExit):
    sys.exit()
