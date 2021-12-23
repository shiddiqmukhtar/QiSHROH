from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.uix.screenmanager import Screen
from kivy.properties import (
    BooleanProperty,
    StringProperty, 
    ConfigParserProperty
    )
from kivy.animation import Animation
from kivymd.app import MDApp

from base.main_screen import MainScreen
from base.signup_screen import SignupScreen
from base.reset_password_screen import ResetPasswordScreen

import pyrebase

firebaseConfig={'apiKey' : "AIzaSyDEn2FDVx2VxrHHEwviUseSB9N4Qh-h6t0",
    'authDomain': "kivyproject-b1866.firebaseapp.com",
    'databaseURL': "https://kivyproject-b1866-default-rtdb.firebaseio.com",
    'projectId': "kivyproject-b1866",
    'storageBucket': "kivyproject-b1866.appspot.com",
    'messagingSenderId': "1001884580697",
    'appId': "1:1001884580697:web:3bd48e3528f105f2e66a48",
    'measurementId': "G-QHRQ5MKVWM"};
    
firebase=pyrebase.initialize_app(firebaseConfig)

auth=firebase.auth()

class LoginScreen(Screen):
    
    nickname = ConfigParserProperty(
        '',
        'qishroh',
        'nickname',
        'app',
        val_type=str
    )
    
    surel = ConfigParserProperty(
        '',
        'qishroh',
        'surel',
        'app',
        val_type=str
    )
    
    keyword = ConfigParserProperty(
        '',
        'qishroh',
        'keyword',
        'app',
        val_type=str
    )
    
    def logout(self):
        print('LOGOUT')
        auth.sign_out()
        
    
    def login(self):
        
        self.app = MDApp.get_running_app()
        email_text = self.ids.email.text
        pwd_text = self.ids.password.text
        
        # Check validitate of email & password
        if email_text.split() == [] or pwd_text.split() == []:
            # if user (username or email or password is blank)
            self.invalid_input()
            
        elif len(email_text.split())>1 or len(pwd_text.split())>1:
            # if username or password cont. space
            self.invalid_input()
            
        else:
            try:
                auth.sign_in_with_email_and_password(email_text, pwd_text)
                
                self.sigin = 1
                self.surel = email_text
                self.success()
                
                # kalau beres arahkan ke "main" screen
                self.manager.current = 'main' 
                self.manager.transition.direction = 'up'
            except:
                #print('ERROR')
                self.manager.current = 'login'
                self.manager.transition.direction = 'up'
                self.unsuccess()
        
    def invalid_input(self):
        self.cancel_btn_username_dialogue = MDFlatButton(text='Retry',on_release = self.close_username_dialogue)
        self.dialog = MDDialog(title = 'Invalid Data',text = 'Please enter email or password',size_hint = (0.7, 0.2),buttons = [self.cancel_btn_username_dialogue])          
        self.dialog.open()
        
        
    def unsuccess(self):
        self.cancel_btn_username_dialogue = MDFlatButton(text='Retry',on_release = self.close_username_dialogue)
        self.dialog = MDDialog(title = 'Unsuccess',text = 'Invalid email or password..!',size_hint = (0.7, 0.2),buttons = [self.cancel_btn_username_dialogue])          
        self.dialog.open()
        
        
    def success(self):
        self.cancel_btn_username_dialogue = MDFlatButton(text='Oke..',on_release = self.close_username_dialogue)
        self.dialog = MDDialog(title = 'Successfully..!',text = "Thank's, continue please...",size_hint = (0.7, 0.2),buttons = [self.cancel_btn_username_dialogue])          
        self.dialog.open()
        
    def close_username_dialogue(self,obj):
        self.dialog.dismiss()
        
#---------------- Animation -----------------#
        
    def anim(self, widget):
        anim = Animation(pos_hint={'center_y': 1.17})
        anim.start(widget)
        
    def anim1(self, widget):
        anim = Animation(pos_hint={'center_y': .95})
        anim.start(widget)
        
    def icons(self, widget):
        anim = Animation(pos_hint={'center_y': .75}, opacity=0)
        anim += Animation(pos_hint={'center_y': .88}, opacity=1, duration=1.5)
        anim.start(widget)
        
    def text(self, widget):
        anim = Animation(duration=2.5, opacity=0)
        anim += Animation(opacity=1)
        
        anim.start(widget)