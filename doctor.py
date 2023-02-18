from person import Person


class Doctor(Person):

    dr_id = 0

    def __init__(self, name, f_name, gender, specility):
        super().__init__(name, f_name, gender)
        self.__specility = specility
        self.__p_id = Doctor.__create_id()

    def __create_id():
        p_id = "Dr-"+ str(Doctor.dr_id)
        Doctor.dr_id += 1
        return p_id
    
    def get_name(self):
        return super().get_name()
    
    def get_f_name(self):
        return super().get_f_name()
    
    def get_gender(self):
        return super().get_gender()
    
    def get_specility(self):
        return self.__specility
    
    def get_id(self):
        return self.__p_id
    