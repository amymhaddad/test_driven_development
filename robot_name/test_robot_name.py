
from robot_name import Robot 

def test_robot_has_name():
    robot = Robot()
    assert robot.create_random_name() == 'AB123'

