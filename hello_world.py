from direct.showbase.ShowBase import ShowBase
import sys
import platform

print("Hello")

print( 1, sys.version)
print( 2, platform.python_implementation())
print( 3, sys.executable)


class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transform on the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

app = MyApp()
app.run()