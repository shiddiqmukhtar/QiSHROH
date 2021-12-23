from kivy.uix.screenmanager import Screen
from kivy.properties import ColorProperty

class WelcomeScreen(Screen):
    
    col_spin = ColorProperty([.7, .7, .7, 1])
    
    hadits_nabi ="""[color=#c0c0c0][b]Hadits:[/b]
  
"Sebaik-baik dari kalian adalah
 yang  mempelajari  [color=#ffd700]Al-Quran[/color] dan 
 mengajarkannya."[/color]"""