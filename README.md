[![Build Status](https://travis-ci.org/javad-hajiani/Exchanger.svg?branch=master)](https://travis-ci.org/javad-hajiani/dnsmanager)

# DNS Manager with Django RESTful API

## Getting Started

This script help us for work easily with bind dns in your scripts.Its my experience for our servers.

You Can Call each kind of actions in bash scripts or applications and parse Json Output in your application.

- bear this in mind that, it works if your dns structure like [Bind9 Split Horizon](https://github.com/javad-hajiani/Ansible-Bind-DNS-Cluster).
### Requirements

- ##### Python3
 - Debian Based
  - > sudo apt install python3
 - Redhat Based
  - > sudo yum install python3
 - Arch Based
  - > sudo pacman -Sy python3
#

- ##### virtualenv
 - > pip install virtualenv
- ##### Django 2
 - > pip install django==2

### Installation
#### Step by Step

- >  sudo apt install python3
- > pip install virtualenv
- > pip install -r requirements.txt
- > source venv/bin/activate
- > python manage.py runserver 
