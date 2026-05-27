# import os

# from flask import Flask
# from flask_cors import CORS
# from flask_migrate import Migrate
# from config import Config
# from database import db
# from controllers.reviews_controller.reviews_controller import reviews_bp
# from controllers.services_controller.services_controller import service_bp
# from ai_routes import assistant_bp
# from ma import ma
# from dotenv import load_dotenv

# load_dotenv()


# migrate = Migrate()

# def create_app():
#     app = Flask(__name__)
#     FRONTEND = os.getenv('FRONTEND_URL')
#     CORS(app, resources={r"/api/*": {"origins": FRONTEND}}, supports_credentials=True)
#     app.config.from_object(Config)

#     db.init_app(app)
#     ma.init_app(app)
#     migrate.init_app(app, db)

#     app.register_blueprint(reviews_bp, url_prefix='/api/v1/reviews')
#     app.register_blueprint(service_bp, url_prefix='/api/v1/services')
#     app.register_blueprint(assistant_bp, url_prefix='/api/v1')

#     return app

# app = create_app()

# if __name__ == '__main__':
#     app.run(port=5000)



# import os
# from flask import Flask
# from flask_cors import CORS  # ДОДАНО: імпорт для зняття блокування CORS
# from flask_migrate import Migrate
# from config import Config
# from database import db
# from controllers.reviews_controller.reviews_controller import reviews_bp
# from controllers.services_controller.services_controller import service_bp
# from ai_routes import assistant_bp
# from ma import ma
# from dotenv import load_dotenv

# load_dotenv()

# migrate = Migrate()

# def create_app():
#     # ЗМІНЕНО: виправлено з 'name' на системну змінну 'name'
#     app = Flask(__name__)
    
#     # ЗМІНЕНО: замість обмеженого FRONTEND_URL поставили "*".
#     # Тепер твій бекенд прийматиме запити з будь-якого деплою фронтенду на Vercel без помилок CORS.
#     CORS(app, resources={r"/api/*": {"origins": "*"}})
    
#     app.config.from_object(Config)

#     db.init_app(app)
#     ma.init_app(app)
#     migrate.init_app(app, db)

#     app.register_blueprint(reviews_bp, url_prefix='/api/v1/reviews')
#     app.register_blueprint(service_bp, url_prefix='/api/v1/services')
#     app.register_blueprint(assistant_bp, url_prefix='/api/v1')

#     return app

# # ДОДАНО (ГЛОБАЛЬНО): створення екземпляра додатка на найвищому рівні (top-level).
# # Без цього рядка Vercel не бачив додаток і видавав помилку "Could not find a top-level app".
# app = create_app()

# # ЗМІНЕНО: виправлено умову перевірки головного файлу з 'name' на 'name'
# if __name__ == '__main__':
#     app.run(port=5000)



import os
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from config import Config
from database import db
from controllers.reviews_controller.reviews_controller import reviews_bp
from controllers.services_controller.services_controller import service_bp
from ai_routes import assistant_bp
from ma import ma
from dotenv import load_dotenv

load_dotenv()

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    # ЗМІНЕНО: Глобальний CORS для всіх маршрутів. 
    # Це гарантує, що браузер не блокуватиме запити до жодного з блюпринтів.
    CORS(app)
    
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(reviews_bp, url_prefix='/api/v1/reviews')
    app.register_blueprint(service_bp, url_prefix='/api/v1/services')
    app.register_blueprint(assistant_bp, url_prefix='/api/v1')

    return app

app = create_app()

if __name__ == '__main__':
    app.run(port=5000)