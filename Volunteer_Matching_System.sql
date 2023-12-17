CREATE TABLE locations (
    location_id INTEGER PRIMARY KEY,
    address TEXT,
	district TEXT,
    city TEXT,
	country TEXT
);

CREATE TABLE branches(
	branch_id INTEGER PRIMARY KEY,
	location_id INTEGER,
	branch_name TEXT,
	location TEXT,
    contact_info TEXT,
	FOREIGN KEY(location_id) REFERENCES locations(location_id)
);
CREATE TABLE missions (
    mission_id INTEGER PRIMARY KEY,
    mission_description TEXT
);


CREATE TABLE branch_mission (
    branch_id INTEGER,
    mission_id INTEGER,
    FOREIGN KEY(branch_id) REFERENCES branches(branch_id),
    FOREIGN KEY(mission_id) REFERENCES missions(mission_id),
    PRIMARY KEY(branch_id, mission_id)
);
--add max numbers of voluntiers needed to missions column
ALTER TABLE missions DROP COLUMN max_volunteers;
ALTER TABLE missions DROP COLUMN mission_description;
ALTER TABLE missions ADD COLUMN mission TEXT;
ALTER TABLE missions ADD COLUMN mission_description TEXT;
ALTER TABLE missions ADD max_volunteers INTEGER;
SELECT * FROM missions
SELECT * FROM locations
SELECT * FROM branches
DELETE FROM missions;

ALTER TABLE locations ADD COLUMN temp_district TEXT;
ALTER TABLE locations DROP COLUMN temp_district;
ALTER TABLE locations DROP COLUMN country;
ALTER TABLE locations DROP COLUMN city;
ALTER TABLE locations DROP COLUMN district;
ALTER TABLE locations ADD COLUMN city TEXT;
ALTER TABLE locations ADD COLUMN district TEXT;
ALTER TABLE locations ADD COLUMN country TEXT;

