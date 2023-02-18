#creating hospital class
from patient import Patient, Investigation
from doctor import Doctor
from nurse import Nurse

class Hospital:
    def __init__(self, capacity, h_data):


        self.capacity = capacity
        self.patients = h_data[0]
        self.investigation = h_data[1]
        self.doctor = h_data[2]
        self.nurse = h_data[3]
        self.used_ids = h_data[4]
        self.credintals = h_data[5]


    def admit_patient(self):
        
        '''this method will append pateints  in patient attribute'''
        
        name = input("Enter name: ")
        f_name =   input("Enter F_name: ")
        age = input("Enter Age: ")
        gender = input("Enter gender: ")
        dieases = input("Enter disease: ")
        assign_doc = input("Enter Doctor ID to assign: ")
        if assign_doc in self.doctor.keys():
            
            try:
            

                if len(self.patients) < self.capacity:
                    Patient.pat_id = self.used_ids["Patient_IDs"]
                    pat = Patient(name, age, f_name, gender, dieases, assign_doc)
                    self.patients[pat.get_id()] = pat.get_name(), pat.get_f_name(),pat.get_age() ,pat.get_gender(),  pat.get_dieases(), pat.get_assigned_doc()
                    self.used_ids["Patient_IDs"] = Patient.pat_id
                    return "Patient admitted successfully"
                else:
                    return "Hospital is full"
                    
            except:

                if len(self.patients) < self.capacity:
                    self.used_ids["Patient_IDs"] = Patient.pat_id
                    Patient.pat_id = self.used_ids["Patient_IDs"]
                    pat = Patient(name, age, f_name, gender, dieases, assign_doc)
                    self.patients[pat.get_id()] = pat.get_name(), pat.get_f_name(),pat.get_age() ,pat.get_gender(),  pat.get_dieases(), pat.get_assigned_doc()
                    self.used_ids["Patient_IDs"] = Patient.pat_id
                    return "Patient admitted successfully"
                else:
                    return "Hospital is full"
        
        else:
            return f"No doctor with ID  {assign_doc}"


    def discharge_patient(self):
        
        '''this method will remove a 
        pateint from patient dictonary of given ID and also his investigation'''
        
        patient_id = input("Enter patient ID to discharge: ")
        
        if patient_id not in self.patients:
            return "Patient Not Found"

        self.patients.pop(patient_id)
        try:  
            self.investigation.pop(patient_id)
        except:
            pass 
        return f"Patient  with ID {patient_id} discharged succesfully"

    def add_investigation(self):
        
        '''This method will add investigation to investagiation
        to the dictonry with Patient ID as key'''
        
        
        
        id = input("Enter Patient Id: ")
        
        # for patient_id in self.patients.keys():
        if id in self.patients.keys():
            type = input("Enter investigtion Type: ")
            date = input("Enter Investigation Date: ")
            result = input("Enter investigation Result: ")
            invest =  Investigation(type, date, result) 
            self.investigation[id] = invest.get_invest_type(), invest.get_date(), invest.get_result()
            return "investigation added successfully"

        else:
            return f"patient with ID {id} does not Exist "

    def add_staff(self):
        
        '''This Method will add 
        doctor or nurse to it's respective dictionary'''
        
        name = input("Enter name: ")
        f_name =   input("Enter F_name: ")
        gender = input("Enter gender: ")
        role = input("Enter role of the staff (Doctor(1) or Nurse(2)): ")
                        
        if role == "1":
            speciltiy = input("Enter Doctor Specility: ")
                            
                                #this will check how many doctors are already aadded and then will set 
                                # the static attribute dr_id value to already present doctors
            try:                    #so the new id will not start again from 0
                Doctor.dr_id = self.used_ids["Dr_IDs"]
                doc = Doctor(name, f_name , gender, speciltiy)
                self.doctor[doc.get_id()] = doc.get_name(), doc.get_f_name(), doc.get_gender(), doc.get_specility()
                self.used_ids["Dr_IDs"] = Doctor.dr_id
                self.credintals[doc.get_id()] = ""
                return "Doctor added successfully"
            
            except:
                self.used_ids["Dr_IDs"] =  Doctor.dr_id                  
                Doctor.dr_id = self.used_ids["Dr_IDs"]
                doc = Doctor(name, f_name , gender, speciltiy)
                self.doctor[doc.get_id()] = doc.get_name(), doc.get_f_name(), doc.get_gender(), doc.get_specility()
                self.used_ids["Dr_IDs"] = Doctor.dr_id
                self.credintals[doc.get_id()] = ""
                return "Doctor added successfully"
                        
        elif role == "2":
            duty = input("Enter Nurse duty on ward: ")
            
            try:
                Nurse.nr_id = self.used_ids["Nurse_IDs"]
                nurse = Nurse(name, f_name, gender, duty)
                self.nurse[nurse.get_id()] = nurse.get_name(), nurse.get_f_name(), nurse.get_gender(), nurse.get_duty()
                self.used_ids["Nurse_IDs"] = Nurse.nr_id
                self.credintals[nurse.get_id()] = ""
                return "Nurse added succesfully"
            except:
                self.used_ids["Nurse_IDs"] = Nurse.nr_id
                Nurse.nr_id = self.used_ids["Nurse_IDs"]
                nurse = Nurse(name, f_name, gender, duty)
                self.nurse[nurse.get_id()] = nurse.get_name(), nurse.get_f_name(), nurse.get_gender(), nurse.get_duty()
                self.used_ids["Nurse_IDs"] = Nurse.nr_id
                self.credintals[nurse.get_id()] = ""
                return "Nurse added succesfully"
                        
        else:
            return "Wrong Input"
            
            
    def remove_staff(self):
        
        role = input("Which staff do you want to remove Doctor or Nurse(1/2): ")
        
        if role=='1':
            doc_id = input("Enter doctor Id to remove: ")
            if doc_id in self.doctor:
                self.doctor.pop(doc_id)
                self.credintals.pop(doc_id)
                print(f"Doctor with id {doc_id} removed successfully")
            else:
                print(f"Doctor with ID {doc_id} does not exist")
        if role=='2':
            nurse_id = input("Enter Nurse ID to remove: ")
            if nurse_id in self.nurse:
                self.nurse.pop(nurse_id)
                self.credintals.pop(nurse_id)
                print(f"Nurse with Id {nurse_id} removed succefully")
            else:
                print(f"Nurse with ID {nurse_id} does not exist")
            
            
            
    def display_patients(self):
        
        '''this method dispaly all patients
            addmitted in hospital'''
        
        
        print("***************************************************")
        print("\n           Patients Admitted ")
        for patient_id, patient_det in self.patients.items():
            print(f'''\n
            Patient Id      : {patient_id}\n
            Name            : {patient_det[0]}\n
            Father Name     : {patient_det[1]}\n
            Age             : {patient_det[2]}\n
            Gender          : {patient_det[3]}\n
            Disease         : {patient_det[4]}\n
            Doctor Assigned : {patient_det[5]}\n''')
            print("       ----------------------------")
            
            

    def my_details(self):
        
        '''this mehtod will return details
        of the patient of given id'''
        
        id = input("Enter your id: ")
        try:
            patient = self.patients[id]
            print( f'''\n
        PAteint ID          :  {id}\n
        Patient Name        :  {patient[0]}\n
        Father Name         :  {patient[1]}\n 
        Pateint Age         :  {patient[2]}\n
        Patient Gender      :  {patient[3]}\n
        Patient Disease     :  {patient[4]}\n
        Doctor Assigned     :  {patient[5]}''')
            
        except:
            print("\nPateint not found")
        
        
        if id in self.investigation.keys():
                invest_details = self.investigation[id]    
                print(f'''\n
        Investigation type   :  {invest_details[0]}\n
        Investigation Date   :  {invest_details[1]}\n
        Investigation result :  {invest_details[2]}\n
                        ''')

            
    
    def display_doc(self):
        
        '''This method will dispaly docotrs 
            avilable in hospital'''
        
        print("*****************************************************")
        print("\n           Doctors ")
        for doc_id, doc_det in self.doctor.items():
            print (f'''\n
            Doctor Id :  {doc_id}\n
            Name      :  {doc_det[0]}\n
            f_name    :  {doc_det[1]}\n
            Gender    :  {doc_det[2]}\n
            specility :  {doc_det[3]}\n''')
            print("      ---------------------------------")

    def display_nurse(self):
        
        '''This method will display 
        Nurses avilable in hospital'''
        
        print("**************************************************")
        print("\n           Nurses")
        for nurse_id, nurse_det in self.nurse.items():
            print(f'''\n
            Nurse ID     :  {nurse_id}\n
            Name         :  {nurse_det[0]}\n
            Father Name  :  {nurse_det[1]}\n
            Gender       :  {nurse_det[2]}\n
            Duty on Ward :  {nurse_det[3]}\n''')
            print("   -------------------------------------------")

