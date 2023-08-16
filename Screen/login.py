import firebase_admin 
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.tools.hotreload.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from firebase_admin import credentials, auth, db, storage
import firebase_admin.auth as firebase_auth


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, name='my-app')


class Login(MDScreen):
    def login(self):
        email = self.ids.email_input.text
        password = self.ids.password_input.text

        try:
            user = auth.get_user_by_email(email)
            firebase_auth.verify_password(user.uid, password)
            # Login berhasil, arahkan ke halaman Home
            self.manager.current = "homescreen"
        except auth.AuthError as e:
            # Tampilkan pesan bahwa email atau password salah
            self.show_popup("Login Gagal", "Email atau password salah")
        except Exception as e:
            # Tampilkan pesan kesalahan
            self.show_popup("Login Gagal", str(e))                                      

    def show_popup(self, title, text):
        dialog = MDDialog(
            title=title,
            text=text,
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=self.close_popup
                )
            ],
        )
        dialog.open()

    def close_popup(self, instance):
        instance.parent.parent.dismiss()