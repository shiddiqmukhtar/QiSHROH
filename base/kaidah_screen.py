from kivymd.app import MDApp

from kivy.uix.screenmanager import Screen
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.font_definitions import fonts
from kivymd.icon_definitions import md_icons
from kivymd.uix.tab import MDTabsBase
from kivy.properties import StringProperty

from asset.qoryname import QoryName
from base.main_screen import MainScreen


class Tab(MDFloatLayout, MDTabsBase):
    
    text_tab = StringProperty()

    
class KaidahScreen(Screen):
   
    title = StringProperty ("Kaidah Baca")
    qory_name = QoryName()
    bg_kaidah = StringProperty('#B2DFDB')
    bg_toolbar = StringProperty("#006060")
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()
        
    def on_kv_post(self, base_widget):
        toolbr = self.ids["toolbar_kaidah"]
        toolbr.ids.label_title.font_style = "H6"
        #toolbr.ids.label_title.font_name = ".kivy/fonts/Robota-NonCommercial.otf"
        
        tabs = self.ids["tabs"]
        
        for tab_name in self.qory_name.name_qory:
            tab = Tab(text = f"[b][ref={tab_name}][b][font={fonts[-1]['fn_regular']}][/font][/ref][/b]  {tab_name}")
            tabs.add_widget(tab)
    
    def on_tab_switch(self,instance_tabs,instance_tab,instance_tab_label,tab_text):
            
        instance_tab.ids.label.text = self.qory_name.qolun_text