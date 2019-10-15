
from robot_name import Robot 

def test_robot_has_name():
    robot = Robot()
    assert robot.name != robot.create_random_name()

def test_reset_name_to_different_name():
    robot = Robot()
    assert robot.reset() != robot.name
