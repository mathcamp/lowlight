Lowlight
========
This is a tiny little server for a coding interview question for our mobile
candidates. It serves up a list of users and their photos.

Running the Server
------------------
It's easiest to run this from a developer machine, because the EC2 security
group is open on port 80. So ssh to your developer machine and then::

    git clone git@github.com:mathcamp/lowlight
    cd lowlight
    virtualenv venv
    . venv/bin/activate
    pip install -e .
    sudo su # become root because the webserver will listen on port 80
    . venv/bin/activate # Have to reactivate because sudo breaks out of virtualenv
    pserve production.ini

Now your server will be listening on port 80. I'd recommend doing this inside a
tmux or screen session so you can do other things while this is going on.

Prompt
------
Your task is to create a small app that displays a set of users. The only
requirements are that you must have a screen that displays them in a list, and
a screen that displays them on a map.

Any and all software libraries on the internet are acceptable. Do not use any
art assets that are not built into iOS. If you have extra time and want to make
the app more visually appealing and fancy without adding art, please do.

The list of users can be acquired from the following endpoint:

http://<ip address>/feed
