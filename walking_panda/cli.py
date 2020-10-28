from .panda import WalkingPanda

import argparse


def cli():
    parser = argparse.ArgumentParser(prog = "walking_panda")
    parser.add_argument("--no-rotate", help="Suppress Rotation", action="store_true")
    parser.add_argument("--scale=1", help="Increase Scale", action="store_const", dest="set_scale", const=0.01, default=0.005)
    parser.add_argument("--cam-speed", help="Set Speed of Camera Rotation", action="store", default=6)
    parser.add_argument("--cam-spin-direction", help="Change Camera Spin Direction to Spin Left", action="store_const", const=-1,default=1)
    parser.add_argument("--flip-camera", help="Flip the Camera Upside Down", action="store_const", const=180, default=0)
    args = parser.parse_args()

    walking = WalkingPanda(**vars(args))
    walking.run()
