from robot_name import Robot


def test_robots_have_different_names():
    robot1 = Robot()
    robot2 = Robot()
    assert robot1.name != robot2.name


def test_reset_name_to_different_name():
    robot = Robot()
    assert robot.reset() != robot.name


def test_length_robot_name():
    robot = Robot()
    assert len(robot.name) == 5
