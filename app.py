from model import Model
import torch

from flask import Flask, request, jsonify
app = Flask(__name__)


x = torch.rand(5, 3)
vocab_size = 4
model = Model(x_dim = x.shape[-1], n_classes = vocab_size)
print(model(x))

@app.route('/home')
def home():
    return "Home"

@app.route("/security")
def security():
    return "Checking Security route"

@app.route("/predict", methods = ["POST"])
def predict():
    data = request.get_json()

    if data:
        x = data.get("x")
        x = torch.tensor(x, dtype = torch.float32)
        model_id = data.get("model_id")
        if model_id == 1:
            current_model = model
        else:
            return "Model is not Defined"
        with torch.no_grad():
            probs = current_model(x)
        return jsonify({
            "input": x.tolist(),
            "probs": probs.tolist(),
            "predicted_label": torch.argmax(probs, dim=-1).item()
        })
    else:
        return "Data Not Recieved"
    

if __name__ == "__main__":
    app.run(debug=True)