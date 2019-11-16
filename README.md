<h1 align="center">
Lingó Hack 2020 Landing Page
</h1>

<img src="https://user-images.githubusercontent.com/9976294/68986366-b1823c00-07ec-11ea-87d7-e7b7ce6270d5.png" alt="Screenshot" align="center"/>

<h2 align="center">
<a href="https://lingo-hack-2020.herokuapp.com/">> Website <</a>
</h2>

## Table of Contents
<!-- ⛔️ MD-MAGIC-EXAMPLE:START (TOC:collapse=true&collapseText=Click to expand) -->
<details>
<summary>Click to expand</summary>

1. [Introduction](#1-introduction)
2. [Setup](#2-setup)
3. [Collaborators](#3-collaborators)
4. [License](#4-license)
5. [References](#5-references)

</details>
<!-- ⛔️ MD-MAGIC-EXAMPLE:END -->


## 1 Introduction
This is the official code used for Lingó Hack Landing Page.

## 2 Setup

Make sure to have Python 3.6 or newer, and pip installed.

### 2.1 Get virtualenv

```bash
$ pip install virtualenv
```

### 2.2 Create a virtual enviroment

Make sure to create a Python3 instead of Python2 enviroment by refrencing its binaries.
```bash
$ which python3
/usr/bin/python3
```

You can use any name you want, we will use "venv".
```bash
$ virtualenv -p /usr/bin/python3  venv
```

### 2.3 Activate enviroment

```bash
$ . venv/bin/activate
```

Now you have activated your virual enviroment and your teminal should display its name as so:
```bash
$(venv)
```

### 2.4 Install requried packages
```bash
$(venv) pip3 install -r requirements.txt  
```

### 2.5 Run The Application

```bash
$(venv) flask run
```

You’ll see output similar to this:

```bash
Serving Flask app "app"
Environment: development
Debug mode: on
Running on http://127.0.0.1:5000/
Restarting with stat
Debugger is active!
Debugger PIN: 298-204-950
```

Open the link in your browser.

### 2.6 Push to Heroku
Make sure you have installed Heroku CLI, and have authentication to the Heroku project.

Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-command-line)
Download and install the Heroku CLI.

If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key.
**Login into Heroku**
```bash
$ heroku login
```

**Clone the repository**
Use Git to clone lingo-hack-2020's source code to your local machine.


```bash
$ heroku git:clone -a lingo-hack-2020
$ cd lingo-hack-2020
```

**Deploy your changes**
Make some changes to the code you just cloned and deploy them to Heroku using Git.

```bash
$ git add .
$ git commit -am "make it better"
$ git push heroku master
```

## 3 Collaborators
* [Egill Anton Hlöðversson](https://github.com/egillanton) - MSc. Language Technology Student

## 4 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 5 References
- [Flask 1.1.1](http://flask.pocoo.org/) - A microframework for Python web applications
- [Bootstrap 4](https://getbootstrap.com/) - An open source design system for HTML, CSS, and JS.
- [Jinja2 2.10.3](http://jinja.pocoo.org/docs/2.10/) - A templating language for Python, used by Flask.


<p align="center">
🌟 PLEASE STAR THIS REPO IF YOU FOUND SOMETHING INTERESTING 🌟
</p>