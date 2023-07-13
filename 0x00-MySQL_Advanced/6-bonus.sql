-- Add bonus
DROP procedure IF EXISTS AddBonus;
delimeter $$
CREATE procedure AddBonus (
    IN user_id int,
    IN project_name varchar(255),
    IN score float)
BEGIN
    declare project_id int;
    IF (SELECT count(*) FROM projects WHERE name = project_name) = 0
    THEN
        INSERT INTO projects (name) values (project_name);
    END IF;
    SET project_id = (SELECT id FROM projects WHERE name = project_name LIMIT 1);
    INSERT INTO corrections (user_id, project_id, score) VALUES(user_id, project_id, score);
END
$$
delimeter ;
