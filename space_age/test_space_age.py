from space_age import SpaceAge



def test_earth_years():
    #creating a new SA object with 10000000 seconds
    #this will always pass it to init
    seconds = 1000000000
    age = SpaceAge(seconds)

    assert age.earth_age() == 31.69
