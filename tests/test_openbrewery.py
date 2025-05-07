import requests
import json
import pytest

@pytest.mark.parametrize("city_req,city",
                         [('austin','Austin'),
                          ('norman','Norman')],
                         ids=["Austin", "Norman"])
def test_filter_by_city(city_req, city):
    url="https://api.openbrewerydb.org/v1/breweries"
    response = requests.request("GET", url, params={"by_city": city_req})
    assert response.ok
    breweries = response.json()
    brewery=breweries[0]
    assert brewery.get('city')==city, f"Город должен быть {city}, а он {brewery.get('city')}"

@pytest.mark.parametrize("obdb_id, name",
                         [('ef970757-fe42-416f-931d-722451f1f59c','10 Barrel Brewing Co'),
                          ('5fdcc498-f9df-4fa5-b35d-487a59f0fecc','2Kids Brewing Company')],
                         ids=["10 Barrel Brewing Co", "2Kids Brewing Company"])
def test_brawery_is_exist(obdb_id, name):
    url="https://api.openbrewerydb.org/v1/breweries"
    payload=f"/{obdb_id}"
    response = requests.request("GET", url+payload)
    assert response.ok
    brewery = response.json()
    breweryName = brewery.get('name')
    assert breweryName == name, f"имя должно быть {name}, а оно {brewery}"

def test_list_id():
    url = "https://api.openbrewerydb.org/v1/breweries"
    list_id = ["701239cb-5319-4d2e-92c1-129ab0b3b440","06e9fffb-e820-45c9-b107-b52b51013e8f"]
    response = requests.request("GET", url, params={"by_ids": list_id})
    assert response.ok
    breweries = response.json()
    assert all([brewery.get('id') in list_id for brewery in breweries])

def test_number_breweries():
    url = "https://api.openbrewerydb.org/v1/breweries"
    response = requests.request("GET", url , params={"per_page": 3})
    assert response.ok
    breweries = response.json()
    assert len(breweries)==3, "на странице не 3 человека"

def test_sort():
    url = "https://api.openbrewerydb.org/v1/breweries"
    response = requests.request("GET", url, params={"per_page": 5, "sort":"name"})
    assert response.ok
    breweries = response.json()
    assert all([breweries[i].get('name') <= breweries[i+1].get('name') for i in range (4)])