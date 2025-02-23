from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from routes import blueprint
app = Flask(__name__, static_folder='static')

app.config['SECRET_KEY'] = 'KwsJpGfCDlcP77okfHAtpbo-F_c'
app.config['WTF_CSRF_SECRET_KEY'] = 'yLnLKAJ3UuK8cEqmNucvLAuusjY'
app.config['UPLOAD_FOLDER'] = 'static/images'
app.register_blueprint(blueprint)


login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_message = "Please login."
login_manager.login_view = 'frontend.login'

from api.user_api import UserClient




@login_manager.user_loader
def load_user(user_id):
    return UserClient.get_user_by_id(user_id)  # Replace with your actual user-fetching logic

bootstrap = Bootstrap(app)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

