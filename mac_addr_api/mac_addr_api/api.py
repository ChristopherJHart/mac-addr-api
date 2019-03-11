from flask import Blueprint, request, Flask
from manuf import manuf
import time
import sys

bp = Blueprint("api", __name__, url_prefix="/api")
mp = manuf.MacParser(update=True)
app = Flask(__name__)

@bp.route("/<mac>", methods=["GET",])
def mac_lookup(mac):
    if request.method == "GET":
        return mp.get_all(mac)

@bp.route("/manufacturer/<mac>", methods=["GET",])
def mac_lookup_manufacturer(mac):
    if request.method == "GET":
        return mp.get_manuf(mac)

@bp.route("/comment/<mac>", methods=["GET",])
def mac_lookup_comment(mac):
    if request.method == "GET":
        comment = mp.get_comment(mac)
        if comment:
            return comment
        else:
            return ("", 204)

def update_macdb():
    while True:
        app.logger.info("Updating MAC address database...")
        mp.update()
        app.logger.info("MAC address database update successful!")
        time.sleep(86400)