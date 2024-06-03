# from flask import Flask, render_template, request
# import pandas as pd

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('upload.html')

# @app.route('/upload', methods=['GET','POST'])
# def upload():
#     if 'file' not in request.files:
#         return "No file part"
    
#     file = request.files['file']
    
#     if file.filename == '':
#         return "No selected file"
    
#     if file:
#         xls = pd.ExcelFile(file)
#         sheet_names = xls.sheet_names
#         data_dict = {}
#         for sheet_name in sheet_names:
#             df = pd.read_excel(xls, sheet_name, skiprows=1)  # Skip the first row
#             # Replace empty strings with an empty cell placeholder
#             df.replace('', '', inplace=True)
#             # Drop rows and columns containing only empty cells
#             df = df.replace('', pd.NA).dropna(axis=0, how='all').dropna(axis=1, how='all')
#             data_dict[sheet_name] = df.to_html(index=False, na_rep='')  # Replace remaining NaN with empty string
        
#         return render_template('data.html', data_dict=data_dict)

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return "Please upload an Excel file using the form."
    
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    
    if file.filename == '':
        return "No selected file"
    
    if file:
        xls = pd.ExcelFile(file)
        sheet_names = xls.sheet_names
        data_dict = {}
        for sheet_name in sheet_names:
            df = pd.read_excel(xls, sheet_name, skiprows=1)  # Skip the first row
            # Replace empty strings with an empty cell placeholder
            df.replace('', '', inplace=True)
            # Drop rows and columns containing only empty cells
            df = df.replace('', pd.NA).dropna(axis=0, how='all').dropna(axis=1, how='all')
            data_dict[sheet_name] = df.to_html(index=False, na_rep='')  # Replace remaining NaN with empty string
        
        return render_template('data.html', data_dict=data_dict)

if __name__ == '__main__':
    app.run(debug=True)