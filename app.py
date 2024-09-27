from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
from main import create_withdraw_order

app = Flask(__name__)
load_dotenv()  # Load environment variables from the .env file

@app.route('/withdraw', methods=['POST'])
def withdraw():
    try:
        data = request.get_json()
        if 'password' not in data or data['password'] != os.getenv('ROUTE_PASSWORD'):
            return jsonify({"error": "Wrong password"}), 401  # Unauthorized access

        params = {
            "chain": data.get('chain'),  # Required; ensure the client sends this
            "market_token_symbol": data.get('market_token_symbol'),  # Required
            "out_token_symbol": data.get('out_token_symbol'),  # Required
            "gm_amount": int(data.get('gm_amount', 0))  # Default can be set if necessary, converted to int
        }

        order = create_withdraw_order(params)
        return "order exeuted"
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))

# curl -X POST http://127.0.0.1:5000/withdraw -H "Content-Type: application/json" -d '{
#     "chain": "arbitrum",
#     "market_token_symbol": "ETH",
#     "out_token_symbol": "USDC",
#     "gm_amount": "3",
#     "password": "yourPassword"
# }'
