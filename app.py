from flask import Flask, render_template, request

app = Flask(__name__)

def konversi_jarak(m):
    return {
        'km': m / 1000,
        'm': m,
        'cm': m * 100,
        'mm': m * 1000,
        'dam': m / 10,
        'hm': m / 100,
        'dm': m * 10,
    }
    
@app.route('/', methods=['GET', 'POST'])
def index():
    hasil_konversi = None
    faktor_dari_1meter = konversi_jarak(1) 
    
    if request.method == 'POST':
        try:
            nilai = float(request.form.get('nilai'))
            satuan_awal = request.form.get('satuan_awal')
            satuan_konversi = request.form.get('satuan_konversi')
            
            nilai_satuan_awal1m = faktor_dari_1meter.get(satuan_awal)
            
            if nilai_satuan_awal1m is None:
                hasil_konversi = "Error: Satuan awal tidak didukung (hanya km, m, cm, mm, dam, hm, dm)."
                
            else:
                faktor_ke_meter = 1 / nilai_satuan_awal1m
                nilai_dalam_meter = nilai * faktor_ke_meter
                
                hasil_konversi_jadi = konversi_jarak(nilai_dalam_meter) 
                hasil_akhir = hasil_konversi_jadi.get(satuan_konversi)
                
                if hasil_akhir is None:
                    hasil_konversi = "Error: Satuan konversi tujuan tidak didukung."
                else:
                    hasil_konversi = f"{nilai} {satuan_awal} = {hasil_akhir:.1f} {satuan_konversi}"
                
        except ValueError:
            hasil_konversi = "Error: Input nilai harus berupa angka yang valid."
        except Exception as e:
            hasil_konversi = f"Terjadi kesalahan: {e}"

    return render_template(
        'index.html', 
        units=list(faktor_dari_1meter.keys()), 
        hasil=hasil_konversi
    )
app = app

if __name__ == '__main__':
    app.run(debug=True)




# from flask import Flask, render_template, request, redirect, url_for

# app = Flask(__name__)

# def konversi_jarak (m) : 
#     return {
#     'km':m / 1000,
#     'm': m,
#     'cm': m * 100,
#     'mm': m * 1000,
#     'dam': m / 10,
#     'hm' : m / 100,
#     'dm' : m * 10,
# }

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     hasil_konversi = None
    
#     if request.method == 'POST':
#         try:
#             nilai = float(request.form.get('nilai'))
#             satuan_awal = request.form.get('satuan_awal')
#             satuan_konversi = request.form.get('satuan_konversi')
            
#             faktor_awal = konversi_jarak.get(satuan_awal)
#             faktor_konversi = konversi_jarak.get(satuan_konversi)
            
#             if faktor_awal is None or faktor_konversi is None:
#                 hasil_konversi = "Error: Satuan tidak valid."
#             else:
#                 nilai_dalam_meter = nilai * faktor_awal
#                 hasil_akhir = nilai_dalam_meter / faktor_konversi
#                 hasil_konversi = f"{nilai} {satuan_awal} = {hasil_akhir:.4f} {satuan_konversi}"
                
#         except ValueError:
#             hasil_konversi = "Error: Input nilai harus berupa angka."
#         except Exception as e:
#             hasil_konversi = f"Terjadi kesalahan: {e}"

#     return render_template(
#         'index.html', 
#         units=list(konversi_jarak(1).keys()), 
#         hasil=hasil_konversi
#     )

# if __name__ == '__main__':
#     app.run(debug=True)





# from flask import Flask, request, render_template

# app = Flask(__name__)

# def calculate_factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * calculate_factorial(n-1)
    
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     result = None
#     if request.method == 'POST':
#         try:
#             number = int(request.form.get('number'))
#             result = calculate_factorial(number)
#         except ValueError:
#             result = "Invalid input. Please enter an integer."
#     return render_template('index.html', result=result)
    
# if __name__ == '__main__':
#     app.run(debug=True)
    

# from flask import Flask, request

# app = Flask (__name__)

# @app.route("/greet",methods=["POST"])
# def greet_post():
#     name = request.form.get("name","Guest")
#     return f"Hello, {name}!"

# if __name__ == '__main__':
#     app.run(debug=True)
    


