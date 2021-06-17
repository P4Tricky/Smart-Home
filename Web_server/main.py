from flask import Flask, url_for, redirect, render_template, request
import os
import sys

# Changing current directory to parent
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import db
from db import Sensor, Device
from handle_json import JsonObj
from comm import Comm


# CONSTANTS 
DB_NAME = "data.db" 
JSON_NAME = "devices.json"
JSON_PATH = os.path.join(parentdir, JSON_NAME)
DB_PATH = os.path.join(parentdir, DB_NAME)


app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    # ------------ POST METHOD ------------ #
    if request.method == "POST":        
        form_data = request.form.get("update")
        device, status = form_data.split(";")

        """ Add form validation """

        j = JsonObj(JSON_PATH)

        # Send data to broker
        c = Comm(client_id="Sender253")
        c.send("myhome", f"{j.get_specified(device)['id']};{status}")
        c.disconnect()

        # Update current device status
        success = j.modify(device, "status", int(status))
        if success:
            j.update()
            """ msg success - Not matching key in json file """
        
        else:
            print("Error! Cannot update specified device!")
            # msg unsuccess

        return redirect(url_for("home"))
    
    # ------------ GET METHOD ------------ #
    else:
        context = {"devices": []}
        
        devices = JsonObj(JSON_PATH)
        for key, attr in devices.get().items():
            new = {
                "id": attr["id"],
                "name": key,
                "value": attr["status"]
            }
            context["devices"].append(new)

        return render_template("home.html", context=context)


@app.route("/devices")
def devices():
    context = {"devices": []}

    d = Device(DB_PATH)
    for device in reversed(d.query_all()):
        new = {
            "id": device[0],
            "name": device[1],
            "status": device[2],
            "date_created": device[3] 
        }
        context["devices"].append(new)
    
    d.close_conn()
    return render_template("devices.html", context=context)


    

if __name__ == "__main__":
    app.run(debug=True)