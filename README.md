# mnemosyne
[![Build Status](https://travis-ci.org/jgraichen/mnemosyne.svg?branch=master)](https://travis-ci.org/jgraichen/mnemosyne) [![license](https://img.shields.io/github/license/jgraichen/mnemosyne.svg?maxAge=2592000)](https://github.com/jgraichen/mnemosyne/blob/master/LICENSE)
An in-house monitoring platform (experimental)

## Install

Install Python 3.5+ and dependencies:

```
pip3 install -r requirements.txt
```

The web frontend is based on JavaScript. Install NodeJS and dependencies:

```
npm install
```

Build JavaScript frontend:

```
npm run dist
```

## Configuration

See `mnemosyne.ini`. Mnemosyne follows the XDG spec for configuration lookup and additionally search current working directory.

## Usage

Run consumer listing on AMQP queue on dumping traces to database:

```
python3 consumer.py
```

Run simple web server:

```
python3 server.py
```

Run with gunicorn3:

```
gunicorn mnemosyne.app --bind localhost:8080 --worker-class aiohttp.worker.GunicornWebWorker
```
