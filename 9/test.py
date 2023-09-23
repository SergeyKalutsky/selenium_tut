class Title:
    def __init__(self, text, x, y, visible):
        self.text = text
        self.x = x
        self.y = y
        self.visible = visible
    
    def print_info(self):
        print('x', self.x)
        print('y', self.y)
        print('visible', self.visible)
    
    def hide(self):
        print(self.text, 'Скрыто')
    
    def show(self):
        print(self.text, 'Отображается')
            
t1 = Title('Узнать победителя прямо сейчс!', 150, 50, True)
t1.print_info()