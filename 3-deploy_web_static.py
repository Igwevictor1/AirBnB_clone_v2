#!/usr/bin/python3
"""
Fabric script to genereate tgz archive and deploy
execute: fab -f 3-deploy_web_static.py deploy -i my_ssh_private_key -u ubuntu
"""

from datetime import datetime
from fabric.api import *
from os.path import exists, isdir


env.hosts = ['34.239.160.19', '34.231.243.196']


def do_pack():
    """
    making an archive on web_static folder
    """

    time = datetime.now()
    archive = 'versions/web_static_' + time.strftime("%Y%m%d%H%M%S") + '.tgz'
    local('mkdir -p versions')
    if isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(archive)).failed is True:
        return None
    return archive


def do_deploy(archive_path):
    """
    deploying an archive to a server
    """
    if not exists(archive_path):
        return False
    try:
        archive_fname = archive_path.split('/')[-1]
        basename = archive_fname.split('.')[0]
        if put(archive_path, '/tmp/').failed:
            return False
        if run('mkdir -p /data/web_static/releases/{}'.format(
                    basename)).failed:
            return False
        if run(('tar -xzf /tmp/{0}.tgz -C /data/web_static/releases' +
                '/{0}').format(basename)).failed:
            return False
        if run(('mv /data/web_static/releases/{0}/web_static/* ' +
                '/data/web_static/releases/{0}/').format(basename)).failed:
            return False
        if run('rm -rf /data/web_static/releases/{}/web_static'.format(
                                                      basename)).failed:
            return False
        if run('rm -f /tmp/{}'.format(archive_fname)).failed:
            return False
        if run('rm -f /data/web_static/current').failed:
            return False
        if run(('ln -s /data/web_static/releases/{}' +
                ' /data/web_static/current').format(basename)).failed:
            return False
        return True
    except Exception:
        return False


def deploy():
    """
    deploying on the servers
    """
    file_name = do_pack()
    if file_name is None:
        return False
    else:
        return do_deploy(file_name)
