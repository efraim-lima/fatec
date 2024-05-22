#Import from the parent directory (app)
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from flask import Flask, request, jsonify, render_template, make_response
import datetime
from dotenv import load_dotenv
import json
from app.db import db
from app.logs.logs import info, error, warn, critic

load_dotenv()
now = datetime.datetime.now()
now = now.strftime("%Y-%m-%d %H:%M:%S")

def getStock(stock_symbol):
    quote = stock.delay(stock_symbol)
    result = quote.get()

    result = json.dumps(result)
    return result

def configure(app):

    @app.route('/stock/<string:stock_symbol>', methods=['GET'])
    def get_stock(stock_symbol):
        quote = getStock(stock_symbol)
        
        quote = json.loads(quote)
       
        info(f"route page accessed, 1")
        scrape = scraper.delay(stock_symbol)
        
        result = scrape.get()
        result = json.loads(result) 
        
        warn(f"got scrape result")
        return jsonify(result)

    @app.route('/stock/<string:stock_symbol>', methods=['POST'])
    def purchase(stock_symbol):
        amount = str(request.json.get('amount'))
        if not amount:
            critic(f"invalid amount at stock {stock_symbol}")
            abort(400, 'Invalid amount')
        else:
            stock_symbol = stock_symbol.upper()
            conn = db.get_db_connection()
            db.configure()
            db.insert(stock_symbol, amount, now)

            if db.check(stock_symbol, now) == True:
                # Get the sum of all amounts for the given stock symbol
                amount_sum = db.get_amount_sum(stock_symbol)

            phrase = f"{amount} units of stock {stock_symbol} were added to your stock record"
            db.close()
            warn(f"{amount} of {stock_symbol} purchased at {now}")
            return make_response(jsonify(phrase), 201)            

