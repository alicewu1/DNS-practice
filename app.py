## .SSH Terminal Setup Commands
# sudo apt-get update
# sudo apt install python3-pip
# pip3 install Flask
# git clone (repo URL)
#cd to Part1_Remote_GCP
# sudo python3 app.py
# nano app.py to read/edit 
# Ctrl + Z
# bg
# sudo nohup python3 app.py > log.txt 2>&1 &

from flask import Flask 

app = Flask(__name__)

@app.route('/') ## .route creates landing page for app
def hello_world():
    return 'Hello world!'

@app.route('/contact')
def contact():
    return 'List of contact names, numbers, and emails'

@app.route('/reports')
def reports():
    return 'View quarterly reports'

@app.route('/resources')
def resources():
    return 'List of relevant news or articles'


## .run actually runs the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80) 
    ## host set to 0.0.0.0 to match IP address of remote instance