import os
from flask import Flask, send_file, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return send_file('src/index.html')

@app.route("/sozluk")
def sozluk():
    dictionary = {"elma": "apple", "armut": "pear", "muz": "banana"}
    return render_template("sozluk.html", data=dictionary)

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
    @app.route("/ara", methods=["POST"])
def ara():
    from flask import request

    dictionary = {"elma": "apple", "armut": "pear", "muz": "banana"}
    images = {"elma": "elma.jpg", "armut": "armut.jpg", "muz": "muz.jpg"}

    kelime = request.form.get("kelime")
    sonuc = dictionary.get(kelime)
    resim = images.get(kelime)

    if sonuc and resim:
        return render_template("sonuc.html", kelime=kelime, anlam=sonuc, resim=resim)
    else:
        return "Kelime bulunamadı.", 404