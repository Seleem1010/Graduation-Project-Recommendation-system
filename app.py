from flask import Flask, send_from_directory

from blueprints.auth import auth
from blueprints.places import places
from blueprints.comments import comments
from blueprints.user import user
from blueprints.ratings import ratings

from models.db import DB
from utils.mailer import Mailer
from utils.config import MAIL_CONFIG

app = Flask(__name__, static_url_path='')

app.register_blueprint(auth, url_prefix='/api/auth')
app.register_blueprint(places, url_prefix='/api/places')
app.register_blueprint(comments, url_prefix='/api/comments')
app.register_blueprint(user, url_prefix='/api/user')
app.register_blueprint(ratings, url_prefix='/api/ratings')
@app.route('/images/<path:path>')
def send_images(path):
    return send_from_directory('images', path)

app.config['MAIL_SERVER'] = MAIL_CONFIG['server']
app.config['MAIL_PORT'] = MAIL_CONFIG['port']
app.config['MAIL_USERNAME'] = MAIL_CONFIG['username']
app.config['MAIL_PASSWORD'] = MAIL_CONFIG['password']
app.config['MAIL_USE_TLS'] = MAIL_CONFIG['tls']
app.config['MAIL_USE_SSL'] = MAIL_CONFIG['ssl']

if __name__ == "__main__":
    DB()
    Mailer(app)
    app.run(port=3000, debug=True)
