-- divide two numbers
DROP function IF EXISTS SafeDiv;
delimeter $$
CREATE function SafeDiv(a int, b int)
returns float deterministic
BEGIN
    if (b = 0)
    THEN
        return (0);
    ELSE
        return (a / b);
    END IF;
END
$$
delimeter ;
