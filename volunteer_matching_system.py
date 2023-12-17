import psycopg2
import random

#establish connection 
conn = psycopg2.connect(
    dbname  ='Volunteer_Matching_System',
    user ='postgres',
    host = 'localhost',
    port ='5432'
)
cursor = conn.cursor()
#insert data to location table
# locations_data = [
#     (1, '123 Main St', 'Tel Aviv', 'Central District','Israel'),
#     (2, '456 Oak Ave', 'Jerusalem', 'Jerusalem District','Israel'),
#     (3, '789 Maple Rd', 'Haifa', 'Haifa District','Israel'),
#     (4, '202 Cedar Street', 'Rishon LeZion','Central District','Israel'),
#     (5, '303 Elm Boulevard', 'Petah Tikva','Central District','Israel'),
#     (6, '707 Maple Court', 'Ashdod','Southern District','Israel'),
#     (7, '404 Birch Avenue', 'Netanya','Central District','Israel'),
#     (8, '101 Pine Lane', 'Beersheba','Southern District','Israel'),
#     (9, '505 Willow Way', 'Holon','Central District','Israel'),
#     (10,'313 Maple Lane', 'Ramat Gan','Central District','Israel'),
#     (11, '414 Cedar Avenue', 'Rehovot','Central District','Israel'),
#     (12, '808 Pinecrest Avenue', 'Bat Yam','Central District','Israel'),
#     (13, '101 Pine Lane', 'Kfar Saba','Central District','Israel'),
#     (14, '789 Maple Rd', 'Nazareth','Northern District','Israel'),
#     (15, '123 Main St', 'Acre','Northern District','Israel'),
#     (16, '508 Willow Way', 'Ashqelon','Southern District','Israel'),
#     (17, '717 Maple Court', 'Eilat','Southern District','Israel'),
#     (18, '809 Pinecrest Avenue', 'Arad','Southern District','Israel'),
#     (19, '107 Birch Avenue', 'Sderot','Southern District','Israel'),
#     (20, '790 Maple Rd', 'Nahariyya','Northern District','Israel')
# ]
# insert_query = "INSERT INTO locations (location_id, address, city, district, country) VALUES (%s, %s, %s, %s, %s)"
# cursor.executemany(insert_query, locations_data)

# conn.commit()
# cursor.close()
# conn.close()

#insert data to branches table
# branches_data = [
#     (1, 1, 'Branch Tel Aviv', 'Tel Aviv'),
#     (2, 2, 'Branch Jerusalem', 'Jerusalem'),
#     (3, 3, 'Branch Haifa', 'Haifa'),
#     (4, 4, 'Branch Rishon', 'Rishon LeZion'),
#     (5, 5, 'Branch Petah Tikva', 'Petah Tikva'),
#     (6, 6, 'Branch Ashdod', 'Ashdod'),
#     (7, 7, 'Branch Netanya', 'Netanya'),
#     (8, 8, 'Branch Beersheba', 'Beersheba'),
#     (9, 9, 'Branch Holon', 'Holon'),
#     (10, 10, 'Branch Ramat Gan', 'Ramat Gan'),
#     (11, 11, 'Branch Rehovot', 'Rehovot'),
#     (12, 12, 'Branch Bat Yam', 'Bat Yam'),
#     (13, 13, 'Branch Kfar Saba', 'Kfar Saba'),
#     (14, 14, 'Branch Nazareth', 'Nazareth'),
#     (15, 15, 'Branch Acre', 'Acre'),
#     (16, 16, 'Branch Ashqelon', 'Ashqelon'),
#     (17, 17, 'Branch Eilat', 'Eilat'),
#     (18, 18, 'Branch Arad', 'Arad'),
#     (19, 19, 'Branch Sderot', 'Sderot'),
#     (20, 20, 'Branch Nahariyya', 'Nahariyya')
# ]

# phone_numbers = [
#     f"03-{random.randint(1000000, 9999999)}"
#     for _ in range(20)
# ]
# # Generate 20 phone numbers starting with '03'
# branches_data_with_phone = [
#     branch + (phone,)  # Concatenate the phone number to each branch tuple
#     for branch, phone in zip(branches_data, phone_numbers)
# ]

# Insert data into branches table

# insert_query = "INSERT INTO branches (branch_id, location_id, branch_name, location,contact_info) VALUES (%s, %s, %s, %s, %s)"
# cursor.executemany(insert_query, branches_data_with_phone)
# conn.commit()
# cursor.close()
# conn.close()

