from app import create_app, db

def reset_database():
    app = create_app()
    with app.app_context():
        db.drop_all()
        db.create_all()
        print("Banco de dados reiniciado com sucesso!")

if __name__ == '__main__':
    reset_database()
