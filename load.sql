COPY passengers
FROM '/Users/pavanpaj/UB Courses/Sem2 Aug-Dec24/CSE 560 - DMQL - Shreyasree/Project/passengers_table.csv'
DELIMITER ','
CSV HEADER;

select * from passengers;

COPY flights
FROM '/Users/pavanpaj/UB Courses/Sem2 Aug-Dec24/CSE 560 - DMQL - Shreyasree/Project/flight_table.csv'
DELIMITER ','
CSV HEADER;

select * from flights;

COPY satisfaction_ratings
FROM '/Users/pavanpaj/UB Courses/Sem2 Aug-Dec24/CSE 560 - DMQL - Shreyasree/Project/satisfaction_ratings_table.csv'
DELIMITER ','
CSV HEADER;

select * from satisfaction_ratings;



COPY delays
FROM '/Users/pavanpaj/UB Courses/Sem2 Aug-Dec24/CSE 560 - DMQL - Shreyasree/Project/delays_table.csv'
DELIMITER ','
CSV HEADER;

select * from delays;


COPY overall_satisfaction
FROM '/Users/pavanpaj/UB Courses/Sem2 Aug-Dec24/CSE 560 - DMQL - Shreyasree/Project/overall_satisfaction_table.csv'
DELIMITER ','
CSV HEADER;

select * from overall_satisfaction;