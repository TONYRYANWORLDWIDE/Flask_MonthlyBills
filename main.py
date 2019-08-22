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
@app.route('/MonthlyBill/')
def getMonthlyBills():
    bills = session.query(MonthlyBill).all()
    return render_template('monthlyBills.html', bills=bills)

@app.route('/MonthlyBill/new',methods=['GET','POST'])
def newMonthlyBills():
    if request.method == 'POST':
        newMonthlyBill = MonthlyBill(
        bill = request.form['bill'],
        cost = request.form['cost'],
        date = request.form['date'],
        UserID = request.form['UserID'],
        )
        session.add(newMonthlyBill)
        session.commit()
        return redirect(url_for('getMonthlyBills'))
    else:
        return render_template('addMonthlyBill.html')


@app.route('/MonthlyBill/<int:mbid>/edit')
def editMonthlyBills(mbid):
    editBill = session.query(MonthlyBill).filter_by(id =mbid).one()
    # newMonthlyBill = 
    # return render_template('monthlyBills.html', bills=bills)
    return render_template('editMonthlyBill.html', editBill = editBill)

@app.route('/MonthlyBill/<int:mbid>/delete')
def deleteMonthlyBills(mbid):
    deleteBill = session.query(MonthlyBill).filter_by(id =mbid).one()
    # newMonthlyBill = 
    # return render_template('monthlyBills.html', bills=bills)
    return render_template('deleteMonthlyBill.html', deleteBill = deleteBill)


if __name__ == '__main__':  # ensure function only runs if executed from the python interpreter
    app.secret_key = 'super_secret_key2'
    app.debug = True        # server will reload itself whenever a change is made
    app.run(host = '0.0.0.0' , port = 5000)