from flask import Flask, render_template, request, send_file
import qrcode
import io

app = Flask(__name__)

# Esta parte le dice a Python qué mostrar cuando alguien entra a la página
@app.route('/')
def index():
    return render_template('index.html')

# Esta parte procesa el link y genera el QR
@app.route('/generar', methods=['POST'])
def generar_qr():
    # 'qr_link' es el nombre que le daremos a la cajita en el HTML
    link = request.form.get('qr_link')
    
    # Creamos el QR (tu lógica original)
    img = qrcode.make(link)
    
    # Guardamos la imagen en la memoria RAM para enviarla rápido
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)
    
    return send_file(buf, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)