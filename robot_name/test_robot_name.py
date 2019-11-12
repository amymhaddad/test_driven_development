from robot_name import Robot

import pytest, re


@pytest.fixture
def robot():
    return Robot()


def test_robots_have_different_names(robot):
    robot2 = Robot()
    assert robot.name != robot2.name


def test_reset_name_to_different_name(robot):
    original_name = robot.name
    assert original_name != robot.reset()


def test_robot_name_contains_correct_values(robot):
    result = re.match(r"\D{2}\d{3}", robot.name)
    assert result.group() == robot.name
