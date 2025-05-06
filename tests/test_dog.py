import requests
import json
import pytest

def message_response(payload):
    base_url = "https://dog.ceo/api"
    response = requests.request("GET", base_url + payload, data=payload)
    return response.json().get('message')

def test_random_image_not_nul() :
    url="https://dog.ceo/api"
    payload="/breeds/image/random"
    response = requests.request("GET", url + payload, data=payload)
    assert "http" in response.text, f" нет http в строке {response_address}"

@pytest.mark.parametrize("breed",
                         [("boxer"),
                          ("chow") ],
                         ids=["Boxer", "Chow"])
def test_breeds_in_list(breed) :
    url = "https://dog.ceo/api"
    payload = "/breeds/list/all"
    response = requests.request("GET", url + payload, data=payload)
    assert breed in response.text

def test_poodle_success() :
    url="https://dog.ceo/api/breed"
    payload="/poodle/image/random"
    response = requests.request("GET", url + payload, data=payload)
    assert "http" in response.text, f" нет http в строке {response_address}"

@pytest.mark.parametrize("number_of_image",
                         [("1"),
                          ("50") ],
                         ids=["min", "max"])
def test_multiple(number_of_image) :
    url = "https://dog.ceo/api/breeds"
    payload = f"/image/random/{number_of_image}"
    response = requests.request("GET", url + payload, data=payload)
    massage = response.json().get('message')
    assert len(massage)==int(number_of_image), "количество ссылок не совпадает с запрошенным"

def test_full_list() :
    total_australian = len(message_response("/breed/australian/images"))
    kelpie_australian = len(message_response("/breed/australian/kelpie/images"))
    shepherd_australian = len(message_response("/breed/australian/shepherd/images"))
    assert total_australian == kelpie_australian + shepherd_australian