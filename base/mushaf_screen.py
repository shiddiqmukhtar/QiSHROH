from kivymd.app import MDApp

from kivy.uix.screenmanager import Screen
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.font_definitions import fonts
from kivymd.icon_definitions import md_icons
from kivy.properties import StringProperty

#from kivymd.icon_definitions import md_icons

from asset.qoryname import QoryName
#from base.main_screen import MainScreen

class Tab(FloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''
    text_tab = StringProperty()
    text = StringProperty()

class MushafScreen(Screen):
   
    title = StringProperty ("Mushaf Warsy")
    qory_name = QoryName()
    bg_toolbar = StringProperty("#006060")
    mushaf_imam = 'warsy'
    bg_mushaf = StringProperty('#B2DFDB')
    
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()
    
    def check_color(self, titles):
        if titles == "Mushaf Warsy":
            self.app.changes_status_bar('#004848', '#004848')
            self.bg_mushaf = '#B2DFDB'
            return "#006060" # Cyan, 900
        elif titles == "Mushaf Qolun":
            self.app.changes_status_bar('#B71C1C', '#b71c1c')
            self.bg_mushaf = '#FFCDD2'
            return "#c62828" 
        elif titles == "Mushaf Hafs":
            self.app.changes_status_bar('#880e4f', '#880e4f')
            self.bg_mushaf = '#F8BBD0'
            return "#ad1457"
        elif titles == "Mushaf Syu'bah":
            self.app.changes_status_bar('#4a148c', '#4a148c')
            self.bg_mushaf = '#E1BEE7'
            return "#6a1b9a"
        elif titles == "Mushaf Hisyam":
            self.app.changes_status_bar('#01579b', '#01579b')
            self.bg_mushaf = '#B3E5FC'
            return "#0277bd"
        elif titles == "Mushaf Ibnu Dzakwan":
            self.app.changes_status_bar('#1b5e20', '#1b5e20')
            self.bg_mushaf = '#C8E6C9'
            return "#2e7d32"
        elif titles == "Mushaf Ad Duuriy":
            self.app.changes_status_bar('#827717', '#827717')
            self.bg_mushaf = '#F0F4C3'
            return "#9e9d24"
        elif titles == "Mushaf As Suusiy":
            self.app.changes_status_bar('#ff6f00', '#ff6f00')
            self.bg_mushaf = '#FFECB3'
            return "#ff8f00"
        elif titles == "Mushaf Qunbul":
            self.app.changes_status_bar('#1a237e', '#1a237e')
            self.bg_mushaf = '#C5CAE9'
            return "#283593"
        elif titles == "Mushaf Al Bazziy":
            self.app.changes_status_bar('#bf360c', '#bf360c')
            self.bg_mushaf = '#FFCCBC'
            return "#d84315"
         
        #------------------#
        elif titles == "Mushaf Abu Al Harits":
            self.app.changes_status_bar('#ff6d00', '#ff6d00')
            self.bg_mushaf = '#FFCC80'
            return "#ff9100"
        elif titles == "Mushaf Khalaf":
            self.app.changes_status_bar('#0d47a1', '#0d47a1')
            self.bg_mushaf = '#BBDEFB'
            return "#1565c0"
        elif titles == "Mushaf Khallad":
            self.app.changes_status_bar('#33691e', '#33691e')
            self.bg_mushaf = '#BCEDC8'
            return "#558b2f"
        else:
            self.app.changes_status_bar('#f57f17', '#f57f17')
            self.bg_mushaf = '#FFF9C4'
            return "#f9a825"
    
    def changes_mushaf_screen(self, title):
        self.title = title
        self.num_color = self.check_color(title)
        self.bg_toolbar = self.num_color
        #self.app.changes_status_bar('#004848')
        
        
        
    def on_kv_post(self, base_widget):
        
        toolbr = self.ids["toolbar_mushaf"]
        toolbr.ids.label_title.font_style = "H6"
        #toolbr.ids.label_title.font_name = ".kivy/fonts/Robota-NonCommercial.otf"
        
        tabs = self.ids["tabs"]

        for tab_name in self.qory_name.name_surah:
            tab = Tab(text = f"[b][ref={tab_name}][b][font={fonts[-1]['fn_regular']}][/font][/ref][/b]  {tab_name}")
            tabs.add_widget(tab)
            
    def on_tab_switch(self,instance_tabs,instance_tab,instance_tab_label,tab_text):
        
        if self.mushaf_imam == 'warsy':
            instance_tab.ids.label.text = self.qory_name.warsy_text
        elif self.mushaf_imam == 'hafs':
            instance_tab.ids.label.text = self.qory_name.hafs_text
        elif self.mushaf_imam == 'syubah':
            instance_tab.ids.label.text = self.qory_name.syubah_text
        elif self.mushaf_imam == 'hisyam':
            instance_tab.ids.label.text = self.qory_name.hisyam_text
        elif self.mushaf_imam == 'ibnu dzakwan':
            instance_tab.ids.label.text = self.qory_name.ibnudzakwan_text
        elif self.mushaf_imam == 'ad duuriy':
            instance_tab.ids.label.text = self.qory_name.adduuriyA_text
        elif self.mushaf_imam == 'as suusiy':
            instance_tab.ids.label.text = self.qory_name.assuusiy_text
        elif self.mushaf_imam == 'al bazziy':
            instance_tab.ids.label.text = self.qory_name.albazziy_text
        elif self.mushaf_imam == 'qunbul':
            instance_tab.ids.label.text = self.qory_name.qunbul_text
        elif self.mushaf_imam == 'abu al harits':
            instance_tab.ids.label.text = self.qory_name.abualharits_text
        elif self.mushaf_imam == 'ad-duuriy':
            instance_tab.ids.label.text = self.qory_name.adduuriyK_text
        elif self.mushaf_imam == 'khalaf':
            instance_tab.ids.label.text = self.qory_name.khalaf_text
        elif self.mushaf_imam == 'khallad':
            instance_tab.ids.label.text = self.qory_name.khallad_text
        else:
            instance_tab.ids.label.text = self.qory_name.qolun_text