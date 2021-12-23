from kivy.uix.screenmanager import Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
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

#---------------------------signup----------------------------------  
 
class SignupScreen(Screen):
    
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
    
    def signup(self):
        
        # get name of user
        self.username_text = self.ids.username.text
        
        # get address email of user
        self.email_text = self.ids.email.text
        
        # get password of user
        self.password_text = self.ids.password.text
        
        # Check validitas user
        # self.username_text.split() == [] or
        if self.username_text.split() == [] or self.password_text.split() == [] or self.email_text.split() == []:
            # if user (username or email or password is blank)
            self.cancel_btn_username_dialogue= MDFlatButton(text = 'Retry',on_release=self.close_username_dialogue)
                    
            # initialize dialog
            self.dialog = MDDialog(title = 'Invalid Input',text = "Please enter a valid input",size_hint = (0.7,0.2),buttons = [self.cancel_btn_username_dialogue])
            
            # Open dialog
            self.dialog.open()
            
        # if user contain space    
        elif len(self.username_text.split())>2:
            
            self.cancel_btn_username_dialogue = MDFlatButton(text = 'Retry',on_release = self.close_username_dialogue)
            
            # Open notification
            self.dialog = MDDialog(title = 'Invalid Username',text = 'Please enter username max. one space',size_hint = (0.7,0.2),buttons = [self.cancel_btn_username_dialogue])
                
            self.dialog.open()
            
        else:
            try:
                auth.create_user_with_email_and_password(self.email_text, self.password_text)
                self.manager.current = 'login'
                self.manager.transition.direction = 'left'
                self.success()
                
            except:
                
                self.cancel_btn_username_dialogue = MDFlatButton(text = 'Retry',on_release = self.close_username_dialogue)
                self.dialog = MDDialog(title = 'Invalid Data',text = 'Please enter valid data!',size_hint = (0.7,0.2),buttons = [self.cancel_btn_username_dialogue])
                self.dialog.open()
        
    def success(self):
        self.cancel_btn_username_dialogue = MDFlatButton(text='Okey',on_release = self.close_username_dialogue)
        self.dialog = MDDialog(title = 'Successfully..!',text = 'Thanks, for registeration..!',size_hint = (0.7,0.2),buttons = [self.cancel_btn_username_dialogue])          
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