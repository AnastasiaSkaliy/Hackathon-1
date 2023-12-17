from dataclasses import dataclass
import psycopg2

@dataclass
class Location:
    location_id: int
    address: str
    city: str
    district: str
    country: str

@dataclass
class Branch:
    branch_id: int
    location_id: int
    branch_name: str
    contact_info: str

@dataclass
class Mission:
    mission_id: int
    mission: str
    mission_description: str
    volunteering_time: str
    car_needed: bool

conn = psycopg2.connect(
    dbname  ='Volunteer_Matching_System',
    user ='postgres',
    host = 'localhost',
    port ='5432'
)
cursor = conn.cursor()

class DataRepository():
    global cursor

    def get_missions(self) -> list[Mission]:
        cursor.execute("SELECT * FROM missions")
        result = cursor.fetchall()
       
        return [Mission(*mission) for mission in result]
    
    def get_locations(self) -> list[Location]:
        cursor.execute("SELECT * FROM locations")
        result = cursor.fetchall()

        return [Location(*location) for location in result]
   
    def get_branches(self) -> list[Branch]:
        cursor.execute("SELECT * FROM branches")
        result = cursor.fetchall()
        
        return [Branch(*branch) for branch in result]
    
    def get_missions_by_vol_time(self, time) -> list[Mission]:
        search_pattern = '%' + time + '%'
        cursor.execute("SELECT * FROM missions WHERE volunteering_time LIKE %s", (search_pattern,))
        result = cursor.fetchall()

        return [Mission(*mission) for mission in result]
    
    def get_location_by_district(self, district) -> list[Location]:
        search_pattern = '%' + district + '%'
        cursor.execute("SELECT * FROM locations WHERE district LIKE %s", (search_pattern,))
        result = cursor.fetchall()

        return [Location(*location) for location in result]
    
    def get_missions_by_criteria(self, mission_id, location_id, has_car) -> list[Mission]:
        query = """
            SELECT m.mission_id, m.mission, m.mission_description, m.volunteering_time, m.car_needed
            FROM missions m
            JOIN branch_mission bm ON m.mission_id = bm.mission_id
            JOIN branches b ON bm.branch_id = b.branch_id
            WHERE b.location_id IN %s
            AND m.car_needed = %s
            AND m.mission_id IN %s
            group by m.mission_id;
            """
        cursor.execute(query, (tuple(location_id), has_car, tuple(mission_id)))
        result = cursor.fetchall()

        return [Mission(*mission) for mission in result]
    
    def add_volunteer(self, first_name, last_name, phone, mission_id, mission):
        cursor = conn.cursor()
        try:
            cursor.execute(
                'INSERT INTO volunteers (first_name, last_name, phone, mission_id, mission) VALUES (%s, %s, %s, %s, %s)',
                (first_name, last_name, phone, mission_id, mission)
            )
            conn.commit()
            print("Volunteer information inserted successfully!")
        except psycopg2.Error as e:
            conn.rollback()
            print("Error inserting volunteer information:", e)
