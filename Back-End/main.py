from flask import Flask
from flask_cors import CORS
from API.Controllers import user_blueprint
from API.Controllers import ticket_blueprint

app = Flask(__name__)
app.json.sort_keys = False
CORS(app)

app.register_blueprint(user_blueprint, url_prefix='/user')
app.register_blueprint(ticket_blueprint, url_prefix='/ticket')


if __name__ == '__main__':
    app.run(port=5000)