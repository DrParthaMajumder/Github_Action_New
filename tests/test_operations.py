from src.math_operations import addition, substraction

def test_add():
    assert addition(2,3)==5
    assert addition(-1,1)==0
    
def test_sub():
    assert substraction(5,3)==2
    assert substraction(4,3)==1
    assert substraction(3,3)==0
    assert substraction(2,3)==-1