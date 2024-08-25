from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://SA:yourStrong(!)Password@localhost:1433/your_database?driver=ODBC+Driver+17+for+SQL+Server'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

from app import routes
