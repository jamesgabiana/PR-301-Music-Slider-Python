# all imports
import kivy
# enforce a minimum versioning
kivy.require('1.1.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import *
import gc
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.properties import NumericProperty, ObjectProperty
from kivy.lang import Builder
from kivy.config import Config
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '300')

from kivy.uix.scatter import Scatter
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

# From Kivy Crash Course 14 - Screen Manager
from kivy.properties import ListProperty

# From BradMC MusicSliderApp.py
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout

from kivy.core.audio import SoundLoader

# Got from https://groups.google.com/forum/#!msg/
# kivy-users/7rOZGMMIFXI/2kHbw7vlg9EJ
from kivy.core.window import Window

import random
from time import sleep

from kivy.uix.popup import Popup

# http://kivy.org/docs/_modules/kivy/adapters/listadapter.html
from kivy.adapters.adapter import Adapter





# WelcomeScreen:    (1) Code from Kivy Example screenmanager.py
# SliderBar:    	(2) Code from Kivy Pong Tutorial main.py
# MainScreen:		(1) Code from Kivy Example screenmanager.py


class WelcomeScreen(Screen):
    # give the background a random colour
    hue = NumericProperty(0)


class SliderBar(Screen):
    source = 'images/chords/minor.png'
    slideChords = ['Major', 'Minor','Dom7','Augmented','diminish']
    slideScales = ['AscendingMelodic','DescendingMelodic', 'Harmonic',
                   'Major', "Minor"]

##    def __init__(self):
##        addSpinner()
##
##    def addSpinner(self, Spinner):
##        spinner = Spinner()
##
##        self.sliderSpinLayout.add_widget(spinner(
##                                  text = ('Select a Scale'),
##                                  values = ('Major', 'Minor', 'Belivenant'),
##                                  size_hint = (None, None),
##                                  pos_hint= ({'center_x': 0, 'center_y': 0}),
##                                  size= (self.width / 4, self.height / 10.5)))
##
##    spinner.bind(text=selected_value)

    def changeSpinner(self):
        self.sliSpinLayout.clear_widgets()
        choSpin = Spinner(      text='Select a Chord',
                                values= self.slideChords,
                                pos_hint=  {'center_x':0.32,'top': 1},
                                size= (self.width / 4, self.height / 10.5),
                                size_hint= (None, None)
                                 )
        scaSpin = Spinner(      text='Select a Scale',
                                values= self.slideScales,
                                pos_hint=  {'center_x':0.32,'top': 1},
                                size= (self.width / 4, self.height / 10.5),
                                size_hint= (None, None)
                                 )

        scaSpin.bind(text=self.show_selected_value)
        choSpin.bind(text=self.show_selected_value)

        if (self.sliTog.state ==  'down'):
            self.sliSpinLayout.add_widget(scaSpin)
            self.chosenScale.disabled = True
        else:
            self.sliSpinLayout.add_widget(choSpin)
            self.chosenScale.disabled = True



    def show_selected_value(self, spinner, text):
        global chosen
        print('The spinner', spinner, 'have text', text)
        chosen = text
        self.chosenScale.disabled = False




    def updateScale(self):
        self.changeSpinner()

        if self.sliTog.state == 'down':
            self.my_image.source = "images/scales/" + chosen + ".png"
            self.my_image_wrap.source = "images/scales/" + chosen + ".png"  # <

        else:
            self.my_image.source = "images/chords/" + chosen + ".png"
            self.my_image_wrap.source = "images/chords/" + chosen + ".png"  # <


##        if self.btnScale.text == self.btnScale.text:
##            self.my_image.source = "images/minor.png"
##            #self.btnScale.text = "Major"
##        else:
##            self.my_image.source = "images/major.png"
##           # self.btnScale.text = "Minor"



##    def selected_value(spinner, text):
##        print('The spinner', spinner, 'have text', text)
##        updateScale(text)

    def update_image_wrap(self):                                            # <
        sctr = self.scatter                                                 # <
        img = self.my_image_wrap                                            # <
        if sctr.pos[0] + (sctr.size[0] / 2) < self.width / 2:               # <
            img.pos[0] = sctr.size[0] - img.size[0]                         # <
        else:                                                               # <
            img.pos[0] = 0                                                  # <

        if sctr.pos[0] > 0:                                                 # <
            sctr.pos = (sctr.pos[0] - (sctr.size[0] - img.size[0]) / 2,
                        sctr.pos[1])                                        # <
        elif sctr.pos[0] + sctr.size[0] < self.width:                       # <
            sctr.pos = (sctr.pos[0] + (sctr.size[0] - img.size[0]) / 2,
                        sctr.pos[1])                                        # <


class DropDownSlider(Screen):
    global freq
    hue = NumericProperty(0)
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

# Notes/frequency dictionary provided by www.phy.mtu.edu/~suits/notefreqs.html
    freq = {'C': 262, 'C#': 277, 'D': 294, 'D#': 311, 'E': 330, 'F': 349,
            'F#': 370, 'G': 392, 'G#': 415, 'A': 440, 'A#': 466, 'B': 494,
            'C5': 523, 'C#5': 554, 'D5': 587, 'D#5': 622, 'E5': 659,
            'F5': 698, 'F#5': 740, 'G5': 784, 'G#5': 831, 'A5': 880,
            'A#5': 932, 'B5': 988, 'C6': 1047, 'C#6': 1109, 'D6': 1175,
            'D#6': 1245, 'E6': 1319, 'F6': 1397, 'F#6': 1480, 'G6': 1568,
            'G#6': 1661, 'A6': 1760, 'A#6': 1865, 'B6': 1976}

