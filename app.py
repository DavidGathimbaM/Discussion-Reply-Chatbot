from flask import Flask, render_template, request
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

# Path to the notebook
notebook_path = "chatbot.ipynb"

# Load and execute the notebook
def run_notebook_function(func_name, *args):
    with open(notebook_path, "r", encoding="utf-8") as f:
        notebook = nbformat.read(f, as_version=4)
    
    # Execute the notebook
    ep = ExecutePreprocessor(timeout=600, kernel_name="python3")
    ep.preprocess(notebook, {"metadata": {"path": "."}})
    
    # Execute the function defined in the notebook
    global_namespace = {}
    exec("\n".join(cell["source"] for cell in notebook["cells"] if cell["cell_type"] == "code"), global_namespace)
    
    # Call the specific function
    return global_namespace[func_name](*args)

# Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form["user_input"]
    # Call the `generate_response` function from the notebook
    chatbot_response = run_notebook_function("generate_response", user_input)
    return {"user_input": user_input, "chatbot_response": chatbot_response}

if __name__ == "__main__":
    app.run(debug=True)
