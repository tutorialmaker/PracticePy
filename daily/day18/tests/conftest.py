import pytest
from day18 import app


@pytest.fixture
def _app():
    app.config.update({'TESTING': True})
    yield app


@pytest.fixture
def client(_app):
    return app.test_client()
