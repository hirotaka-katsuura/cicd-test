import pytest
from hello import app

def test_flask_simple():
    app.config['TESTING'] = True
    client = app.test_client()
    result = client.get('/')
    assert b'Hello World' == result.data