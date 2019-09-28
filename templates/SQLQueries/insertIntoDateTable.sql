Create OR REPLACE FUNCTION createDateTable(
)
RETURNS VOID as $$
DECLARE
	iterator integer := 1;
	startdate date := now();
BEGIN
Delete from public."dateTable";
	WHILE iterator < 999
	LOOP
		Insert INTO public."dateTable" ("theDate", "DayOfWeek")
		Values (startdate,to_char(startdate, 'day'));
		iterator := iterator + 1;
		startdate := startdate + interval '1' day;
	END LOOP;
END;
$$ LANGUAGE plpgsql;

Select createDateTable();

Select * from public."dateTable"

