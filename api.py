from app import user
from db import Preference


def get():
    res = Preference.query.filter((Preference.account == user["account"])).one_or_none()
    doc = {
        "version": "v0",
        "prefs": res.prefs if res else None
    }
    return doc, 200


def post(request):
    pass
