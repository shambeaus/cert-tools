from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import scripts.openssl as openssl

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)


@app.route("/", methods=['GET'])
def first():
    return openssl.generate_private_key('1024')


if __name__ == "__main__":
    app.run()