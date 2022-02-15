from flask import Flask, jsonify, request 
app = Flask(__name__)

languages = [{'Unnamed' : 'Yajush'}, {'Unnamed: 0.1' : 'Chaudhary'} , {'BIC / BLZ,Beguenstigter / Auftraggeber': 'DEUTDEFFXXX'} , {'Betrag': 'XXXXeuros'} , {'Buchungstag': '15.02.2022'} ,{'Verwendungszweck': 'Testing'} ,{'Umsatzart,IBAN / Kontonummer': '0980xxxx'} ,{'content': '-Content value-' }]
infile = open('input.txt', 'r')
firstLine = infile.readline()

@app.route('/', methods = ['GET'])
def test(): 
    return jsonify ("URL CALLING FUNCTION WORKS")

@app.route('/Unnamed: 0,Unnamed: 0.1,BIC / BLZ,Beguenstigter / Auftraggeber,Betrag,Buchungstag,Verwendungszweck,Umsatzart,IBAN / Kontonummer,content', methods = ['GET'])
def returnAll():
    return jsonify (languages)

if __name__ == '__main__': 
    app.run(debug=True, port =8080)
    
    