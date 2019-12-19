import pytest
import falcon
from falcon import testing

from xkcd_api import api


@pytest.fixture
def client():
    """Create a Falcon test client.

    Returns:
        (obj): A configured Falcon API context.

    """
    return testing.TestClient(api)
