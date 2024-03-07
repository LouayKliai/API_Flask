from functools import wraps
from flask import redirect, url_for
from flask_login import current_user

def login_required(view_func):
    @wraps(view_func)
    def wrapped_view(*args, **kwargs):
        if not current_user.is_authenticated:
            return redirect(url_for('login'))  # Redirige vers la page de connexion
        return view_func(*args, **kwargs)
    return wrapped_view
