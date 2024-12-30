from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

# Global variable to store the DataFrame
df = None

# Folder to store uploaded files
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    """Route for file upload."""
    global df
    if request.method == 'POST':
        file = request.files['file']
        if file:
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(file_path)
            df = pd.read_excel(file_path)
            return render_template('index.html', columns=df.columns.tolist())
    return render_template('upload.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    """Route for counting occurrences and filtering data."""
    global df
    if df is not None:
        column = request.form['column']
        value = request.form['value'].strip().lower()

        # Normalize data for case-insensitivity and whitespace trimming
        df[column] = df[column].astype(str).str.strip().str.lower()

        # Count the occurrences
        count = (df[column] == value).sum()

        # Filter the data based on the value
        filtered_data = df[df[column] == value]

        # Return results to result.html without saving as file
        return render_template('result.html', count=count, filtered_data=filtered_data.to_html(classes="table table-striped", index=False))
    return "No data uploaded yet!", 400

if __name__ == '__main__':
    app.run(debug=True)