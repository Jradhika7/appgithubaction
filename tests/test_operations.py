from src.math_operation import add, sub

def test_add():
    assert add(2,1)==3
    assert add(-1,1)==0
    assert add(2,3)==5

def test_sub():
    assert sub(2,1)==1
    assert sub(4,3)==1
    assert sub(4,2)==2
    assert sub(10,10)==0
    assert sub(1,2)==-1
    
