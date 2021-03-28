from flaskr import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

"""
You added the hello route as an example when writing the factory at the
beginning of the tutorial. It returns “Hello, World!”, so the test checks that
the response data matches.
"""

def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'