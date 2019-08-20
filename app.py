# import の実行
from flask import Flask,jsonify,request,json

# インスタンスの作成
app = Flask(__name__)
items = []
programs = []
program = []

#programs作成
f = open('data.json','r')
dict_data = json.load(f)

for i in dict_data['results']:
        programs.append(dict_data['results'])
print(type(programs))

# URL, Methodと関数の紐づけ
@app.route('/item', methods=['POST'])
def make_item():
    item = request.get_json()
    items.append(item)
    return jsonify(item)


@app.route('/', methods=['POST'])
def make():
    item = {'name':'chair', 'price':5000}
    items.append(item)
    return jsonify(item)

@app.route('/jsn')
def home_json():
    return jsonify({'message' : 'hello_world'})

@app.route('/hw')
def home():
    return 'Hello World'

@app.route('/item/<name>')
def name_disp(name):
    return name

@app.route('/programs')
def all_movie():
    return jsonify(programs)

@app.route('/programs/<input_broadcast>')
def movie_service(input_broadcast):
        for i in dict_data['results']:
            if i['broadcasted_on'] == input_broadcast:
                program.append(i)
        return jsonify(program)

@app.route('/program/', methods=['POST'])
def movie_add():
    item = request.get_json()
    dict_data['results'].append(item)
    return jsonify(dict_data)

# サーバの起動
if __name__ == '__main__':
    app.run()

#app.run(host='0.0.0.0', port=80, debug=True)
