from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
import subprocess
import sys
import os

class LoginApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_file('login.kv')
    
    def login(self):
        username = self.root.ids.user.text
        password = self.root.ids.password.text
        
        if username == "admin" and password == "password123":
            print('Login successful')           
            
            if sys.platform == 'win32':
                subprocess.Popen([sys.executable, 'authentech visvas/frontend/main.py'])
            sys.exit()
            # Close the current login window
            
        else:
            print('Invalid username or password')
    
    def clear(self):
        self.root.ids.user.text = ''
        self.root.ids.password.text = ''

if __name__ == '__main__':
    LoginApp().run()