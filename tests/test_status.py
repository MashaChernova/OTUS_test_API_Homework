import pytest
import requests

def test_statuse_code (status_code, url):
    assert requests.get(url).statuse_code == status_code


