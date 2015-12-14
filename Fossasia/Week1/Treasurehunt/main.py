import kivy
from board import Board
from kivy.app import App
from kivy.uix.button import Button 
from kivy.uix.modalview import ModalView
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.properties import ListProperty, NumericProperty, AliasProperty, ObjectProperty
from kivy.event import EventDispatcher
from kivy.uix.popup import Popup
kivy.require('1.8.0')
#Determine size of your board
tiles = 6
def restart(size):
    Size = []
    for x in range(size):
        Size.append([0] * size)
    return Size
global tiles
Finish = Board(restart(tiles))

class GridMixin(EventDispatcher):
    value = NumericProperty(0, min=0, max=9)

class SelectSizePopup(Popup):
    button = ObjectProperty()
    def open(self, *args, **kwargs):
        return super(SelectSizePopup, self).open(*args, **kwargs)
    def select(self, value): 
        self.dismiss()
        global tiles
        tiles = value

class ColButton(Button, GridMixin):
    def __init__(self, **kwargs):
        super(ColButton, self).__init__(**kwargs)
        self.bind(on_release=self.show_popup)
        self.popup = SelectSizePopup(button=self)
    
    def show_popup(self, *args):
        self.popup.open()
    
    def set_value(self, value):
        self.value = value
        return True

class GridEntry(Button):
   coords = ListProperty([0, 0])
   pressed = NumericProperty(1)
#Fancy grid
class TreasureHuntGrid(GridLayout):
    global tiles
    value = NumericProperty(tiles)
    Finish.shuffle()
    status = ListProperty(Finish.board)
    attempts = NumericProperty(8)
    treasures = NumericProperty(9)
    treasuresfound = NumericProperty(0)
    def __init__(self, *args, **kwargs):
      super(TreasureHuntGrid, self).__init__(*args, **kwargs)
      global tiles
      for row in range(tiles):
         for column in range(tiles):
            grid_entry = GridEntry(
               coords=(row, column))
            grid_entry.bind(on_release=self.button_pressed)
            self.add_widget(grid_entry)
    def reset(self, *args):
        global tiles
        self.value = tiles
        self.clear_widgets()
        Finish.board = restart(self.value)
        Finish.shuffle()
        self.status = Finish.board 
        for row in range(tiles):
           for column in range(tiles):
              grid_entry = GridEntry(
              coords=(row, column))
              grid_entry.bind(on_release=self.button_pressed)
              self.add_widget(grid_entry)
        self.attempts = 8
        self.treasuresfound = 0
        for child in self.children: #All child widget
            child.text = ''
            child.background_color = (1, 1, 1, 1)
            child.pressed = 1

    def button_pressed(self, button):
        colours = {-1: (1, 0, 0, 1), 1: (0, 1, 0, 1)} # (r, g, b, a)
        row, column = button.coords 
        if button.pressed == 1:
            button.text = {-1: Finish.surrounded(row, column), 1: 'X'}[self.status[row][column]]
            button.background_color = colours[self.status[row][column]]
            print ('{} button clicked!'.format(button.coords))
            button.pressed = 0
            if Finish.board[row][column] == 1:
                self.treasuresfound = self.treasuresfound + 1
                if self.treasuresfound == 9:
                    popup = ModalView(size_hint=(0.75, 0.5))
                    endlabel = Button(text="You won !", font_size=50)
                    endlabel.background_color = (0, 1, 0, 1)
                    popup.add_widget(endlabel)
                    popup.bind(on_dismiss=self.reset)
                    popup.open()
            else:
               self.attempts = self.attempts - 1
               if self.attempts == 0:
                  popup = ModalView(size_hint=(0.75, 0.5))
                  endlabel = Button(text="Try again", font_size=50)
                  popup.add_widget(endlabel)
                  popup.bind(on_dismiss=self.reset)
                  popup.open()

class Interface(BoxLayout):
    pass

class TreasureHuntApp(App):
    def build(self):
       return Interface()

if __name__ == "__main__":
    TreasureHuntApp().run()


