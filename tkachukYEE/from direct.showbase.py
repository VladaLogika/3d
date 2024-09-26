from direct.showbase.ShowBase import ShowBase
class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.model = self.loader.loadModel('models/environment')
        self.model.reparentTo(self.render)
        self.model.setScale(0.1)
        self.model.setPos(-2, 25, -3)
        base.camLens.setFov(90)

game = ShowBase()
game.run()