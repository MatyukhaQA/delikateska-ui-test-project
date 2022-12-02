import requests
from pytest_voluptuous import S
from voluptuous import PREVENT_EXTRA, Schema

create_user_schema = Schema(
    {
        "data": {
            "id": int,
            "email": str,
            "first_name": str,
            "last_name": str,
            "avatar": str
        },
        "support": {
            "url": str,
            "text": str
        }
    },
    extra=PREVENT_EXTRA,
    required=True,
)


def test_get_single_user():
    result = requests.get("https://reqres.in/api/users/2")

    assert result.status_code == 200
    assert result.json() == S(create_user_schema)
    assert len(result.json()['data']) != 0
    assert len(result.json()['support']) != 0
    assert result.json()['data']['first_name'] == 'Janet'