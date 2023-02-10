from app import create_app
from app.db import db

app=create_app()

@app.route('/',) #ruta raiz
def index():
    return "Inicio de una gran aventura"


db.init_app(app)
with app.app_context():
    db.create_all()
    print("Base de datos conectado!")

if __name__ == "__main__":
    app.run(debug=True)