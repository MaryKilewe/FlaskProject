
from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)


@app.route("/")
def home():
    return "getting somewhere"


@app.route("/index")
def index():
    return render_template('index.html')


# anytime you want to pass a variable in your URL you use angle brackets < >
@app.route("/user/<username>")
def user(username):
    return "Hey there %s" % username


#=================================================================================
# create a table named register. Columns: username, password, firstname, lastname
@app.route('/register', methods=['POST', 'GET'])
def register():
    # logic goes here. handle form data
    if request.method == 'POST':  # check if user posted something
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        username = request.form['username']
        password = request.form['password']

        con = pymysql.connect("localhost", "root", "", "sampledb")
        cursor = con.cursor()
        sql = "INSERT INTO register_tbl(`firstname`,`lastname`,`username`,`password`) VALUES(%s,%s,%s,%s)"  # use tick marks ( ` ) instead of single quotes
        try:
            cursor.execute(sql, (firstname, lastname, username, password))
            con.commit()  # commit changes to the db
            return render_template('register.html', msg="Uploaded!")
        except:
            con.rollback()
            return render_template('register.html', msg="Failed!")
    else:
        return render_template('register.html')


#=================================================================================


import matplotlib.pyplot as plt
@app.route('/analysis')
def analysis():

    years = [2010, 2012, 2014, 2015, 2016, 2018, 2020]
    budget = [20000, 15000, 50000, 60000, 70000, 45000, 10000]

    # plot, scatter, bar graph,


    plt.xlabel = "years"
    plt.ylabel = "expense in KES"
    plt.title = "budget distribution / yearly"
    scattergraph = plt.scatter(years, budget)
    plt.savefig("static/image/scatter.png")
    bargraph = plt.bar(years, budget)
    plt.savefig("static/image/bar.png")
    plt.show()

    return render_template('analysis.html')


@app.route('/joinus')
def joinus():
    # we need to create a html page for this route
    # in templates folder
    return render_template('joinus.html')


@app.route('/flag')
def flag():
    # we need to create a html page for this route
    # in templates folder
    return render_template('flag.html')


@app.route('/products')
def products():
    return render_template('products.html')


@app.route('/services')
def services():
    return render_template('services.html')


if __name__ == "__main__":
    app.run(debug=True)
