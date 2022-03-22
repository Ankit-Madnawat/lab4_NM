try:
    from flask import Flask, request,render_template
    from napalm import get_network_driver
    import GET_CONFIG
    import DIFF_CONFIG
    import OSPF_CONFIG
except:
    print("Install necessary modules")


app = Flask(__name__)

@app.route('/')
def index():    
    return render_template('index.html')

@app.route('/Get_Config', methods=['GET', 'POST'])
def Get_Config():
    data = GET_CONFIG.config_call()
    print(data)
    if request.method == 'GET':
        bodyText = data
        return render_template('Get_config.html', bodyText=bodyText)

@app.route("/OSPF_Config")
def OSPF_Config():
    return render_template('OSPF_config.html')

@app.route("/result", methods = ['GET', 'POST'])
def result():
    data = OSPF_CONFIG.database()
    if request.method == 'POST':
        bodyText = data
        return render_template('result.html', bodyText=bodyText)

@app.route('/Diff_Config', methods=['GET', 'POST'])
def Diff_Config():
    diff = DIFF_CONFIG.difference()
    print(diff)
    if request.method == 'GET':
        bodyText = diff
        return render_template('Diff_config.html', bodyText=bodyText)


if __name__ == "__main__":
    app.run(debug=True)
