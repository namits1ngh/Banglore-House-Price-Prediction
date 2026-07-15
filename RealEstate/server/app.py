from flask import Flask, render_template, request, jsonify
import util

app = Flask(__name__)

# Load model and columns when Flask starts
util.load_saved_artifacts()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = {
        "locations": util.get_location_names()
    }
    return jsonify(response)


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        total_sqft = float(request.form['total_sqft'])
        location = request.form['location']
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])

        estimated_price = util.get_estimated_price(
            location,
            total_sqft,
            bhk,
            bath
        )

        return jsonify({
            "estimated_price": round(estimated_price, 2)
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        })


if __name__ == "__main__":
    app.run(debug=True)