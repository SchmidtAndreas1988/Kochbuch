from app import db, app

with app.app_context():
    db.drop_all()
    print("Alle Tabellen wurden gelöscht.")