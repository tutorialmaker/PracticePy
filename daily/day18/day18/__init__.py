from flask import Flask
import os


app = Flask(__name__)
app.config.from_mapping(SECRET_KEY=os.urandom(24))


# TODO: flask runでサーバを起動
