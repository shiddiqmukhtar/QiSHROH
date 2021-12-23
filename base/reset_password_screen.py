from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.uix.screenmanager import Screen
from kivy.animation import Animation
from kivy.properties import ConfigParserProperty

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

#---------------------- reset password ----------------------#
 
class ResetPasswordScreen(Screen):
    
    surel = ConfigParserProperty(
        '',
        'qishroh',
        'surel',
        'app',
        val_type=str
    )
    
    
    kata_bijak = """
        [color=#004848]"Istiqamah dalam Agama [color=#ff0000][b][i]Allah[/i][/b][/color] membuat orang lebih awal masuk [color=#00aa00][b][i]'surga'[/i][/b][/color], dan kekal di dalamnya."[/color]"""
    
    def reset(self):
        email_text = self.ids.password_reset.text
        
        # get email of user
        if email_text.split() == [] or len(email_text.split())>1:
            
            # Open notification
            self.cancel_btn_username_dialogue = MDFlatButton(text='Retry',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'Invalid Data',text = 'Please enter email!',size_hint = (0.7,0.2),buttons = [self.cancel_btn_username_dialogue])
            
            self.dialog.open()
        else:
            try:
                auth.send_password_reset_email(email_text)
                
                # Open notification
                self.cancel_btn_username_dialogue = MDFlatButton(text='Okey..!',on_release = self.close_username_dialogue)
                self.dialog = MDDialog(title = 'Successfully to reset password!',text = 'Please Check your Email!',size_hint = (0.7,0.2),buttons = [self.cancel_btn_username_dialogue])
                self.dialog.open()
            
                self.manager.current = 'login'
                self.manager.transition.direction = 'right'
                
            except:
                # Open notification
                self.cancel_btn_username_dialogue = MDFlatButton(text='Retry',on_release = self.close_username_dialogue)
                self.dialog = MDDialog(title = 'Invalid Email',text = 'Please enter email..!',size_hint = (0.7,0.2),buttons = [self.cancel_btn_username_dialogue])
            
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