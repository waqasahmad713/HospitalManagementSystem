from person import Person


#here we will create a class Patient which will inherit from class Person

class Patient(Person):       #patient class inherting from Person class

    pat_id = 0                #static attributes

    def __init__(self, name, age,f_name, gender, dieases, assigned_doc):
        super().__init__(name, f_name, gender)
        self.__age = age
        self.__dieases = dieases
        self.__assigned_doc = assigned_doc
        self.__p_id = Patient.__create_id()


    def __create_id():
        p_id = Patient.pat_id
        Patient.pat_id += 1
        return f"Patient-{p_id}"
    
    def get_name(self):
        return super().get_name()
    
    def get_f_name(self):
        return super().get_f_name()
    
    def get_gender(self):
        return super().get_gender()
    
    def get_age(self):
        return self.__age
    
    def get_dieases(self):
        return self.__dieases
    
    def get_assigned_doc(self):
        return self.__assigned_doc
    
    def get_id(self):
        return self.__p_id
    
    




class Investigation:
    def __init__(self,investigation_type, date, result):
        self.__investigation_type = investigation_type
        self.__date = date
        self.__result = result

    def get_invest_type(self):
        return self.__investigation_type
    
    def get_date(self):
        return self.__date
    
    def get_result(self):
        return self.__result