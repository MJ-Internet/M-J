from functools import wraps
from flask import session, redirect

def login_required(route):
    @wraps(route)
    def wrapper(*args, **kwargs):
        if not session.get("logged_in"):
            return redirect("/login")
        return route(*args, **kwargs)
    return wrapper
