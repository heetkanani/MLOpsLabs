from flask import Flask, request, jsonify
import joblib
import os
import sys

sys.path.insert(0, '/app')

app = Flask(__name__)
MODEL_PATH = os.path.join('artifacts', 'iris_model.pkl')

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})

@app.route('/predict', methods=['POST'])
def predict():
    if not os.path.exists(MODEL_PATH):
        return jsonify({'error': 'Model not found'}), 404
    
    model = joblib.load(MODEL_PATH)
    data = request.json
    features = data.get('features', [])
    
    if len(features) != 4:
        return jsonify({'error': 'Expected 4 features'}), 400
    
    prediction = model.predict([features])[0]
    return jsonify({'prediction': int(prediction)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)