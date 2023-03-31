from flask import Flask, render_template, jsonify

app = Flask(__name__, template_folder='app/templates', static_folder='app/static')
 
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/button<int:button_id>')
def press(button_id):
    print('ere')
    print(button_id)

    return jsonify({'message': 'dummy'})

if __name__ == '__main__':
    app.run(debug=True)