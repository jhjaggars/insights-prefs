from app import user
from db import Preference


def get():
    res = Preference.query.filter((Preference.account == user["account"])).one_or_none()
    return res.prefs if res else None, 200


def post(request):
    pass
