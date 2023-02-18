from person import Person


#Here we created a class Nurse which will inherit from person class

class Nurse(Person):

    nr_id = 0

    def __init__(self, name, f_name, gender, duty):
        super().__init__(name, f_name, gender)
        self.__duty = duty
        self.__n_id = Nurse.__create_id()

    def __create_id():
        n_id = "Nurse-" + str(Nurse.nr_id)
        Nurse.nr_id += 1
        return n_id
    def get_name(self):
        return super().get_name()
    
    def get_f_name(self):
        return super().get_f_name()
    
    def get_gender(self):
        return super().get_gender()
    
    def get_duty(self):
        return self.__duty
    
    def get_id(self):
        return self.__n_id