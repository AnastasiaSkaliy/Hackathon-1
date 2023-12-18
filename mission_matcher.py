#This file builds all missions
#This file receives all the user's choices and searches for the right missions
# after applying all the filters (using the volunteer_repository file).

from volunteer_repository import DataRepository

data = DataRepository()

class MissionMatcher:
    global data
    def validate_age(self, age):
        if age < 18:
            raise Exception("Sorry, only individuals aged 18 and above can volunteer.")
        return True

    def build_mission_list(self, mission_id_list_proffesion, mission_id_list_area, mission_id_skills, mission_id_by_time) -> list[int]:
        mission_set = set().union(mission_id_list_proffesion,mission_id_list_area, mission_id_skills)
        return mission_set
    
    def build_location(self, district, locations) -> list[int]:
        locations = filter(lambda x: x.district == district, locations)
        ids = [element.location_id for element in list(locations)]

        return ids
    
    def get_relevant_missions(self, mission_ids, location_ids, has_car):
        return data.get_missions_by_criteria(mission_ids, location_ids, has_car)