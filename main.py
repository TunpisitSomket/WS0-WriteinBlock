from package.sayhi import Blockchain
from flask import Flask, request, render_template


app = Flask(__name__)
blockchain = Blockchain()


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', data=blockchain.hi())


@app.route('/set_name', methods=['POST'])
def set_name():
    name = request.json['name']
    transaction_receipt = blockchain.set_name(name)
    return transaction_receipt


if __name__ == '__main__':
    app.run(debug=True)
