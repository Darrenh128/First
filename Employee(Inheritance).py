# inheritance from person class

from Person import person
class employee(person):

  def __init__(self,name,age,gender,location,is_employed,company):

    super().__init__(name,age,gender,location,is_employed)    #inheriting from the 'person' class

    self.company = company  # adding 'company' to the 'person' class

me=employee('Darren',30,'Male','Slough',False,'N/A')    # adding 'company' to the 'person' class
me1=employee('Michael',32,'Male','Slough',True,'ONS')

print(me.company)
print(me.name)
print(me.is_employed)
print(me1.company)