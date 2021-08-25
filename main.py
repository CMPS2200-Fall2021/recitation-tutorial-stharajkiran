# first change
def sum_of_squares(a):
    sum = 0
    for num in a:
        square = num ** 2
        sum += square
    return sum

def test_one():
    assert sum_of_squares([1,2,3]) == 14

test_one()
  
