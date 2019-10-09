from isbn import isbn

def test_empty_string_of_numbers():
    number = ''
    assert isbn(number) == False

def test_short_number():
    number = '35982150'
    assert isbn(number) == False

def test_isbn_without_hyphens():
    number = '3598215088'
    assert isbn(number) == True 

def test_isbn_ends_with_x():
    number = '359821507X'
    assert isbn(number) == True


#check for dashses or not dashes
#check ends with number