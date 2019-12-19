import falcon

from expects import expect, be, have_key

# NOTE(agileronin): These keys are returned from the XKCD JSON service.
VALID_KEYS = [
    'month',
    'num',
    'link',
    'year',
    'news',
    'safe_title',
    'transcript',
    'alt',
    'img',
    'title'
]


class TestAPI:
    """API test class.

    For convenience, all unit tests for the XKCD API are encapsulated into this class.

    """

    def test_fetch_latest(self, client):
        """Fetch the latest XKCD comic.

        Args:
            client: Falcon API context injected as a fixture by pytest.

        """

        resp = client.simulate_get('/')
        expect(resp.status).to(be(falcon.HTTP_200))
        for key in VALID_KEYS:
            expect(resp.json).to(have_key(key))

    def test_fetch_specific_comic(self, client):
        """Test the ability to fetch a specific XKCD comic by it's identifier.

        Args:
            client: Falcon API context injected as a fixture by pytest.

        """

        resp = client.simulate_get('/1')
        expect(resp.status).to(be(falcon.HTTP_200))
        for key in VALID_KEYS:
            expect(resp.json).to(have_key(key))

        # NOTE(agileronin): At some point in time this test will fail; however it will be an
        # epic day when XKCD releases their 10 millionth comic!
        resp = client.simulate_get('/10000000')
        expect(resp.status).to(be(falcon.HTTP_404))
