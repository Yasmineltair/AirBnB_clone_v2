#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive 
from the contents of the web_static folder 
of your AirBnB Clone repo, using the function do_pack.
"""
from os.path import isdir
from fabric.api import local
from datetime import datetime


def do_pack():
    """ pack function """
    try:
        Date_And_Time = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        Archive_path = "versions/web_static_{}.tgz".format(Date_And_Time)
        local("tar -cvzf {} web_static".format(Archive_path))
        return Archive_path
    except:
        return None
