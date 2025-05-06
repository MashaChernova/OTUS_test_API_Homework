import requests
import json
import pytest


def test_user_is_exist() :
    url="https://jsonplaceholder.typicode.com/users/1"
    response = requests.request("GET", url)
    user = response.json()
    assert int(user.get('id')), f"такого id не существует"

@pytest.mark.parametrize("album_number",
                         [(1),
                          (50),
                          (100)],
                         ids = ['first','middle','last'])
def test_album_has_owner (album_number) :
    url = f"https://jsonplaceholder.typicode.com/albums/{album_number}"
    response = requests.request("GET", url)
    assert int(response.json().get('userId')) in range (11), f"номер пользователя не может быть больше 10, а он {int(response.json().get('userId'))}"

def test_realy_photos_owner() :
    url = f"https://jsonplaceholder.typicode.com/albums/2/photos"
    response = requests.request("GET", url)
    assert all([photo.get('albumId')==2 for photo in response.json()])

@pytest.mark.parametrize("substances",
                         [('user/1/posts'),
                          ('users'),
                          ('user/1/albums')],
                         ids = ['posts','users','albums'])
def test_unicum_number(substances) :
    url = f"https://jsonplaceholder.typicode.com/{substances}"
    substances_list = requests.request("GET", url).json()
    my_list = []
    for substance in substances_list :
        my_list.append(substance.get('id'))
    assert len(substances_list)==len(set(my_list)), f"кажется, есть повторяющиеся id среди {substance}"

def test_deleting() :
    url = f"https://jsonplaceholder.typicode.com/posts/1"
    response= requests.request("DELETE", url)
    assert response.status_code == 200, "код ответа отличается от 200"