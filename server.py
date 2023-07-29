from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def welcome():
    return "Welcome to ITIL exam"


@app.route('/itil_modules')
def itil_modules():
    modules = ["cosa", "security concepts", "FCN", "NDC","PKI","Devops"]  
    return jsonify(modules)

# Route to return your information
@app.route('/my_info')
def my_info():
    prn = "2300344223004"  
    name = "Aniket Bhosale"  
    phone_number = "7030055987"   
    info = {
        "PRN": prn,
        "Name": name,
        "Phone Number": phone_number
    }
    return jsonify(info)

if __name__ == '__main__':
    app.run(debug=True)

