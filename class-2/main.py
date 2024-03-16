from data import db_session, jobs_api
from flask import Flask, Blueprint

app = Flask(__name__)


def main():
    db_session.global_init("db/users.db")
    app.register_blueprint(jobs_api.blueprint)
    app.run(debug=True)


if __name__ == '__main__':
    main()
