import os
import re
import json
from flask import Flask, render_template, request, jsonify, send_file, send_from_directory, safe_join, abort

import sendgrid

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

    cwd = os.getcwd()
    app.config["PKI_VALIDATION"] = f"{cwd}/app/static/.well-known/pki-validation/"

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

        sg = sendgrid.SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))

        for to_email in RECEPIENT_EMAILS:
            sg = sendgrid.SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))

            data = {
                "personalizations": [
                    {
                        "to": [
                            {
                                "email": to_email
                            }
                        ],
                        "subject": subject
                    }
                ],
                "from": {
                    "email": email,
                    "name": name
                },
                "content": [
                    {
                        "type": "text/plain",
                        "value": body
                    }
                ]
            }
            response = sg.client.mail.send.post(request_body=data)

        return jsonify(
            message="Email was successfully sent",
        )

     # -------- SSL Verification -------------------------------- #
    @app.route('/.well-known/pki-validation/<path:filename>')
    def ssl_verification(filename):
        safe_path = safe_join(app.config["PKI_VALIDATION"], filename)

        print(safe_path)
        try:
            return send_file(safe_path, as_attachment=True)
        except FileNotFoundError:
            abort(404)

    return app
