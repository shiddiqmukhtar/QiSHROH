# Project Firebase = KivyProject
#:import rgba kivy.utils.get_color_from_hex

from base.welcome_screen import WelcomeScreen
from base.login_screen import LoginScreen
from base.main_screen import MainScreen

from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivy.lang import Builder
from kivy.clock import Clock
from kivymd.toast.kivytoast.kivytoast import toast
#from kivymd.toast import  kivytoast
#from kivy.factory import Factory
from kivy.properties import ConfigParserProperty

# import module scan keypad
from kivy.base import EventLoop

#from kivy.uix.screenmanager import Screen

#----------- start block statusbar-----------#

from kivy.uix.boxlayout import BoxLayout

from android.runnable import run_on_ui_thread
from jnius import autoclass

#--------- start block orientation ----------#

from plyer import orientation

#from kivy.config import Config
#Config.set("kivy", "log_level", "error")
#Config.write()


Color = autoclass("android.graphics.Color")
WindowManager = autoclass('android.view.WindowManager$LayoutParams')
activity = autoclass('org.kivy.android.PythonActivity').mActivity

class StatusBar:
    
    @run_on_ui_thread
    def statusbar(self, color1,color2):
        window = activity.getWindow()
        window.clearFlags(WindowManager.FLAG_TRANSLUCENT_STATUS)
        window.addFlags(WindowManager.FLAG_DRAWS_SYSTEM_BAR_BACKGROUNDS)
        window.setStatusBarColor(Color.parseColor(color1))
        
        # set color to bottom bar
        window.setNavigationBarColor(Color.parseColor(color2))

#----------- end block statusbar ------------#

class QishrohApp(MDApp):
    teal = "#004848"
    black = "#202020"
    
    sigin = ConfigParserProperty(
        '', 'qishroh', 'sigin',
        'app', val_type=int
    )
    
    def build_config(self, config):
        config.setdefaults(
            'qishroh',
            {
                'nickname': 'username',
                'surel': 'email',
                'keyword': 'password',
                'sigin': 0
            }
        )
    
    def build(self):
        #self.toast = Factory.Toast(duration = 6.0)
        self.theme_cls = ThemeManager()
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.primary_hue = "900"
        #self.theme_cls.accent_palette = 'Amber'
        #self.theme_cls.accent_hue = '400'
        
        self.strng = Builder.load_file('qishroh.kv')
        
        return self.strng
            
            
    def main_screen_call(self, dt):
        self.changes_status_bar(self.teal, self.black)
        self.strng.get_screen('main').manager.current = 'main'
        self.strng.get_screen('main').manager.transition.direction = 'down'
        
        
        
    def login_screen_call(self, dt):
        self.strng.get_screen('login').manager.current = 'login'
        self.strng.get_screen('login').manager.transition.direction = 'left'
        
        
    def changes_status_bar(self, colr1,colr2):
        statusBar = StatusBar()
        statusBar.statusbar(colr1, colr2)
        
            
    def on_start(self):
        
        EventLoop.window.bind(on_keyboard=self.hook_keyboard) 
        
        
#------------ rotation bloced ---------------#
        
        # Set orientation -> portrait
        orientation.set_portrait()
        #orientation.set_landscape()
        
#----------- color statusbar call -----------#
        
        #self.changes_status_bar(self.teal, self.black)
        
        if QishrohApp().sigin == 1:
            Clock.schedule_once(self.main_screen_call, 0)
            
        # If login status
        else:
            Clock.schedule_once(self.login_screen_call, 0)
            
            
#----------- back button blocked ------------#


#-------------- toast display ---------------#
            
    def hook_keyboard(self, window, key, *largs):
        if key == 27:
            toast("\n     Long press, or Log-out at HOME..!!     \n")
            return True      
        else:
            pass
            
    def on_pause(self):
        toast("thank's")
        
        
if  __name__ == "__main__":
    QishrohApp().run()