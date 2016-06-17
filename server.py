#!/usr/bin/env python3

import aiohttp.web

from mnemosyne import app
from mnemosyne.config import config

options = {}

if config.web.port is not None:
    options['port'] = config.web.port

aiohttp.web.run_app(app, **options)
