# -*- coding: utf-8 -*-

import os
import shlex
import shutil
import sys
import datetime

from invoke import task
from invoke.main import program
from invoke.util import cd
from pelican import main as pelican_main
from pelican.server import ComplexHTTPRequestHandler, RootedHTTPServer
from pelican.settings import DEFAULT_CONFIG, get_settings_from_file

OPEN_BROWSER_ON_SERVE = True
SETTINGS_FILE_BASE = 'pelicanconf.py'
SETTINGS = {}
SETTINGS.update(DEFAULT_CONFIG)
LOCAL_SETTINGS = get_settings_from_file(SETTINGS_FILE_BASE)
SETTINGS.update(LOCAL_SETTINGS)

CONFIG = {
    'settings_base': SETTINGS_FILE_BASE,
    'settings_publish': 'publishconf.py',
    # Output path. Can be absolute or relative to tasks.py. Default: 'output'
    'deploy_path': SETTINGS['OUTPUT_PATH'],
    # Github Pages configuration
    'github_pages_branch': 'main',
    'commit_message': "'Publish site on {}'".format(datetime.date.today().isoformat()),
    # Host and port for `serve`
    'host': 'localhost',
    'port': 8000,
}

@task
def clean(c):
    """Remove generated files"""
    if os.path.isdir(CONFIG['deploy_path']):
        shutil.rmtree(CONFIG['deploy_path'])
        os.makedirs(CONFIG['deploy_path'])
    if os.path.exists('artifact.tar'):
        os.remove('artifact.tar')

@task
def build(c):
    """Build local version of site"""
    pelican_run('-d -s {settings_base}'.format(**CONFIG))
    c.run('sass theme/scss/main.scss theme/static/css/main.css')


@task
def serve(c):
    """Automatically reload browser tab upon file modification."""
    from livereload import Server

    def cached_build():
        #cmd = '-s {settings_base} -e CACHE_CONTENT=true LOAD_CONTENT_CACHE=true'
        #pelican_run(cmd.format(**CONFIG))
        build(c)

    cached_build()
    server = Server()
    theme_path = SETTINGS['THEME']
    watched_globs = [
        CONFIG['settings_base'],
        '{}/templates/**/*.html'.format(theme_path),
        '{}/scss/*.scss'.format(theme_path),
        # We explicitly don't want the *.css files here, as they should not
        # be edited directly.
        "{}/static/**/*.js".format(theme_path),
    ]

    content_file_extensions = ['.md', '.rst']
    for extension in content_file_extensions:
        content_glob = '{0}/**/*{1}'.format(SETTINGS['PATH'], extension)
        watched_globs.append(content_glob)

    for glob in watched_globs:
        server.watch(glob, cached_build)

    if OPEN_BROWSER_ON_SERVE:
        # Open site in default browser
        import webbrowser
        webbrowser.open("http://{host}:{port}".format(**CONFIG))

    server.serve(host=CONFIG['host'], port=CONFIG['port'], root=CONFIG['deploy_path'])


@task
def artifact(c):
    """Build and upload a github actions artifact.
    
    This task should only be used in the Github Actions to build a tarball
    that will serve as the content for the github pages site.
    """
    pelican_run('-s {settings_publish}'.format(**CONFIG))
    c.run(
        'cd output && '
        'tar --dereference -cvf "../artifact.tar" --exclude=.git --exclude=.github . && '
        'cd ..'
        )

def pelican_run(cmd):
    cmd += ' ' + program.core.remainder  # allows to pass-through args to pelican
    pelican_main(shlex.split(cmd))