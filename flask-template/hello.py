from flask import Flask, request, render_template, url_for
import os
import time

app = Flask(__name__)

# Konfigurasi direktori upload
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'uploads')

# Pastikan folder upload ada
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Ambil data dari form
        nama = request.form['nama']
        email = request.form['email']
        hp = request.form['hp']
        prodi = request.form['prodi']

        # Cek jika ada file yang diunggah
        foto = request.files['foto']
        if foto:
            # Membuat nama file unik dengan timestamp
            timestamp = str(int(time.time()))
            ext = foto.filename.split('.')[-1]
            unique_filename = f"{timestamp}.{ext}"
            foto_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
            foto.save(foto_path)
            foto_path = f'uploads/{unique_filename}'  # Simpan path relatif
        else:
            foto_path = None

        # Pesan konfirmasi
        confirmation_message = f"Thank you, {nama}. Your registration has been received!"

        return render_template('register.html', confirmation_message=confirmation_message,
                               nama=nama, email=email, hp=hp, prodi=prodi, foto=foto_path)

    # Render halaman registrasi kosong untuk metode GET
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
