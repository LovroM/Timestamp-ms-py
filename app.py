from time import strftime, mktime
from datetime import datetime, date
import re

from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<ext_url>")
def url_input(ext_url):
    
    unix = re.compile("[0-9]{10}")
    nat = re.compile("\w+\s\d+\,\s\d{4}")
    
    month_names = ["January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    
    if unix.match(ext_url):
        #unix input case
        unix_time = ext_url
        nat_time = datetime.fromtimestamp(float(ext_url)).strftime("%m %d, %Y")
        nat_time = nat_time.replace(nat_time[:2], month_names[int(nat_time[:2]) - 1])
        
        return jsonify(unix = unix_time, natural = nat_time)
        
    elif nat.match(ext_url):
        #natural time input case
        print ext_url
        date_list = ext_url.split()
        
        year = date_list[2]
        month = month_names.index(date_list[0])
        day = date_list[1][:len(date_list[1]) - 1]
        
        start = date(int(year), int(month), int(day))
        unix_time = mktime(start.timetuple())
    
        return jsonify(unix = unix_time, natural = date_list[0] + " " + str(day) + ", " + str(year) )
        
    else:
        return jsonify(unix = "null", natural = "null")


### Runs server
if __name__ == "__main__":
    app.debug = True
    app.run(host = "0.0.0.0", port = 8080)