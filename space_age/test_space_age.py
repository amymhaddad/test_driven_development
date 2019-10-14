from space_age import SpaceAge


def test_earth_years():
    
    seconds = 1000000000
    age = SpaceAge(seconds)

    assert age.earth_age() == 31.69


def test_age_on_mercury():

    seconds = 2134835688
    age = SpaceAge(seconds)
    assert age.on_mercury() == 280.88


def test_age_on_venus():

    seconds = 189839836
    age = SpaceAge(seconds)
    assert age.on_venus() == 9.78


def test_age_on_mars():

    seconds = 2329871239
    age = SpaceAge(seconds)
    assert age.on_mars() == 39.25


def test_age_on_jupiter():

    seconds = 901876382
    age = SpaceAge(seconds)
    assert age.on_jupiter() == 2.41


def test_age_on_saturn():

    seconds = 3000000000
    age = SpaceAge(seconds)

    assert age.on_saturn() == 3.23


def test_age_on_uranus():

    seconds = 3210123456
    age = SpaceAge(seconds)

    assert age.on_uranus() == 1.21


def test_age_on_neptune():

    seconds = 8210123456
    age = SpaceAge(seconds)
    assert age.on_neptune() == 1.58
