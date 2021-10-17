from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def render_index():
    return render_template("index.html")

@app.route('/<int:rows>') # acccept rows value and set columns to 8
def render_board(rows):
    return render_template("checkerboard.html",rows=rows,columns=8)

@app.route('/<int:rows>/<int:columns>')
def render_board2(rows,columns): #accepts a value for both rows and columns from user
    return render_template("checkerboard2.html",rows=rows, columns=columns)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
