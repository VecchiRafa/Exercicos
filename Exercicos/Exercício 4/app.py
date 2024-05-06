from flask import Flask, render_template

app= Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quarto')
def quarto():
    return render_template('quarto.html')

@app.route('/quarto/luminosidade')
def luminosidade():
    return render_template('luminosidade.html')

@app.route('/quarto/interruptor')
def interruptor():
    return render_template('interruptor.html')

@app.route('/banheiro')
def banheiro():
    return render_template('banheiro.html')

@app.route('/banheiro/umidade')
def umidade():
    return render_template('umidade.html')

@app.route('/banheiro/lampada')
def lampada():
    return render_template('lampada.html')

if __name__ == "__main__":  
    app.run(host='0.0.0.0', port=8080, debug=True)
