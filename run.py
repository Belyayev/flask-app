from flask import Flask
from models import db, User
from routes import bp as main_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc://SA:YourStrong!Passw0rd@host.docker.internal:1433/your_database?driver=ODBC+Driver+17+for+SQL+Server"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

# Register Blueprints
app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
