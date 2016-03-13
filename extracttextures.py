#!/usr/bin/env python

import os, glob, sys, io, builtins
import json, pprint, pathlib

from subprocess import Popen, PIPE

_W3_LUA_MODULES = r"/home/alfi238/src/Lua-utils-for-Witcher-3/"
_W3_PATH = r"C:\Program Files (x86)\R.G. Games\The Witcher 3 Wild Hunt"
_TARGET_PATH = r"/media/alfi238/VOL_3B/ubuntu1510_os"


def unpack_all_textures_for_maps(w3luautilpath='/home/alfi238/src/Lua-utils-for-Witcher-3/',
                                 w3_path='/media/alfi238/WIN_10_SYSTEM/Program Files (x86)/R.G. Games/The Witcher 3 '
                                         'Wild Hunt/',
                                 outdir='/media/alfi238/VOL_3B/ubuntu1510_os/'):
    assert os.path.exists(w3luautilpath) and os.path.isdir(w3luautilpath), \
        'require a valid directory path to witcher 2/3 lua utils'
    assert os.path.exists(w3_path) and os.path.isdir(w3_path), \
        'require a path to witcher 2/3 install directory.'
    assert os.path.exists(outdir) and os.path.isdir(outdir), \
        'require a output directory path.'

    w3luautilpath = os.path.dirname(w3luautilpath)
    paths = os.environ['PATH']
    os.environ['PATH'] = paths + ':%s' % w3luautilpath

    env_names = os.environ.keys()

    if env_names.__contains__('PYTHONPATH'):
        pythonpaths = os.environ['PYTHONPATH']
        os.environ['PYTHONPATH'] = pythonpaths + ':%s' % w3luautilpath
    else:
        os.environ['PYTHONPATH'] = w3luautilpath

    _outdir = os.path.join(outdir, 'witcher3textures')
    if not os.path.exists(_outdir):
        os.mkdir(_outdir)

    outdir = _outdir

    texturecaches = glob.glob(os.path.dirname(w3_path) + '/**/texture.cache', recursive=True)

    texcache = 'no-input'
    lua_inspect_textures = os.path.join(w3luautilpath, 'inspect_textures.lua')

    if texturecaches and len(texturecaches) > 0:
        print('number of texture cache file: %s' % len(texturecaches))
        print('first cache in the list is %s' % texturecaches[0])
        texcache = texturecaches[0]

    luacmd = 'lua %s "%s" "%s"' % (lua_inspect_textures, texcache, outdir)
    print('LUA : %s' % luacmd)
    os.chdir(w3luautilpath)
    output = Popen(luacmd, shell=True, stdout=PIPE).stdout.read()


unpack_all_textures_for_maps(w3_path=_W3_PATH, w3luautilpath=_W3_LUA_MODULES, outdir=_TARGET_PATH)
