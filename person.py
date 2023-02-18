#First We Will make a class for person

from abc import ABC, abstractmethod


#using abstraction

class Person(ABC):

    def __init__(self, name, f_name, gender):
        self.__name = name                      #encupslating the attributes
        self.__f_name = f_name
        self.__gender = gender
     
    @abstractmethod    
    def get_name(self):
        return self.__name
    
    
    @abstractmethod
    def get_f_name(self):
        return self.__f_name
    
    
    @abstractmethod
    def get_gender(self):
        return self.__gender



class Admin:
    def __init__(self):
        self.__password = "admin123"

    def return_pass(self):
        return self.__password






