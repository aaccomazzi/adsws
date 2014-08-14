# -*- coding: utf-8 -*-

from __future__ import absolute_import

from .server import blueprint as server_blueprint
from .settings import blueprint as settings_blueprint

blueprints = [
    server_blueprint,
    settings_blueprint,
]
