from flask import Flask, url_for
from .users_mock_base import users

app = Flask(__name__)

@app.route("/")
def root_page():
    return "Root page"

@app.route("/about")
def about_page():
    return "About page"

@app.route("/users")
def all_users_page():
    payload = "Users"
    for user in users:
        payload += f"""
        <br>
        <a href={url_for('user_page', user_id=user)}>
        USER:{users[user]["name"]}
        </a>
        """
    return payload

@app.route("/users/<int:user_id>")
def user_page(user_id):
    if user_id in users:
        payload = f"""
            USER:{users[user_id]["name"]}
            <br>AGE:{str(users[user_id]["age"])}
            """
        return payload
    else:
        return f"User {user_id} not available"



