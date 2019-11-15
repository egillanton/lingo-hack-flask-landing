import os

from flask import Flask, render_template


def create_app(test_config=None):
    """create and configure the app"""
    app = Flask(__name__, instance_relative_config=True)
    app.secret_key = os.urandom(12)  # Generic key for dev purposes only

    # ======== Routing ============================= #
    # -------- Home -------------------------------- #
    @app.route('/', methods=['GET'])
    def index():
        return render_template('layouts/index.html')
    
    # -------- CHALLENGES -------------------------- #
    @app.route('/challenges', methods=['GET'])
    def challenges():
        return render_template('layouts/challenges.html')

    # -------- SPONSORS & PARTNERS ----------------- #
    @app.route('/sponsors_partners', methods=['GET'])
    def sponsors_partners():
        return render_template('layouts/sponsors_partners.html')

    # -------- FAQ --------------------------------- #
    @app.route('/faq', methods=['GET'])
    def faq():
        return render_template('layouts/faq.html')

    return app