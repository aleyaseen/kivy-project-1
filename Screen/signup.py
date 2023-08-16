import os, cv2, face_recognition, base64, pickle
import firebase_admin 
from kivymd.tools.hotreload.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from firebase_admin import credentials, db, storage, auth

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://absensiwajahrealtime-default-rtdb.firebaseio.com/",
    'storageBucket': "absensiwajahrealtime.appspot.com"
})

class Signup(MDScreen):
    def signup(self, data):
        full_name = self.ids.full_name_input.text
        email = self.ids.email_input.text
        password = self.ids.password_input.text

        # Membuat user di Firebase Authentication
        try:
            user = auth.create_user(
                email=email,
                password=password,
                display_name=full_name
            )
            print("Pendaftaran berhasil! UID pengguna:", user.uid)
        except Exception as e:
            print("Gagal mendaftar:", str(e))
                