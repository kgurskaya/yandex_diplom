import configuration
import requests
import data


# Функция создает новый заказ

def post_new_order(body):
    print(configuration.URL_SERVICE + configuration.CREATE_ORDER)
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body,
                         headers=data.headers)

# Функция получает номер заказа

def get_order_track():
    response = post_new_order(data.order_body)
    return response.json().get('track')


# Функция получает заказ по его номеру

def get_order_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK + str(track))
