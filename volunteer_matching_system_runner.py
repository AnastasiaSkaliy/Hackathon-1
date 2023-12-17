from mission_matcher import MissionMatcher
from volunteer_repository import DataRepository
from volunteer_repository import Location
from volunteer_repository import Mission
from volunteer_repository import Branch


matcher = MissionMatcher()
data = DataRepository()

class SystemRunner:

    def get_age(self):
        user_age = int(input("Please enter your age: "))
        return user_age
  
    def get_district(self,locations: list[Location]) -> str:
        index = 1
        print("Select your preferred area of volunteering:")
        
        districts = {loc.district for loc in locations}
        for i in districts:
            print(f"{index}. {i}")
            index = index + 1
        dist_choice = int(input("Enter the number corresponding to your preferred district: "))
        dist_list = list(districts)
        dist_choice = dist_choice-1
        if dist_choice < 0 or dist_choice > len(dist_list):
                print("Invalid choice. Please select a valid area.")
                return None
        return dist_list[dist_choice]
    
    def match_profession(self) -> list[int]:
        professions = {
            "Doctor": [4, 10],  # Map professions to corresponding mission IDs
            "Vet":[24,27,29,30],
            "Psychologist":[16,22,18],
            "Driver":[1,7,15,26],
            "Teacher":[5,6,14],
            "Lawyer":[21,23],
            "Cook":[2],
            "Financier":[19,25],
            "Accountant":[19,25],
            "Translator":[12],
            "SMM Specialist":[8,17]
        }
        user_profession = input("Enter your profession: ").lower()
        lowercase_keys = {key.lower(): value for key, value in professions.items()}
        if user_profession in lowercase_keys:
            return lowercase_keys[user_profession]
        return []
    
    def match_car_needed(self):
        user_has_car = input("Do you have a car? (yes/no): ").lower()
        if user_has_car == "yes":
             return True
        return False
    
    def preferred_volunteering_area(self) -> tuple[str, list[int]]:
        print("Select your preferred area of volunteering:")
        print("1. Medical Support and Aid")
        print("2. Psychological assistance and trainings")
        print("3. Media and Communication")
        print("4. Children")
        print("5. Transport and Logistics")
        print("6. Office work")
        print("7. Jurisprudence")
        print("8. Finance")
        print("9. Animals")
        print("10. Housing for refugees")
        print("11. Food and clothing")

        areas = {
            "Medical Support and Aid": [4, 10],  # Mapping areas to corresponding mission IDs
            "Psychological assistance and trainings": [16, 22, 18],
            "Media and Communication": [8, 17],
            "Children": [5, 6, 14],
            "Transport and Logistics": [1, 7, 26, 15],
            "Office work": [9, 12],
            "Jurisprudence": [21, 23],
            "Finance": [19, 25],
            "Animals": [24, 27, 29, 30],
            "Housing for refugees": [11, 13, 20, 28],
            "Food and clothing": [2, 3]
        }

        while True:
            try:
                area_choice = int(input("Enter the number corresponding to your preferred area (1-11): "))
                if 1 <= area_choice <= 11:
                    selected_area = list(areas.keys())[area_choice - 1]
                    return selected_area, areas[selected_area]
                else:
                    print("Please enter a number between 1 and 11.")
            except ValueError:
                print("Please enter a valid number.")
    
    
    def match_skills(self) -> tuple[str, list[int]]:
        print("Please indicate if you possess any of the following skills:")
        print("1. Communication skills")
        print("2. Foreign languages")
        print("3. Cooking")
        print("4. Communication with animals")
        print("5. Communication with children")
        print("6. Conduct trainings")
        print("7. No specific skills")

        skills = {
            "Communication": [8,9,17,16,18],  # Mapping skills to corresponding mission IDs
            "Foreign languages": [12],
            "Cooking": [2],
            "Communication with animals": [29, 30],
            "Communication with children":[5,14],
            "Conduct trainings":[18],
            "No specific skills":[]
        }

        while True:
            try:
                skill_choice = int(input("Enter the number corresponding to your skill (1-6) or 0 if none of the above: "))
                if skill_choice == 0:
                    return ('', [])
                elif 1 <= skill_choice <= 7:
                    selected_skill = list(skills.keys())[skill_choice - 1]
                    return selected_skill, skills[selected_skill]
                else:
                    print("Please enter a number between 1 and 7 or 0 to stop.")
            except ValueError:
                print("Please enter a valid number.")
    
    def match_preferred_time(self):
        print("Choose your preferred volunteering time:")
        print("1. Morning")
        print("2. Afternoon")
        print("3. Evening")
        print("4. Flexible")
        print("5. Full day")
        print("6. Anytime")
        print("7. Weekends")

        time_options = {
            1: "Morning",
            2: "Afternoon",
            3: "Evening",
            4: "Flexible",
            5: "Full day",
            6: "Anytime",
            7: "Weekends"
        }

        while True:
            try:
                time_choice = int(input("Enter the number corresponding to your preferred time (1-7): "))
                if 1 <= time_choice <= 7:
                    selected_time = time_options[time_choice]
                    return selected_time
                else:
                    print("Please enter a number between 1 and 7.")
            except ValueError:
                print("Please enter a valid number.")  
      

    def run(self):
        locations_id_to_search = []
        mission_id = []

        missions = data.get_missions()
  
        locations = data.get_locations()
        # print(locations)
        branch = data.get_branches()
        # print(branch)

        age = self.get_age()
        r = matcher.validate_age(age)
        mission_id_list_proffesion = self.match_profession()
        print(mission_id_list_proffesion)
        mission_id_list_area = self.preferred_volunteering_area()[1]
        print(mission_id_list_area)
        mission_id_skills = self.match_skills()[1]
        print(mission_id_skills)
        has_car = self.match_car_needed()
        time = self.match_preferred_time() 
        print(time)       
        district = self.get_district(locations)
        print(district)
        
        mission_id_by_time = [element.mission_id for element in data.get_missions_by_vol_time(time)]
        print(mission_id_by_time)
        location_id_by_district = data.get_location_by_district(district)
        print(location_id_by_district)
        mission_set = matcher.build_mission_list(mission_id_list_proffesion, 
                                   mission_id_list_area, 
                                   mission_id_skills, 
                                   mission_id_by_time)
        location_set = matcher.build_location(district, locations)
        
        result = matcher.get_relevant_missions(mission_set, location_set, has_car)
        print(f"total missions {len(result)}")
        for i in result:
            print(f"{i.mission_id},{i.mission} {i.mission_description}")

    def add_volunteer(self, first_name, last_name, phone, mission_id, mission):
        conn = psycopg2.connect(
            dbname  ='Volunteer_Matching_System',
            user ='postgres',
            host = 'localhost',
            port ='5432'
        )
        cursor = conn.cursor()
        try:
            cursor.execute(
                'INSERT INTO Volunteers (first_name, last_name, phone, mission_id, mission) VALUES (%s, %s, %s, %s, %s)',
                (first_name, last_name, phone, mission_id, mission)
            )
            conn.commit()
            print("Volunteer information inserted successfully!")
        except psycopg2.Error as e:
            conn.rollback()
            print("Error inserting volunteer information:", e)
        finally:
            cursor.close()
            conn.close()
    def ask_volunteering(self, missions):
        for mission in missions:
            answer = input(f"Would you like to volunteer for one of these missions? (yes/no): ").lower()
            if answer == "yes":
                mission_id = input("Enter the ID of the mission you choose: ")
                name = input("Enter your first name: ")
                last_name = input("Enter your last name: ")
                phone = input("Enter your phone number: ")
            elif answer == "no":
                break
            else:
                print("Please answer with 'yes' or 'no'.")    
    ask = SystemRunner()                                        
    ask.ask_volunteering(missions)
    ask.add_volunteer(missions)


r = SystemRunner()
r.run()
