from app import app
from app import DEVOPS_QUOTES


def test_home():
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200
    assert b"DevOps" in res.data


def test_motivator():
    client = app.test_client()
    res = client.get("/motivator")
    assert res.status_code == 200


def test_motivator_content():
    client = app.test_client()
    res = client.get("/motivator")
    quote = res.data.decode("utf-8")
    assert quote in DEVOPS_QUOTES
