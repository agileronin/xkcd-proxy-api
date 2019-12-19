"""XKCD API Resource.

Falcon resource class for implementing XKCD API.

"""

import os
import json
import falcon
import requests


class XKCDResource(object):
    """XKCD resource."""

    def _handle_get(self, resp, url, error_message):
        """Handle the GET request to the XKCD API.

        Args:
            resp (obj): The response object injected into the class by Falcon.
            url (str): The XKCD URL to query.
            error_message (str): Error message string to display in the event of a 4xx response.

        """

        xkcd_resp = requests.get(url)
        if xkcd_resp.status_code == 200:
            resp.status = falcon.HTTP_200
            resp.body = json.dumps(xkcd_resp.json(), ensure_ascii=False)
        else:
            resp.status = falcon.HTTP_404
            resp.body = json.dumps(
                {'message': error_message}, ensure_ascii=False)

    def _process_xkcd_request(self, resp, id=None):
        """Retrieve a request from XKCD.

        Args:
            resp (obj): The response object injected into the class by Falcon.
            id: The id of the comic to retrieve. Load the latest comic if none specified.

        """

        base_url = os.getenv('XKCD_BASE_URL', 'https://xkcd.com')

        if not id:
            xkcd_url = '{}/info.0.json'.format(base_url)
            self._handle_get(
                resp, xkcd_url, 'Failed to retrieve latest XKCD comic.')
        else:
            xkcd_url = '{}/{}/info.0.json'.format(base_url, id)
            self._handle_get(
                resp, xkcd_url, 'Failed to retrieve XKCD comic number {}'.format(id))

    def on_get(self, req, resp, id=None):
        """HTP GET endpoint for the XKCD API.

        Args:
            req (obj): Request object injected into the class by the Falcon framework.
            resp (obj): Response object injected into the class by the Falcon framework.
            id (str): The ID for the comic to retrieve.

        """
        if not id:
            self._process_xkcd_request(resp)
        else:
            self._process_xkcd_request(resp, id)
