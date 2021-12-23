from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.properties import ConfigParserProperty
from kivymd.uix.taptargetview import MDTapTargetView
from kivy.clock import Clock
from base.login_screen import LoginScreen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog

#import kivy.utils.get_hex_from_color as rgb


import bidi.algorithm

from arabic_reshaper import ArabicReshaper

import sys

class MainScreen(Screen):
    
    dialog = None
    
    nickname = ConfigParserProperty(
        '', 'qishroh', 'nickname',
        'app', val_type=str
    )
    surel = ConfigParserProperty(
        '', 'qishroh', 'surel',
        'app', val_type=str
    )
    keyword = ConfigParserProperty(
        '', 'qishroh', 'keyword',
        'app', val_type=str
    )
    sigin = ConfigParserProperty(
        '', 'qishroh', 'sigin',
        'app', val_type=int
    )
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()
        #self.log = LoginScreen()
        
        configuration = {
        'delete_harakat': False,
        'shift_harakat_position': False,
        'delete_tatweel': False,
        'use_unshaped_instead_of_isolated': False,
        'support_ligatures': True,
        'RIAL SIGN': True,
        }
        
        reshaper = ArabicReshaper(configuration=configuration)
        
        sub_title2 ="""مخترصديق"""
        
        sub_title1 = reshaper.reshape(sub_title2)

        self.sub_title = bidi.algorithm.get_display(sub_title1)
     
    def on_kv_post(self, base_widget):
        print('on kv post 1')
        self.tap_target_view = MDTapTargetView(
            #widget = self.ids['button'], # eq
            widget = self.ids.button,
            title_text = '[size=60][b][color=#ffd600]QiSH[/color][/b][color=#c0c0c0]ROH[/color][sup][color=#ffd600]©[/color][/sup][/size]',
            description_text = f"[size=25][color=#000000]email:[/color][/size]\n[b][size=30]{self.surel}[/b][/size]",
            widget_position = "left_top",
            #title_position = 'left_top',
            #outer_circle_color = (0, .35, .35),
            outer_circle_color = (.8, 0, 0), # (0, 0.27, 0.27),
            target_circle_color = (.9, .9, .9),
            #outer_circle_alpha = .2 # default .96,
            draw_shadow = True,
            #target_radius = 90,
        )
        
    def tap_target_start(self):
        print('start login call')
        self.surel = LoginScreen().surel
        print('stop login call')
        if self.tap_target_view.state == "close":
            print('start-start tap target')
            self.tap_target_view.start()
        else:
            print('stop-start tap target')
            self.tap_target_view.stop()
            
    def close_dialog(self, obj):
        self.dialog.dismiss()
            
    def log_out(self):
        self.dialog = MDDialog(
        title="[color=#aa0000][b][size=40]Caution..![/size][/b][/color]",
            #radius=[30, 30, 30, 30],
            text="[i][color=#006060][size=25]{}[/size][/i][/color]\n[color=#202020]Are you sure to log-out?[/color]".format(self.surel), 
            size_hint=(0.7, 1),
            buttons=[
                MDFlatButton(
                    text='CANCEL',
                    #text_color= app.theme_cls.primary_color,
                    text_color= (0, .35, .35, 1),
                    on_release=self.close_dialog),                              
                MDRectangleFlatButton(
                    text='YES',
                    text_color= (0, .35, .35, 1),
                    on_release= self.exite
                )
            ]
        )
        self.dialog.open()
        
    
    def exite(self, obj):
        self.dialog.dismiss()
        #self.log.logout()
        nickname = ''
        self.sigin = 0
        self.surel = 'anonymous'
        self.keyword = None
        sys.exit()
        