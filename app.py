from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

orders = []
order_no = 1


## HTML을 주는 부분
@app.route('/')
def home():
    return 'This is Home!'


@app.route('/mypage')
def mypage():
    return render_template('index.html')


## API 역할을 하는 부분
@app.route('/post', methods=['POST'])
def post():
    global orders
    global order_no

    name_receive = request.form['name_give']
    quan_receive = request.form['quan_give']
    address_receive = request.form['address_give']
    contact_receive = request.form['contact_give']

    order = {'no': order_no
                ,'name': name_receive
                ,'quan': quan_receive
                ,'address': address_receive
                ,'contact': contact_receive}  # 받은 걸 딕셔너리로 만들고,

    order_no = order_no + 1

    orders.append(order)  # 넣는다

    return jsonify({'result': 'success'})


@app.route('/post', methods=['GET'])
def view():
    return jsonify({'result': 'success', 'orders': orders})


@app.route('/orders', methods=['GET'])
def order_list():
    return render_template('orders.html')


@app.route('/delete', methods=['post'])
def delete():
    global orders
    no_receive = request.form['no_give']  # 클라이언트로부터 no를 받는 부분

    for order in orders:  # 반복문: orders를 돌면서,
        if str(order['no']) == no_receive:  # 조건문: 받은 no와 같은 번호의 아티클을 찾아서 (단, 문자열 == 문자열로!)
            orders.remove(order)  # 해당 order을 지우고,
            return jsonify({'result': 'success'})  # 결과를 주고 함수를 끝낸다.

    return jsonify({'result': 'fail', 'msg': '아티클이 없습니다'})  # 만약 반복문을 다 돌아도 결과를 주지 않았으면, 아티클이 없다고 한다.


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)