# Chords information retrieved from http://www.scales-chords.com/chdbmain.php
    chords = {'Major': [0, 4, 7], 'Minor': [0, 3, 7], 'Dominant 7th':
              [0, 4, 7, 10], 'Augmented': [0, 4, 8], 'Diminish': [0, 3, 6],
              'Major 7th': [0, 4, 7, 11], 'Minor 7th': [0, 3, 7, 10],
              '5': [0, 7], 'Sus 4': [0, 5, 7], 'Minor 6': [0, 3, 7, 9],
              '9': [0, 4, 7, 10, 14], 'Minor 11': [0, 3, 7, 10, 17],
              'Minor 13': [0, 3, 7, 10, 21], 'Major 13': [0, 4, 7, 11, 21],
              '6 and 9': [0, 4, 7, 9, 14], '7b5': [0, 4, 6, 10],
              '7sus4': [0, 5, 7, 10], '9sus4': [0, 5, 7, 10, 14]}

# Scales info retrieved from http://www.scales-chords.com/scalefinder.php
    scales = {'Major': [0, 2, 4, 5, 7, 9, 11, 12],
              'Dorian': [0, 2, 3, 5, 7, 9, 10, 12],
              'Phrygian': [0, 1, 3, 5, 7, 8, 10, 12],
              'Mixolydian': [0, 2, 4, 5, 7, 9, 10, 12],
              'Lydian': [0, 2, 4, 6, 7, 9, 11, 12],
              'Locrian': [0, 1, 3, 5, 6, 8, 10, 12],
              'Harmonic Minor': [0, 2, 3, 5, 7, 8, 11, 12],
              'Melodic Minor': [0, 2, 3, 5, 7, 9, 11, 12],
              'Pentatonic Major': [0, 2, 4, 7, 9, 12],
              'Blues': [0, 3, 5, 6, 7, 10, 12],
              'Augmented': [0, 3, 4, 7, 8, 11, 12]}

    def checkActive(self):
        if self.checkbox_sca.active == True:
            self.dropdown_sca.disabled = False
            self.dropdown_cho.disabled = True
        else:
            self.dropdown_cho.disabled = False
            self.dropdown_sca.disabled = True


    def on_press(self):
        # clear_widgets method found through internet search
        self.resultLayout.clear_widgets()
        self.playAllLayout.clear_widgets()
        self.patternLayout.clear_widgets()
        if self.checkbox_cho.active:
            self.calc(self.dropdown_ton.text, self.dropdown_cho.text,
                      self.chords)
        elif self.checkbox_sca.active:
            self.calc(self.dropdown_ton.text, self.dropdown_sca.text,
                      self.scales)

    def calc(self, tonic, template, type):
        global allNotes
        allNotes = []
        calcnotes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A',
                     'A#', 'B', 'C5', 'C#5', 'D5', 'D#5', 'E5', 'F5', 'F#5',
                     'G5', 'G#5', 'A5', 'A#5', 'B5', 'C6', 'C#6', 'D6', 'D#6',
                     'E6', 'F6', 'F#6', 'G6', 'G#6', 'A6', 'A#6', 'B6']
        tonicnotes = calcnotes[calcnotes.index(tonic):]
        self.resultLayout.add_widget(Label(text='Notes in selection: ',
                                     size_hint=(None, None), size=(150, 50)))
        for x in type.get(template):
            self.resultLayout.add_widget(SoundButton(text=tonicnotes[x],
                                         size_hint=(None, None),
                                         size=(self.width / 20,
                                               self.width / 20)))
            allNotes.append(tonicnotes[x])

        self.playAllLayout.add_widget(PlayAllUp(text = 'Play All (Up)',
                                              size_hint = (None, None),
                                              size=(self.width / 4,
                                              self.width / 20),
                                              pos_hint= {'center_x' : 0.4,
                                                         'center_y':0.4}))

        self.playAllLayout.add_widget(PlayAllDown(text = 'Play All (Down)',
                                              size_hint = (None, None),
                                              size=(self.width / 4,
                                              self.width / 20),
                                              pos_hint= {'center_x' : 0.4,
                                                         'center_y':0.4}))

        self.patternLayout.add_widget(Label(text='Pattern Used: '
                                            + str(type.get(template)),
                                            size_hint=(None, None), width=300))




class PlayAllUp(Button):
    def on_press(self):
        p = PlayUpPopup()
        p.open()

class PlayAllDown(Button):
    def on_press(self):
        p = PlayDownPopup()
        p.open()


class PlayUpPopup(Popup):

    def playU(self):
        for n in allNotes:
            sound = SoundLoader.load('tones/' + n + '.wav')
            sound.play()
            sleep(0.9)
        self.dismiss()

class PlayDownPopup(Popup):

    def playD(self):
        for n in reversed(allNotes):
            sound = SoundLoader.load('tones/' + n + '.wav')
            sound.play()
            sleep(0.9)
        self.dismiss()


class SoundButton(Button):
    def on_press(self):
        sound = SoundLoader.load('tones/' + self.text + '.wav')
        sound.play()

# Taken from BradMC MusicSliderApp.py
# class and method names found on kivy.org/docs


class SliderTable(Screen):
    hue = NumericProperty(0)


class MyScreenManager(ScreenManager):
    pass



# The controling class - creates all others
class ScreenManagerApp(App):

    def on_pause(self):
        # Here you can save data if needed
        return True

    def build(self):
        pass


# initialization
if __name__ == '__main__':
    ScreenManagerApp().run()
