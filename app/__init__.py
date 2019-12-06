import os
import re

from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message

# ======== Global Variables =========================================================== #
# -------- For Contact Form ---------------------------------------------------------- #
RECEPIENT_EMAILS = ["egillanton@gmail.com",
                    # "davidemollberg@gmail.com",
                    # "eyglombjorns@gmail.com",
                    # "gabrielajona@gmail.com",
                    # "stefanornsnae@gmail.com",
                    ]

BODY = "You have received a new message from your lingohack.is contact form.\n\nHere are the details:\n\nName: {}\n\nEmail: {}\n\nPhone: {}\n\nSubject: {}\n\nMessage:\n{}"


# ======== Strip HTML Tags from String =================================================#
def strip_tags(string, allowed_tags=''):
    if allowed_tags != '':
        # Get a list of all allowed tag names.
        allowed_tags_list = re.sub(r'[\\/<> ]+', '', allowed_tags).split(',')
        allowed_pattern = ''
        for s in allowed_tags_list:
            if s == '':
                continue
            # Add all possible patterns for this tag to the regex.
            if allowed_pattern != '':
                allowed_pattern += '|'
            allowed_pattern += '<' + s + ' [^><]*>$|<' + s + '>|'
        # Get all tags included in the string.
        all_tags = re.findall(r'<]+>', string, re.I)
        for tag in all_tags:
            # If not allowed, replace it.
            if not re.match(allowed_pattern, tag, re.I):
                string = string.replace(tag, '')
    else:
        # If no allowed tags, remove all.
        string = re.sub(r'<[^>]*?>', '', string)

    return string


# ======== CREATE APP  ================================================================#
def create_app(test_config=None):
    """create and configure the app"""
    app = Flask(__name__, instance_relative_config=True)
    app.secret_key = os.urandom(12)  # Generic key for dev purposes only

    # Mail Config
    app.config.update(dict(
        DEBUG=True,
        MAIL_SERVER='smtp.gmail.com',
        MAIL_PORT=587,
        MAIL_USE_TLS=True,
        MAIL_USE_SSL=False,
        MAIL_USERNAME=os.environ['EMAIL_USER'],
        MAIL_PASSWORD=os.environ['EMAIL_PASSWORD'],
        MAIL_DEFAULT_SENDER='noreply@lingohack.is',
        MAIL_MAX_EMAILS=5,
    ))
    mail = Mail(app)

    # ======== Routing ============================= #
    # -------- Home -------------------------------- #
    @app.route('/', methods=['GET'])
    @app.route('/eng', methods=['GET'])
    def index():
        return render_template('layouts/index.html')

    @app.route('/isl', methods=['GET'])
    def isl():
        return render_template('layouts/index_isl.html')

    # -------- EMAIL -------------------------------- #
    @app.route('/email', methods=['POST'])
    def email():
        name = strip_tags(request.json['name'])
        email = strip_tags(request.json['email'])
        phone = strip_tags(request.json['phone'])
        subject = strip_tags(request.json['subject'])
        message = strip_tags(request.json['message'])

        body = BODY.format(name, email, phone, subject, message)

        msg = Message(
            sender=("lingohack.is Contact Form", email),
            subject=subject,
            body=body,
            recipients=RECEPIENT_EMAILS,
        )

        mail.send(msg)

        return jsonify(
            message="Email was successfully sent",
        )

    return app
