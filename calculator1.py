from kivy.app import App
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.properties import ObjectProperty

class Manager(ScreenManager):
    pass

class Calc(Screen):
    txt=ObjectProperty(None)

    def process(self,ope):
            self.num1=float(self.txt.text)
            self.ope=ope
            self.txt.text= ''

    def res(self):
        self.num2= float(self.txt.text)

        if self.ope == '+':
           self.r=self.num1+self.num2
        elif self.ope == '-':
            self.r=self.num1-self.num2
        elif self.ope == '*':
            self.r=self.num1*self.num2
        else:
            self.r=self.num1/self.num2

        self.txt.text= str(self.r)





class MainApp(App):
    def build(self):
        Window.size=360,640
        return Builder.load_file('main.kv')

if __name__ == "__main__":
    app=MainApp()
    app.run()