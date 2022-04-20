from flask import Flask, render_template, request, redirect, url_for
import sqlite3 as sql
from	flask	import	Flask
app	=	Flask(__name__)

@app.route('/')
def	home():
	return	render_template("home.html")

@app.route("/products")
def product():
    return render_template("product.htm")

@app.route("/addrec/", methods = ["POST", "GET"])
def addrec():
    if request.method == "POST":
        nm = request.form["nm"]
        desc = request.form["desc"]
        qty = request.form["qty"]
        cid = request.form["cid"]
    
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO products (name, description, quantity, checkin) VALUES ('{0}', '{1}', '{2}', '{3}')".format(nm, desc, qty, cid))
        con.commit()
        message = "Product details added successfully"

    return render_template("result.htm", msg = message)


@app.route("/summary/")
def summary():
        con = sql.connect("database.db")
        con.row_factory = sql.Row

        cur = con.cursor()
        cur.execute("SELECT * FROM products")

        rows = cur.fetchall()
        return render_template("summary.htm", rows = rows)

if __name__ == '__main__':
    app.run(debug = True)
