from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
app = Flask(__name__)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base , MonthlyBill, WeeklyBill,BringHome,BankBalance
import datetime

engine = create_engine('sqlite:///TRBills.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

@app.route('/')
@app.route('/BankBalance/')
def getBankBalance():
    balances = session.query(BankBalance).all()
    return render_template('bankBalances.html', balances=balances)

@app.route('/BankBalance/new',methods=['GET','POST'])
def newBankBalance():
    if request.method == 'POST':
        newBankBalance = BankBalance(
        balance = request.form['balance'],
        date = datetime.datetime.now(),
        UserID = 'a5ca7194-40f8-4d8e-81ed-d56e7338317f'
        )
        session.add(newBankBalance)
        session.commit()
        return redirect(url_for('getBankBalance'))
    else:
        return render_template('addBankBalance.html')

@app.route('/BankBalance/<int:mbid>/edit', methods=['GET','POST'])
def editBankBalance(mbid):
    editBalance = session.query(BankBalance).filter_by(id =mbid).one()
    if request.method == 'POST':
        if request.form['balance']:
            editBalance.balance = request.form['balance']
        session.add(editBalance)
        session.commit()
        return redirect(url_for('getBankBalance'))
    else:
        return render_template('editBankBalance.html', mbid = mbid, item = editBalance)

@app.route('/BankBalance/<int:mbid>/delete',methods=['GET','POST'])
def deleteBankBalance(mbid):
    deleteBalance = session.query(BankBalance).filter_by(id = mbid).one()
    if request.method == 'POST':
        session.delete(deleteBalance)
        session.commit()
        return redirect(url_for('getBankBalance'))
    else:    
        return render_template('deleteBankBalance.html', mbid = mbid, item = deleteBalance)



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


@app.route('/MonthlyBill/<int:mbid>/edit', methods=['GET','POST'])
def editMonthlyBills(mbid):
    editBill = session.query(MonthlyBill).filter_by(id =mbid).one()
    if request.method == 'POST':
        if request.form['bill']:
            editBill.bill = request.form['bill']
        if request.form['cost']:
            editBill.cost = request.form['cost']
        if request.form['date']:
            editBill.date = request.form['date']
        if request.form['UserID']:
            editBill.UserID = request.form['UserID']
        session.add(editBill)
        session.commit()
        return redirect(url_for('getMonthlyBills'))
    else:
        return render_template('editMonthlyBill.html', mbid = mbid, item = editBill)

@app.route('/MonthlyBill/<int:mbid>/delete',methods=['GET','POST'])
def deleteMonthlyBills(mbid):
    deleteBill = session.query(MonthlyBill).filter_by(id = mbid).one()
    if request.method == 'POST':
        session.delete(deleteBill)
        session.commit()
        return redirect(url_for('getMonthlyBills'))
    else:    
        return render_template('deleteMonthlyBill.html', mbid = mbid, item = deleteBill)




@app.route('/WeeklyBill/')
def getWeeklyBills():
    bills = session.query(WeeklyBill).all()
    return render_template('weeklyBills.html', bills=bills)

@app.route('/WeeklyBill/new',methods=['GET','POST'])
def newWeeklyBills():
    if request.method == 'POST':
        newWeeklyBill = WeeklyBill(
        name = request.form['name'],
        dayOfWeek = request.form['dayOfWeek'],
        cost = request.form['cost'],
        UserID = request.form['UserID'],
        )
        session.add(newWeeklyBill)
        session.commit()
        return redirect(url_for('getWeeklyBills'))
    else:
        return render_template('addWeeklyBill.html')




@app.route('/WeeklyBill/<int:mbid>/edit', methods=['GET','POST'])
def editWeeklyBills(mbid):
    editBill = session.query(WeeklyBill).filter_by(id =mbid).one()
    if request.method == 'POST':
        if request.form['name']:
            editBill.name = request.form['name']
        if request.form['dayOfWeek']:
            editBill.dayOfWeek = request.form['dayOfWeek']
        if request.form['cost']:
            editBill.cost = request.form['cost']
        if request.form['UserID']:
            editBill.UserID = request.form['UserID']
        session.add(editBill)
        session.commit()
        return redirect(url_for('getWeeklyBills'))
    else:
        return render_template('editWeeklyBill.html', mbid = mbid, item = editBill)

@app.route('/WeeklyBill/<int:mbid>/delete',methods=['GET','POST'])
def deleteWeeklyBills(mbid):
    deleteBill = session.query(WeeklyBill).filter_by(id = mbid).one()
    if request.method == 'POST':
        session.delete(deleteBill)
        session.commit()
        return redirect(url_for('getWeeklyBills'))
    else:    
        return render_template('deleteWeeklyBill.html', mbid = mbid, item = deleteBill)


if __name__ == '__main__':  # ensure function only runs if executed from the python interpreter
    app.secret_key = 'super_secret_key2'
    app.debug = True        # server will reload itself whenever a change is made
    app.run(host = '0.0.0.0' , port = 5000)