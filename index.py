from flask import Flask, request, jsonify
from predict import response
app = Flask(__name__)

@app.route('/api/predict', methods=['POST'])
def predict():
 data = request.get_json()  # Get the JSON data from the request
 message = data['message']  # Extract the message from the JSON data
    # response = {
    #     data:"Got the response"
    # }
 result=response(message, userID='123', show_details=False)
 return result

# jsonify(response)  # Return the response as JSON

if __name__ == '__main__':
    app.run(debug=True)
