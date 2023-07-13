-- Reset email after change
DELIMETER $$
CREATE TRIGGER changedEmail_trigger
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
IF new.email <> old.email
THEN
    SET new.valid_email = 0;
END IF
END
$$
DELIMETER ;
