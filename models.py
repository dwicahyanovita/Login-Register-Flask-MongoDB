from flask import jsonify, request, session, redirect
from passlib.hash import pbkdf2_sha256
from datetime import datetime
import uuid, re

class User:
    def __init__(self, db):
        self.db = db
    
    def start_session(self, user):
        session['logged_in'] = True
        session['user'] = user
        return jsonify(user), 200
        
    def register(self):
        print(request.form)
        now = datetime.utcnow()

        user = {
            "_id": uuid.uuid4().hex,
            "username": request.form.get('username'),
            "email": request.form.get('email'),
            "password": request.form.get('password'),
            "created_at": now.isoformat(),
            "last_login": None
        }

        # Validasi password
        password = user['password']
        if len(password) < 8:
            return jsonify({"error": "Password minimal 8 karakter"}), 400
        if not re.search(r"[A-Z]", password):
            return jsonify({"error": "Password harus mengandung huruf besar"}), 400
        if not re.search(r"[a-z]", password):
            return jsonify({"error": "Password harus mengandung huruf kecil"}), 400
        if not re.search(r"[0-9]", password):
            return jsonify({"error": "Password harus mengandung angka"}), 400
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            return jsonify({"error": "Password harus mengandung simbol"}), 400

        # Enkripsi
        user['password'] = pbkdf2_sha256.encrypt(user['password'])

        # Cek duplikat
        if self.db.users.find_one({"username": user['username']}):
            return jsonify({"error": "Username sudah terdaftar, gunakan username lain!"}), 400
        if self.db.users.find_one({"email": user['email']}):
            return jsonify({"error": "Email sudah terdaftar, gunakan email lain!"}), 400

        try:
            self.db.users.insert_one(user)
            return jsonify({"success": "Berhasil register, silakan login!"})
        
        except Exception as e:
            print(e)
            return jsonify({"error": "Register gagal"}), 500

    def login(self):
        user = self.db.users.find_one({
            "email": request.form.get('email')
        })
        
        if user and pbkdf2_sha256.verify(request.form.get('password'), user['password']):
            last_login_time = datetime.utcnow().isoformat()
            self.db.users.update_one(
                {"_id": user["_id"]}, 
                {"$set": { "last_login": last_login_time }}
            )
            user['last_login'] = last_login_time
            return self.start_session(user)

        return jsonify({ "error": "Email atau password salah"}), 401
    ({ "error": "Invalid login credentials"}), 401
        
    def signout(self):
        session.clear()
        return redirect('/')
        
        
    
    