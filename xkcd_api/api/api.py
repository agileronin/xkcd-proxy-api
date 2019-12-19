"""Falcon API."""

import falcon

from xkcd_api.middleware.cors import CORSComponent
from xkcd_api.resources.xkcd_resource import XKCDResource

xkcd_resource = XKCDResource()
api = application = falcon.API(middleware=[CORSComponent()])
api.add_route('/{id}', xkcd_resource)
