from flask import Flask, render_template
import os
from datetime import datetime, time
import dotenv

dotenv.load_dotenv()
app = Flask(__name__)
app.secret_key = os.urandom(32)


def format_currency(value):
    if isinstance(value, (int, float)):
        return "₩{:,.0f}".format(value)
    return value


app.jinja_env.filters['currency'] = format_currency


@app.route('/')
def home():  # put application's code here
    return render_template('./login/login.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('./error/404err.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('./error/500err.html'), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
