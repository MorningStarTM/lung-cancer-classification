from flask import Flask, redirect, render_template, request, jsonify

application  = Flask(__name__)
app = application

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/predict", methods=["POST"])
def predict():
    # Handle image upload and prediction here
    # You'll need code to preprocess the image and use your trained model for classification
    # Return the classification result as JSON
    return jsonify({"result": "Cancer"})



if __name__ == "__main__":
    app.run(host="0.0.0.0" ,debug=True)