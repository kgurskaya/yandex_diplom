import sender_stand_request
import data


def check_order():
    track_obj = sender_stand_request.post_new_order(data.order_body)
    track_response = sender_stand_request.get_order_by_track(track_obj.json()['track'])
    assert track_response.status_code == 200


def test_order_track():
    check_order()
