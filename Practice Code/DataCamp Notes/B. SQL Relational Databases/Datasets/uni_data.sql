CREATE TABLE university_professors(
    first_name character varying(50),
    last_name character varying(50),
    university character varying(50),
    university_shortname character varying(50),
    university_city character varying(50),
    functions character varying(255),
    organisation character varying(255),
    organisation_sector character varying(255)
);

COPY university_professors (first_name, last_name, university, university_shortname, university_city, functions, organisation,organisation_sector) 
FROM 'uni_profs.csv' DELIMITER ',' CSV HEADER;

