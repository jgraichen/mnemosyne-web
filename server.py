#!/usr/bin/env python3

import asyncio
import aiohttp
import aiohttp.web

from mnemosyne.app import application
from mnemosyne.config import config

options = {}

if config.web.port is not None:
    options['port'] = config.web.port

aiohttp.web.run_app(application, **options)
