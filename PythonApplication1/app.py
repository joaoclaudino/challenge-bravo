# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Lista de moedas suportadas
supported_currencies = ['USD', 'BRL', 'EUR', 'BTC', 'ETH', 'HURB', 'GTA$']

# Endpoints para cotações reais (substitua pela sua API de cotações reais)
REAL_RATES_API = "https://api.exchangerate-api.com/v4/latest/USD"

# Cotações fictícias (exemplo)
fictional_rates = {
    'HURB': 0.5,  # 1 USD = 0.5 HURB
    'GTA$': 0.0000668  # 1 USD = 0.0000668 GTA$
}

# Endpoint para conversão de moeda
@app.route('/convert', methods=['GET'])
def convert_currency():
    from_currency = request.args.get('from')
    to_currency = request.args.get('to')
    amount = float(request.args.get('amount', 1.0))

    if from_currency not in supported_currencies or to_currency not in supported_currencies:
        return jsonify({"error": u"Moeda não suportada"}), 400

    if from_currency in fictional_rates:
        from_rate = fictional_rates[from_currency]
    else:
        from_rate = get_real_rate(from_currency)
    
    if to_currency in fictional_rates:
        to_rate = fictional_rates[to_currency]
    else:
        to_rate = get_real_rate(to_currency)

    if from_rate is None or to_rate is None:
        return jsonify({"error": u"Não foi possível obter a cotação"}), 500

    converted_amount = (amount / from_rate) * to_rate

    return jsonify({
        "from": from_currency,
        "to": to_currency,
        "amount": amount,
        "converted_amount": converted_amount
    })

# Endpoint para adicionar uma nova moeda
@app.route('/currencies', methods=['POST'])
def add_currency():
    new_currency = request.json.get('currency')
    if new_currency not in supported_currencies:
        supported_currencies.append(new_currency)
        return jsonify({"message": u"Moeda adicionada com sucesso"}), 201
    return jsonify({"error": u"Moeda já existe"}), 400

# Endpoint para remover uma moeda
@app.route('/currencies', methods=['DELETE'])
def remove_currency():
    currency_to_remove = request.json.get('currency')
    if currency_to_remove in supported_currencies:
        supported_currencies.remove(currency_to_remove)
        return jsonify({"message": u"Moeda removida com sucesso"}), 200
    return jsonify({"error": u"Moeda não encontrada"}), 400

def get_real_rate(currency):
    response = requests.get(REAL_RATES_API)
    data = response.json()
    rates = data.get('rates', {})
    return rates.get(currency)

# Inicializa o servidor Flask
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000,debug=True)
