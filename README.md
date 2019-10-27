![Engagement Monitor Logo](https://github.com/akshatvg/engagement-monitor/blob/master/static/img/Logo.png "Engagement Monitor Logo")

### What is Engagement Monitor?
Engagement Monitor is a web application which helps analyse active or disinterested members of a WhatsApp group.


### How to use Engagement Monitor?
1) Go to group or individual chat settings on WhatsApp in your mobile phone and choose the 'Export Chat' option and save the .txt file anywhere on your device.
2) Open Engagement Monitor and upload the file after registering and logging in.
3) View each member's total count of messages and past counts in numbers as well as in the form of graphs and charts.


### Demo Link:
<http://engagement-monitor.tech>

(or) 

<https://engagement-monitor-cc.herokuapp.com>


### Advantages of Engagement Monitor?
1) Find out the most active members in a WhatsApp group.
2) Find out who spams the most in a WhatsApp group.
3) Keep track of inactive people who rarely/ never reply to or acknowledge messages.
4) Easy to use UI & UX.
5) Saves time checking statistics of member activity.


### Steps to run Engagement Monitor:

#### On MacOS:
```
1) git clone https://github.com/CodeChefVIT/engagement-monitor.git
2) cd engagement-monitor
3) pip install -r requirements.txt
4) cd engagement/venv
5) virtualenv .env
6) source .env/bin/activate
7) cd ..
8) python3 manage.py runserver
```

#### On Windows:
```
1) git clone https://github.com/CodeChefVIT/engagement-monitor.git
2) cd engagement-monitor
3) pip install -r requirements.txt
5) engage/Scripts/activate
6) cd engagement
7) python3 manage.py makemigrations
8) python3 manage.py migrate
9) python3 manage.py runserver
```
