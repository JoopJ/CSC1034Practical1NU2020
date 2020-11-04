from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor

class WalkingPanda(ShowBase):

    def __init__(self, no_rotate=False,set_scale=0.005,cam_speed=6,cam_spin_direction=1, flip_camera=0):
        ShowBase.__init__(self)
        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transform on the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        # Check wether to rotate the camera or to keep it still
        if (no_rotate or flip_camera != 0):
            # Add the setCameraPosition procedure to the task manager.
            self.taskMgr.add(self.setCameraPositionTask, "SetCameraPositionTask", extraArgs=[flip_camera], appendTask=True)
        else:
            # Add the spinCameraTask procedure to the task manager.
            self.taskMgr.add(self.spinCameraTask, "SpinCameraTask", extraArgs=[cam_speed,cam_spin_direction], appendTask=True)

        # Load and transform the panda actor.
        self.pandaActor = Actor("models/panda-model",{"walk": "models/panda-walk4"})
        self.pandaActor.setScale(set_scale, set_scale, set_scale)
        self.pandaActor.reparentTo(self.render)
        # Loop its animation.
        self.pandaActor.loop("walk")

        # Load and play sfx
        footstepsSound = self.loader.loadSfx("sounds/footsteps.mp3")
        roarSound = self.loader.loadSfx("sounds/roar.mp3")
        footstepsSound.setLoop(True)
        footstepsSound.play()
        roarSound.play()

    # Define a procedure to move the camera.
    def spinCameraTask(self, cam_speed, cam_spin_direction, task):
        angleDegrees = task.time * cam_speed * cam_spin_direction
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont

    # Define a procedure to position the camera infront of the panda
    def setCameraPositionTask(self, flip_camera, task):
        self.camera.setPos(0,-20,3)
        self.camera.setHpr(0,0,flip_camera)
        return Task.cont
