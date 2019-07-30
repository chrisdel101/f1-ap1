from controllers import drivers_controller, teams_controller
from utilities import scraper
from models import driver_model
from flask import Flask
from flask import render_template
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from database import db
import json
from utilities import scraper_runner, utils

app = Flask(__name__)
# db.init_app(app)

app.config.from_pyfile("flask.cfg")
app.config.update(
    SQLALCHEMY_TRACK_MODIFICATIONS=app.config['SQLALCHEMY_TRACK_MODIFICATIONS'],
    SQLALCHEMY_DATABASE_URI=app.config['SQLALCHEMY_DATABASE_URI']
)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/drivers')
def all_drivers():
    return jsonify(drivers_controller.show_all_drivers())


@app.route('/drivers/<driver_slug>')
def driver(driver_slug):
    return jsonify(drivers_controller.show_single_driver(driver_slug))


@app.route('/teams')
def all_teams():
    x = teams_controller.show_all_teams()
    print(x)
    return "hello"


@app.route('/teams/<team_slug>')
def team(team_slug):
    return jsonify(scraper.scrape_single_drvier_stats(team_slug))


@app.route('/scrape-drivers')
def scrape_drivers():
    return jsonify(scraper_runner.scrape_drivers())


@app.route('/scrape-teams')
def scrape_teams():
    scraper_runner.scrape_teams()
    return "hello"


@app.route('/scrape-all')
def all():
    scrape_drivers.main()


if __name__ == '__main__':
    app.run(debug=True)