#insert data to missions table
# missions_data = [
#     (1,'Food Distribution for Soldiers', 'Drive and distribute food supplies to soldiers on the front lines.', 'Morning,Afternoon,Flexible,Anytime',True),
#     (2,'Cooking for Soldiers', 'Prepare and cook meals for soldiers in military camps.','Morning,Afternoon,Evening,Flexible,Full Day,Anytime,Weekends',False ),
#     (3,'Clothes Distribution for Refugees', 'Help in distributing clothes to refugees affected by war.','Morning, Afternoon,Evening,Flexible,Full Day,Anytime,Weekends', False),
#     (4,'Medical Support for War Victims', 'Provide medical aid and support to civilians impacted by war.','Morning, Afternoon,Flexible', False),
#     (5,'Entertainment for children affected by war', 'Come up with and organize an entertainment program for children','Morning, Afternoon,Flexible,Weekends',False ),
#     (6, 'Psychological assistance to children affected by war','Provide psychological assistance to children','Morning, Afternoon,Flexible,Weekends',False),
#     (7,'Emergency Supply Transport to Conflict Areas', 'Transport essential supplies to areas affected by conflict.','Morning,Afternoon,Evening,Flexible,Full Day,Anytime,Weekends', True),
#     (8,'Social media','Maintain social networks of our organization, communicate with people there and guide them in accordance with their request','Morning,Afternoon,Evening,Flexible,Full Day,Anytime,Weekends',False),
#     (9,'Telephone operator','Answer phone calls, direct people to destinations depending on their problem','Morning,Afternoon,Evening,Flexible,Full Day,Anytime,Weekends',False),
#     (10,'Emergency Medical Evacuation Support', 'Assist in organizing and providing emergency medical evacuation services for wounded soldiers.','Morning,Afternoon,Evening,Flexible,Full Day,Anytime,Weekends', False),
#     (11,'Aid Coordination for Displaced Families', 'Coordinate and manage aid distribution for families forced to flee conflict zones.','Morning,Afternoon,Evening,Flexible,Full Day,Anytime,Weekends', False),
#     (12,'Language Interpretation Services', 'Provide language interpretation services for refugees and displaced individuals.','Morning,Afternoon,Evening,Flexible,Full Day,Anytime,Weekends', False),
#     (13,'Creating Safe Zones for Civilians', 'Work towards establishing safe zones and shelters for civilians during conflicts.','Morning, Afternoon,Flexible,Weekends', False),
#     (14,'Educational Support for War-Affected Children', 'Offer educational support and activities for children impacted by war.','Morning, Afternoon,Evening,Flexible,Weekends', False),
#     (15,'Supply Chain Management for Relief Materials', 'Manage and optimize supply chains for efficient distribution of relief materials.','Morning,Afternoon,Evening,Flexible,Full Day,Anytime,Weekends', True),
#     (16,'Psychosocial Support Groups for Trauma Healing', 'Organize support groups to help individuals cope with trauma caused by war.','Morning,Afternoon,Evening,Flexible,Full Day,Anytime,Weekends', False),
#     (17,'Media Campaigns for Humanitarian Causes', 'Contribute to media campaigns raising awareness and support for humanitarian causes in war zones.','Morning,Afternoon,Evening,Flexible,Full Day,Anytime,Weekends', False),
#     (18,'Disaster Preparedness Training', 'Provide training sessions to communities on disaster preparedness and response.','Morning,Afternoon,Evening,Flexible,Full Day,Anytime,Weekends', False),
#     (19,'Livelihood Restoration Initiatives', 'Initiate programs aimed at restoring livelihoods for people affected by war.','Morning,Afternoon,Evening,Flexible,Full Day,Anytime,Weekends', False),
#     (20,'Refugee Camp Support Coordination', 'Coordinate efforts to support refugee camps with essential needs and services.','Morning,Afternoon,Evening,Flexible,Full Day,Anytime,Weekends', False),
#     (21,'Legal Aid Services for War Victims', 'Provide legal aid services to war victims and assist in accessing justice.','Morning,Afternoon,Evening,Flexible,Full Day,Anytime,Weekends', False),
#     (22,'Trauma Counseling Workshops', 'Organize workshops focused on trauma counseling and mental health support.','Morning,Afternoon,Evening,Flexible,Full Day,Anytime,Weekends', False),
#     (23,'Documentation of Human Rights Violations', 'Document and report human rights violations occurring in conflict zones.','Morning,Afternoon,Evening,Flexible,Full Day,Anytime,Weekends', False),
#     (24,'Veterinary Services for Animals Affected by War', 'Offer veterinary care and support for animals impacted by war.','Morning,Afternoon,Evening,Flexible,Full Day,Anytime,Weekends', False),
#     (25,'Material aid','Coordinate monetary donations','Morning,Afternoon,Evening,Flexible,Full Day,Anytime,Weekends',False),
#     (26,'Logistics Support for Humanitarian Aid', 'Provide logistical support to ensure efficient delivery of humanitarian aid.','Morning,Afternoon,Evening,Flexible,Full Day,Anytime,Weekends', True),
#     (27,'Livestock and Agriculture Rehabilitation', 'Assist in reviving livestock and agriculture in conflict-affected areas.','Morning,Afternoon,Evening,Flexible,Full Day,Anytime,Weekends', False),
#     (28,'Providing housing to refugees','Invite refugees to live with you during the war/provide them with housing','Morning,Afternoon,Evening,Flexible,Full Day,Anytime,Weekends',False),
#     (29,'Foster animals','Temporarily take animals from a war zone into your foster home','Morning,Afternoon,Evening,Flexible,Full Day,Anytime,Weekends',False),
#     (30,'Adopt animals','Adopt an animal that is left without owners','Morning,Afternoon,Evening,Flexible,Full Day,Anytime,Weekends',False)
# ]

# insert_query = "INSERT INTO missions (mission_id, mission, mission_description, volunteering_time,car_needed) VALUES (%s, %s, %s, %s, %s)"
# cursor.executemany(insert_query, missions_data)


# conn.commit()
# cursor.close()
# conn.close()

#Insert data to branch_mission table
# First 10 branches connected to all 30 missions
# for branch_id in range(1, 11):
#     for mission_id in range(1, 31):
#         insert_query = "INSERT INTO branch_mission (branch_id, mission_id) VALUES (%s, %s)"
#         cursor.execute(insert_query, (branch_id, mission_id))

# Last 10 branches connected to 20 missions each
# for branch_id in range(11, 21):
#     for mission_id in range(1, 21):
#         insert_query = "INSERT INTO branch_mission (branch_id, mission_id) VALUES (%s, %s)"
#         cursor.execute(insert_query, (branch_id, mission_id))        

# conn.commit()
# cursor.close()
# conn.close()







