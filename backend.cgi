#!/usr/bin/python3
from wsgiref.handlers import CGIHandler
from backend import app

CGIHandler().run(app)