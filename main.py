from kivymd.app import MDApp
from kivy.lang import Builder

KV= '''
MDBoxLayout:
    orientation: 'vertical'
    FloatLayout:
        MDIconButton:
            pos_hint: {'center_x': 0.5,'center_y': 0.8}
            icon: "logoFoxSemFundo.png"
            icon_size: "300sp"
            
        MDLabel:
            text: "RAPOSINHA SAPECA"
            halign: "center"
            color: app.theme_cls.primary_color
            font_style: "H4"
            font_name:"Baygo" 
            pos_hint: {'center_x': 0.5, 'center_y': 0.68}
        
        MDLabel:
            text: "Digite sua senha de acesso"
            halign: "center"
            color: app.theme_cls.primary_color
            font_style: "Subtitle1"
            font_name:"Baygo" 
            pos_hint: {'center_x': 0.5, 'center_y': 0.56}
            
        MDTextField:
            id: password_field
            hint_text: "Senha"
            password: True
            multiline:False
            readonly:True
            icon_left: "key-variant"
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            size_hint_x: .4
            
        MDIconButton:
            icon: "eye-off"
            pos_hint: {"center_x":.65,"center_y": .5}
            pos: password_field.width - self.width + dp(8), 0
            theme_text_color: "Hint"
            on_release:
                self.icon = "eye" if self.icon == "eye-off" else "eye-off"
                password_field.password = False if password_field.password is True else True
            
            
        MDRaisedButton:
            text: "1"
            font_name:"Baygo" 
            md_bg_color: app.theme_cls.primary_color
            halign: "center"
            pos_hint: {'center_x': .34, 'center_y': .4}
            size_hint: (0.1, 0.1)
            font_size: "25sp"
            on_release: app.button_click("1")
        
        MDRaisedButton:
            text: "2"
            font_name:"Baygo" 
            md_bg_color: app.theme_cls.primary_color
            halign: "center"
            pos_hint: {'center_x': .5, 'center_y': .4}
            size_hint: (0.1, 0.1)
            font_size: "25sp"
            on_release: app.button_click("2")
                
        MDRaisedButton:
            text: "3"
            font_name:"Baygo" 
            md_bg_color: app.theme_cls.primary_color
            halign: "center"
            pos_hint: {'center_x': 0.66, 'center_y': .4}
            size_hint: (0.1, 0.1)
            font_size: "25sp"
            on_release: app.button_click("3")
            
        MDRaisedButton:
            text: "4"
            font_name:"Baygo" 
            md_bg_color: app.theme_cls.primary_color
            halign: "center"
            pos_hint: {'center_x': 0.34, 'center_y': 0.29}
            size_hint: (0.1, 0.1)
            font_size: "25sp"
            on_release: app.button_click("4")
        
        MDRaisedButton:
            text: "5"
            font_name: "Baygo" 
            md_bg_color: app.theme_cls.primary_color
            halign: "center"
            pos_hint: {'center_x': 0.5, 'center_y': 0.29}
            size_hint: (0.1, 0.1)
            font_size: "25sp"
            on_release: app.button_click("5")
            
        MDRaisedButton:
            text: "6"
            font_name: "Baygo" 
            md_bg_color: app.theme_cls.primary_color
            halign: "center"
            pos_hint: {'center_x': 0.66, 'center_y': 0.29}
            size_hint: (0.1, 0.1)
            font_size: "25sp"
            on_release: app.button_click("6")
            
        MDRaisedButton:
            text: "7"
            font_name: "Baygo" 
            md_bg_color: app.theme_cls.primary_color
            halign: "center"
            pos_hint: {'center_x': 0.34, 'center_y': 0.18}
            size_hint: (0.1, 0.1)
            font_size: "25sp"
            on_release: app.button_click("7")
        MDRaisedButton:
            text: "8"
            font_name: "Baygo" 
            md_bg_color: app.theme_cls.primary_color
            halign: "center"
            pos_hint: {'center_x': 0.5, 'center_y': 0.18}
            size_hint: (0.1, 0.1)
            font_size: "25sp"
            on_release: app.button_click("8")
            
        MDRaisedButton:
            text: "9"
            font_name: "Baygo" 
            md_bg_color: app.theme_cls.primary_color
            halign: "center"
            pos_hint: {'center_x': 0.66, 'center_y': 0.18}
            size_hint: (0.1, 0.1)
            font_size: "25sp"
            on_release: app.button_click("9")
            
        MDRaisedButton:
            text: "0"
            font_name: "Baygo" 
            md_bg_color: app.theme_cls.primary_color
            halign: "center"
            pos_hint: {'center_x': 0.5, 'center_y': 0.07}
            size_hint: (0.1, 0.1)
            font_size: "25sp"
            on_release: app.button_click("0")
            
        MDRectangleFlatIconButton:
            text: ""
            icon: "backspace"
            md_bg_color: app.theme_cls.primary_color
            pos_hint: {'center_x': 0.66, 'center_y': 0.07}
            size_hint: (0.1, 0.1)
            icon_color: "black"
            line_color: app.theme_cls.primary_color
            halign: 'left'
            on_release: app.backspace_click()
                
        
        
        

'''

class mainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.primary_hue = "700"
        return Builder.load_string(KV)
    
    def button_click(self, button_text):
        password_field = self.root.ids.password_field
        current_text = password_field.text
        new_text = current_text + button_text
        password_field.text = new_text
        
    def backspace_click(self):
        password_field = self.root.ids.password_field
        current_text = password_field.text
        new_text = current_text[:-1]  # Remover o último caractere
        password_field.text = new_text
mainApp().run()




