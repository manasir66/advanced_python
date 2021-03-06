import inspect   #can be used to inspect elements 

#Testing generating classes using functions 

def class_generator(some_val):

  class Some_Class:

    def __init__(self, name):           #initialize the class
        self.name = name

    def set_val_for_class(self, val):
      self.val = val

    def get_val_from_class(self):
      return self.val

  return Some_Class                    #Return the class created inside the function 


cls = class_generator("Pass Some Val")
object_of_cls = cls("Some name")

print(object_of_cls.name)
print(id(class_generator))