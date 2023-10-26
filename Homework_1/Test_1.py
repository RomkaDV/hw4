"""Семинар № 1. Реализация тестирования API с использованием DDT.

Задание:
Условие: Добавить в задание с REST API ещё один тест, в котором создаётся новый пост,
а потом проверяется его наличие на сервере по полю «описание».
Подсказка: создание поста выполняется запросом к https://test-stand.gb.ru/api/posts
с передачей параметров title, description, content.
"""
import pytest
import requests
import yaml

S = requests.Session()

with open("config.yaml", encoding='utf-8') as f:
    data = yaml.safe_load(f)


def test_create_post(login):
    url = data['address_post']
    headers = {'X-Auth-Token': login}
    d = {'title': data['title'],
         'description': data['description'],
         'content': data['content']
         }

    res = S.post(url, headers=headers, data=d)
    assert str(res) == '<Response [200]>', "ОШИБКА! Новый пост не создан"


def test_check_description(login, get_description):
    url = data['url_post']
    headers = {'X-Auth-Token': login}
    res = S.get(url=url, headers=headers).json()['data']
    print(res)
    lst = [x['description'] for x in res]
    assert get_description in lst, "ОШИБКА! Новый пост не найден"


if __name__ == "__main__":
    pytest.main(["-vv"])