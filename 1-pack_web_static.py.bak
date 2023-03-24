#!/usr/bin/python3
"""
Fabric script to generate a .tgz archive
execute: fab -f 1-pack_web_static.py do_pack
"""

from fabric.api import local
import datetime as dt
import os


def do_pack():
    """
    Making an archive on web_static folder
    """

    local("mkdir -p versions")
    d = dt.datetime.now()
    name = f"versions/web_static_{d.year}{d.month}{d.day}"\
           + f"{d.hour}{d.minute}{d.second}.tgz"
    local("tar cvfz {} web_static".format(name))
    if os.path.exists(name):
        return os.path.abspath(name)
