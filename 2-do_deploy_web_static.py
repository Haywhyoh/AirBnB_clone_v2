#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""


from fabric.api import run, put, env
import os.path as file_path
env.username = "ubuntu"
env.hosts['100.24.210.123', '3.235.24.154']


def de_deploy(archive_path):
    """distributes an archive to the web servers"""
    try:
        path = '/data/web_static/releases/'
        archive_file = archive_path.split('/')[-1]
        file_name = archive_file.split('.')[0]
        if not file_path.exists(archive_path):
            return False
        put(archive_path, '/tmp/')
        run("mkdir -p {}{}/".format(path, file_name))
        run("tar -xzf /tmp/{} -C {}{}/".format(archive_file, path, file_name))
        run("rm -f /tmp/{}".format(archive_file))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except FileExistsError:
        return False
