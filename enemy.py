from engine.draw import Draw
from engine.game_object import GameObject


class EnemyOne(GameObject):

    def on_start(self):
        pass

    def on_update(self, delta_time):
        pass

    def on_draw(self):
        # enemy 1
        Draw.change_color("#FF0000")
        Draw.rect(50, 20, 45, 45)
        Draw.rect(75, -25, 80, 40)
        # legs
        Draw.rect(90, -65, 15, 15, fill=True)
        Draw.rect(125, -65, 15, 15, fill=True)
        # tail
        Draw.circle(7, 150, -30, fill=True)
        # eyes
        Draw.rect(57, 10, 10, 10, fill=True)
        Draw.rect(75, 10, 10, 10, fill=True)
        # mouth
        Draw.rect(62, -10, 20, 5, fill=True)
        # hair
        Draw.line(50, 20, 65, 30)
        Draw.line(60, 20, 75, 30)
        Draw.line(70, 20, 85, 30)
        Draw.line(80, 20, 95, 30)
        Draw.line(90, 20, 105, 30)


class EnemyTwo(GameObject):

    def on_start(self):
        pass

    def on_update(self, delta_time):
        pass

    def on_draw(self):
        # enemy 2
        Draw.change_color("#FF00FF")
        Draw.rect(212, 20, 45, 45)
        Draw.rect(220, -25, 30, 40)
        # leg
        Draw.rect(210, -65, 50, 15, fill=True)
        # eyes
        Draw.rect(220, 10, 10, 10, fill=True)
        Draw.rect(238, 10, 10, 10, fill=True)
        # mouth
        Draw.rect(225, -10, 20, 5, fill=True)
        # hair
        Draw.line(212, 20, 220, 50)
        Draw.line(257, 20, 250, 50)
        Draw.circle(5, 215, 50)
        Draw.circle(5, 245, 50)
        Draw.line(225, 20, 230, 40)
        Draw.line(245, 20, 240, 40)
        Draw.circle(3, 227, 40)
        Draw.circle(3, 237, 40)


class EnemyThree(GameObject):

    def on_start(self):
        pass

    def on_update(self, delta_time):
        pass

    def on_draw(self):
        # enemy 3
        Draw.change_color("#00FFFF")
        Draw.rect(312, 20, 45, 45)
        Draw.rect(320, -25, 30, 40)
        # leg
        Draw.rect(310, -65, 50, 15, fill=True)
        # eyes
        Draw.rect(320, 10, 10, 10, fill=True)
        Draw.rect(338, 10, 10, 10, fill=True)
        # mouth
        Draw.rect(325, -10, 20, 5, fill=True)
        # hair
        Draw.line(312, 20, 318, 50)
        Draw.line(323, 20, 318, 50)
        Draw.line(323, 20, 330, 50)
        Draw.line(335, 20, 330, 50)
        Draw.line(335, 20, 342, 50)
        Draw.line(347, 20, 342, 50)
        Draw.line(347, 20, 353, 50)
        Draw.line(357, 20, 353, 50)
