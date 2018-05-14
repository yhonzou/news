# coding: utf-8


from scene import *
import sound
import random
import math,base64
A = Action

class Splash (Scene):
    def setup(self):
        
        self.background_color = '#efefef'
        med_font =('Futura', 30)
        en = base64.b64decode('576k5paH5Lu25a+G56CBOgoKaG9uem914oCidG9w'.encode('utf-8'))
        mi=str(en,'utf-8')
        self.title_buton =LabelNode(mi, med_font, color ='black')
        self.title_buton.position = (self.size.w/2,-100)
        self.title_buton.z_position = -1
        self.title_buton.alpha = 1
        self.add_child(self.title_buton)
        
    
    def did_change_size(self):
        pass
    
    def update(self):
        self.title_buton.run_action(A.sequence(A.wait(.5),A.move_to(self.size.w/2,self.size.h/2-20,.1)))
        

        self.title_buton.run_action(A.sequence(A.wait(2),A.fade_to(0,0.5,TIMING_LINEAR),A.wait(0.5),A.fade_to(1,0.5,TIMING_LINEAR)))
    

if __name__ == '__main__':
    run(Splash(), PORTRAIT, show_fps=True)