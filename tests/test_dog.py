import requests
import json
import pytest

def message_response(payload):
    base_url = "https://dog.ceo/api"
    response = requests.request("GET", base_url + payload)
    assert response.ok
    return response.json().get('message')

def test_random_image_not_nul():
    url="https://dog.ceo/api/breeds/image/random"
    response = requests.request("GET", url)
    assert response.ok
    assert "http" in response.text, f" нет http в строке {response_address}"

@pytest.mark.parametrize("breed",
                         ["boxer",
                          "chow" ],
                         ids=["Boxer", "Chow"])
def test_breeds_in_list(breed):
    url = "https://dog.ceo/api"
    payload = f"/breed/{breed}/images"
    response = requests.request("GET", url + payload)
    assert response.ok
    assert "message" in response.json(), "в ответе нет необходимого параметра"
    links_list = response.json().get("message")
    assert all(breed in link for link in links_list)


@pytest.mark.parametrize("breed",
                         ["borzoi",
                          "greyhound"],
                         ids=["poodle","greyhound"])
def test_breed_success(breed):
    base_url=f"https://dog.ceo/api/breed/"
    payload = f"{breed}/images/random"
    response = requests.request("GET", base_url+payload)
    assert response.ok, "ошибка в получении запроса"
    assert response.json().get('message'), "не удается получить ссылку на изображение"
    assert "http" in response.json().get('message'), f" нет http в строке {response_address}"

@pytest.mark.parametrize("number_of_image",
                         [1,50],
                         ids=["min", "max"])
def test_multiple(number_of_image):
    url = "https://dog.ceo/api/breeds"
    payload = f"/image/random/{number_of_image}"
    response = requests.request("GET", url + payload)
    assert response.ok
    massage = response.json().get('message')
    assert len(massage)==int(number_of_image), "количество ссылок не совпадает с запрошенным"

def test_full_list():
    total_australian = len(message_response("/breed/australian/images"))
    kelpie_australian = len(message_response("/breed/australian/kelpie/images"))
    shepherd_australian = len(message_response("/breed/australian/shepherd/images"))
    assert total_australian == kelpie_australian + shepherd_australian

def test_some_breds_in_list():
    url = "https://dog.ceo/api/breeds/list/all"
    response = requests.request("GET", url)
    assert response.ok
    assert "message" in response.json(), "в ответе нет необходимого параметра"
    list_from_request = response.json().get('message')
    some_breeds_list = ["borzoi","boxer", "pointer"]
    assert all(breed in list_from_request for breed in some_breeds_list)