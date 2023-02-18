from person import Admin
from hospital import Hospital
import json
import getpass

def main():

    
    hos_data_reader = open('hospital_data.json', 'r')  #this will open doctors_data json file for reading
    hos_data = json.load(hos_data_reader)         #this will load doctors_data file
    hospital = Hospital(100, hos_data)   #creating hospital object

    while True:
        
        #printing main menu
        
        print('''\n                           
        1) If you are Admin\n
        2) If you are Staff\n
        3) If you are Patient\n
        4) Exit\n''')
        
        responce = input("Enter your choice: ")
        if responce == "1":
            password = getpass.getpass("Enter your password: ")
            admin = Admin()                              #creating hospital admin object
            if password == admin.return_pass():          #calling return_pass method 
                print("LogedIn succesfully \n")
                while True:
                            #printing menu for admin 
                            
                    print('''\n
                    1. Add Staff\n
                    2. Remove Staff\n
                    3. Display Staff Details\n
                    4. Display Patients\n
                    5. Exit\n''')
                                          
                    resp = input("Enter your Choice: ")
                    
                    if resp == "1":
                        print(hospital.add_staff())
            
                    elif resp == "2":
                        hospital.remove_staff()
                    
                    elif resp == "3":    
                        hospital.display_doc()
                        hospital.display_nurse()
                    
                    elif resp == "4":
                        hospital.display_patients()
                    
                    elif resp == "5":
                        break                #Exiting as admin
                    
                    else:
                        print("Wrong Input")



            else:
                print("wrong Password\n")     #this will be printed if an admin enter wrong password

        elif responce == "2":           #if person enter as staff

            if len(hos_data[5]) == 0:
                print("No Staff Found")
            
            else:
                staff_id = input("Enter your Id: ")
                try:
                    if hos_data[5][staff_id] == "":
                        print("You are logging in for the first time")
                        create_pass = input("create password: ")
                        hos_data[5][staff_id] = create_pass
                        print("Password created\n Now you can login with your ID and password ")
                    
                    else:
                        staff_pass = getpass.getpass("Enter your Password: ")
                        if hos_data[5][staff_id] == staff_pass:
                            print("LogedIn succesfully")    

                            while True:
                                
                            #printing menu for staff
                
                                print('''\n
                                1. Admit Patient\n
                                2. Add Patient Investigaton\n
                                3. Discharge Patient\n
                                4. Display Patients\n
                                5. Exit\n''')
                
                                choice = input("Enter your choice: ")
                
                                if choice == "1":
                                    print(hospital.admit_patient())

                                elif choice == "2":
                                    print(hospital.add_investigation())
                    
                                elif choice == "3":
                                    print(hospital.discharge_patient())
                    
                                elif choice == "4":
                                    hospital.display_patients()   #displaying all patients addmitted in hospital
                    
                                elif choice == "5":
                                    break              #exiting as staff
                        
                        else:
                            print("wrong Password")        
        
                except:
                    print("User Name or Staff with given ID does Not Exist")
        
        elif responce == "3":
            while True:
                
                #menu for patient
                print("\n1. Check my details \n")
                print("2. Exit\n")
                choice2 = input("Enter your choice: ")
                
                if choice2 == "1":
                    hospital.my_details()     

                elif choice2 == "2" :
                    break                               # exiting as patinet
                
                else:
                    print("wrong Input")

        elif responce == "4":
            
            hos_data_writer = open('hospital_data.json', 'w')
            total = [hospital.patients, hospital.investigation, hospital.doctor,
                    hospital.nurse, hospital.used_ids, hospital.credintals]
            json.dump(total, hos_data_writer)          #Dumping or saving all the data in json file
            hos_data_writer.close()
            break

        else:
            print("wrong input")

if __name__ == "__main__":
    main()
