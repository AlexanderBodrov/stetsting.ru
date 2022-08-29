import requests


#   Проверяем статус ответа
def test_code():
    link = "https://reqres.in/api/single_user"
    response = requests.get(link)
    assert response.status_code == 200


#   Проверяем имя
def test_first_name():
    link = "https://reqres.in/api/single_user"
    response = requests.get(link)
    rj = response.json()
    data = rj.get('data')
    first_name = data['first_name']
    assert first_name == "Janet"
