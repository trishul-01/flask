from flask import Flask, request, jsonify

app = Flask(_name_)

# Example endpoint to receive POST requests with JSON data
@app.route('/process_tasks', methods=['POST'])
def process_json():
    # Check if the content type is JSON
    if request.headers['Content-Type'] != 'application/json':
        return jsonify({'error': 'Unsupported Media Type'}), 415

    # Assuming the request body contains JSON data
    try:
        data = request.json() #{t1:{celsius_to_fahrenheit:25}, t2:{fahrenheit_to_celsius:77}}
        if data.get('t1'):
            celsius_to_fahrenheit(data.get('t1')['celsius_to_fahrenheit'])
        if data.get('t2'):
            fahrenheit_to_celsius(data.get('t2')['fahrenheit_to_celsius'])
        #so on
        return True
        
    except Exception as e:
        return jsonify({'error': 'Invalid JSON'}), 400

    # Process the received JSON data (here, just returning it as response)
    return jsonify(data)


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


if _name_ == '_main_':
    app.run(debug=True)
