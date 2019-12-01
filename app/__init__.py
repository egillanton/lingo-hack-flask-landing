import os

from flask import Flask, render_template, request
from flask_mail import Mail, Message
import re


SUBJECT = "Lingó Hack 2020 Website Form: {}"
RECEPIENT_EMAILS = ["egilla14@ru.is", "egillanton@live.com"]
BODY = "You have received a new message from your website contact form.\n\nHere are the details:\n\nName: {}\n\nEmail: {}\n\nPhone: {}\n\nMessage:\n{}"
HEADER = "From: noreply@ru.is\nReply-To: {}"

# mail_settings = {
#     "MAIL_SERVER": ' smtp.office365.com',
#     "MAIL_PORT": 587,
#     "MAIL_USE_TLS": False,
#     "MAIL_USE_SSL": True,
#     "MAIL_USERNAME": os.environ['EMAIL_USER'],
#     "MAIL_PASSWORD": os.environ['EMAIL_PASSWORD']
# }


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


def create_app(test_config=None):
    """create and configure the app"""
    app = Flask(__name__, instance_relative_config=True)
    app.secret_key = os.urandom(12)  # Generic key for dev purposes only
    mail = Mail(app)

    # ======== Routing ============================= #
    # -------- Home -------------------------------- #
    @app.route('/', methods=['GET'])
    def index():
        return render_template('layouts/index.html')

    # -------- EMAIL -------------------------------- #
    @app.route('/email', methods=['POST'])
    def email():
        try:
            name = strip_tags(request.json['name'])
            email = strip_tags(request.json['email'])
            phone = strip_tags(request.json['phone'])
            message = strip_tags(request.json['message'])

            body = BODY.format(name, email, phone, message)
            sender = HEADER.format(email)

            msg = Message(body,
                          sender=sender,
                          recipients=RECEPIENT_EMAILS)

            mail.send(msg)
        except:
            pass

    return app
