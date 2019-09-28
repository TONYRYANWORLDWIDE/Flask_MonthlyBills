from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base , MonthlyBill, WeeklyBill,BringHome,BankBalance , MonthlyBills
app = Flask(__name__)

mb = MonthlyBills()
engine = mb.connect()
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

@app.route('/MonthlyBill/JSON')
def monthlyBillJSON():
    if request.method == 'GET':
        monthlybills = session.query(MonthlyBill).all()
        return jsonify(MonthlyBills=[i.serialize for i in monthlybills])

# if __name__ == '__main__':
#     monthlyBillJSON()

