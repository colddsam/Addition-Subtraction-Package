import pytest 
from addition_subtraction.add_sub import AddSub
class TestVariousCases:
    
    first_number=10
    second_number=30
    
    def test_one(self):
        myObj=AddSub()
        assert myObj.operation()==0
        
    def test_second(self):
        myObj=AddSub(method_val=0)
        assert myObj.operation()==0
        
    def test_third(self):
        myObj=AddSub(method_val=2)
        assert myObj.operation()==0
    
    def test_four(self):
        myObj=AddSub(method_val=1)
        assert myObj.operation()==0
    
    def test_five(self):
        myObj=AddSub()
        assert myObj.operation(first_number=self.first_number,second_number=self.second_number)==self.first_number+self.second_number
    
    def test_six(self):
        myObj=AddSub(method_val=0)
        assert myObj.operation(first_number=self.first_number,second_number=self.second_number)==self.first_number-self.second_number
    
    def test_seven(self):
        myObj=AddSub(method_val=1)
        assert myObj.operation(first_number=self.first_number,second_number=self.second_number)==self.first_number+self.second_number
    
    def test_eight(self):
        myObj=AddSub(method_val=2)
        assert myObj.operation(first_number=self.first_number,second_number=self.second_number)==self.first_number+self.second_number
        
    