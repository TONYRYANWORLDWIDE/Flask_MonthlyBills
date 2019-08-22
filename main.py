from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
app = Flask(__name__)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base , MonthlyBill, WeeklyBill


engine = create_engine('sqlite:///TRBills.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

@app.route('/')
@app.route('/MonthlyBill')
def getMonthlyBills():
    bills = session.query(MonthlyBill).all()
    for i in bills:
        print(i.bill)
    return render_template('monthlyBills.html', bills=bills)

@app.route('/MonthlyBill/new')
def newMonthlyBills():
    # newMonthlyBill = 
    # return render_template('monthlyBills.html', bills=bills)
    return 'Add Monthly Bill'

@app.route('/MonthlyBill/<int:mbid>/edit')
def editMonthlyBills(mbid):
    # newMonthlyBill = 
    # return render_template('monthlyBills.html', bills=bills)
    return 'Edit Monthly Bill'


if __name__ == '__main__':  # ensure function only runs if executed from the python interpreter
    app.secret_key = 'super_secret_key2'
    app.debug = True        # server will reload itself whenever a change is made
    app.run(host = '0.0.0.0' , port = 5000)