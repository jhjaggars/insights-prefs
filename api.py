from app import user
from db import Preference


def _get_pref_for(account):
    return Preference.query.filter((Preference.account == account)).one_or_none()


def _format(prefs):
    return {"version": "v0", "preferences": prefs}


def get():
    res = _get_pref_for(user["account"])
    return _format(res.prefs if res else None), 200


def post(preference_set):
    existing = _get_pref_for(user["account"])
    if not existing:
        p = Preference(account=user["account"], prefs=preference_set["preferences"])
        p.save()
        return _format(p.prefs), 201
    else:
        existing.prefs = preference_set["preferences"]
        existing.save()
        return _format(existing.prefs), 200
