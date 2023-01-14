CREATE TABLE `booking` (
  `bookingid` int(10) NOT NULL,
  `aid` int(10) NOT NULL,
  `fname` varchar(20) NOT NULL,
  `lname` varchar(20) NOT NULL,
  `email` varchar(30) NOT NULL,
  `city` varchar(20) NOT NULL,
  `fphone` int(15) NOT NULL,
  `fdestination` varchar(20) NOT NULL,
  'cost' int(15) NOT NULL,
   PRIMARY KEY (bookingid));


INSERT INTO booking values('1','1', 'amogh', 'skanda', 'amoghs387@gmail.com', 'bangalore', '9844776655', 'Goa','5000','none');
INSERT INTO booking values('2','2', 'ananya', 'menon', 'ananya@gmail.com', 'Kerala', '9988776655', 'Delhi','6000','none');
INSERT INTO booking values('3','1', 'virat', 'kohli', 'virat18@gmail.com', 'Delhi', '8056070890', 'Bangalore','3000','none');


CREATE TABLE `customer` (
  `customerid` int(10) NOT NULL,
  `fname` varchar(20) NOT NULL,
  `lname` varchar(20) NOT NULL,
  `email` varchar(30) NOT NULL,
  `city` varchar(10) NOT NULL,
  `phone` bigint(12) NOT NULL,
  PRIMARY KEY (customerid),
  FOREIGN KEY (customerid) REFERENCES booking(bookingid) ON DELETE CASCADE
);


INSERT INTO customer values('1', 'amogh', 'skanda', 'amoghs387@gmail.com', 'bangalore', '9844776655')
INSERT INTO customer values('2', 'ananya', 'menon', 'ananya@gmail.com', 'kerala', '9988776655')
INSERT INTO customer values('3', 'virat', 'kohli', 'goat@gmail.com', 'delhi', '8056070890')

CREATE TABLE `feedback` (
  `id` int(10) NOT NULL,
  `name` varchar(20) NOT NULL,
  `email` varchar(30) NOT NULL,
  `feedbk` varchar(1000) NOT NULL,
  PRIMARY KEY (id)
);

INSERT INTO feedback values('1', 'amogh', 'amoghs387@gmail.com', 'TRIP IT is one of the best booking websites out there and im glad to have used their service')
INSERT INTO feedback values('2', 'ananya', 'ananya@gmail.com', 'spellbound by their service')
INSERT INTO feedback values('3', 'virat',  'goat@gmail.com', 'very good planner, covered everything at a competitive price')


CREATE TABLE `places` (
  `pid` int(10) NOT NULL,
  `pname` varchar(20) NOT NULL,
  `pcity` varchar(20) NOT NULL,
  'lname' varchar(20) NOT NULL,
  PRIMARY KEY (pid)
);





CREATE TABLE `information` (
  `pname` varchar(30) NOT NULL,
  `pid` int(10) NOT NULL,
  `pdescription` varchar(10000) NOT NULL,
  `cost` int(20) NOT NULL,
  FOREIGN KEY (pid) REFERENCES places(pid) ON DELETE CASCADE);




CREATE TABLE `travel_agent` (
  `aid` int(10) NOT NULL,
  `afname` varchar(20) NOT NULL,
  `alname` varchar(20) NOT NULL,
  `aemail` varchar(30) NOT NULL,
  `aphone` int(15) NOT NULL,
  `acity` varchar(20) NOT NULL,
  PRIMARY KEY (aid)
);


INSERT INTO places values('1', 'candolim beach', ' goa');
INSERT INTO places values('2', 'red fort', 'delhi');
INSERT INTO places values('3', 'anjuna beach',  'goa');
INSERT INTO places values('4', 'koramangala', ' bangalore');
INSERT INTO places values('5', 'kochi museum', 'kerala');
INSERT INTO places values('6', 'ub city',  'bangalore');
INSERT INTO places values('7', 'mehrauli',  'delhi');

INSERT INTO information values('candolim beach','1','It is the very first beach which can be reached from the Panaji city. The beach presents its visitors with soft glittering sand and an unforgettable sight of sea. The sight of massive waves waving at you constantly is something which will form a permanent place in your memories','5000');
INSERT INTO information values('red fort','2','Built by Mughal emperor Shah Jahan as the palace fort of his capital Shahjahanabad, the Red Fort is famous for its massive enclosing walls. The forts construction was completed over a span of ten years, between 1638 and 1648.','6000');
INSERT INTO information values('anjuna beach','3','The beach is famous for its stunning ambiance arraying with swaying palms trees and is marked by an unusual rocky formation overlying a cove of white sand and black rock that juts out into the Sea.','7000');
INSERT INTO information values('koramangala','4','One of the most expensive localities in Bangalore with multiple restaurants and cafes to visit','500');
INSERT INTO information values('kochi museum','5','One of the best museums in Kerala. Must visit place, has a lot of cultural heritage','5000');
INSERT INTO information values('ub city','6','One of indias most expensive malls. Has upscale restaurants for dining and luxurious brands from all over the world','6000');
INSERT INTO information values('mehrauli','7','It has the qutub minar. Must visit place in Delhi','7000');

INSERT INTO travel_agent values('1', 'kripal','amanna','krip@gmail.com','9356784','bangalore');
INSERT INTO travel_agent values('2', 'kiran','kumar','kk@gmail.com','8097652','delhi');
INSERT INTO travel_agent values('3', 'mohan','das', 'mkg@gmail.com','7336571','goa');

INSERT INTO travel_agent values('3','ravi','nair', 'ravinair07@gmail.com','6362815','kerala');


--join

SELECT bid,lname,fdesti,travel_agent.afname,travel_agent.aphone FROM booking JOIN travel_agent ON booking.aid=travel_agent.aid;

SELECT fname,lname,customer.email,feedback.feedbk
FROM customer
RIGHT JOIN feedback
ON customer.cid=feedback.id;

SELECT *SELECT places.pid,places.pname,places.pcity,pdescription,cost FROM information JOIN places ON places.pid=information.pid;

FROM places
LEFT JOIN information ON places.pid=information.pid,

--aggregate

SELECT COUNT(*)  FROM customer;  

SELECT places.pid,places.pname,pcity,cost
FROM places,information
WHERE places.pid=information.pid and cost < (SELECT AVG(cost)
                    FROM information);

SELECT MAX(cost) AS LargestPrice
FROM information; 


SELECT MIN(cost) AS LargestPrice
FROM information; 


--set
SELECT aid as id, afname as name FROM travel_agent
UNION
SELECT bid as id, fname as name FROM booking;


SELECT fname as name FROM booking   intersect SELECT name FROM feedback;

SELECT fname FROM booking UNION ALL SELECT fname FROM customer;



SELECT fname
FROM booking
EXCEPT
SELECT name 
FROM feedback;

--procedure
DELIMITER //
CREATE procedure get_feed()
BEGIN
SELECT * FROM feedback;
end //
DELIMITER ;

CALL get_feed()

--function

DELIMITER //
CREATE FUNCTION calc_due_price( starting_value INT,id INT)
RETURNS INT
BEGIN
DECLARE price INT;
DECLARE due INT;
SELECT cost INTO price FROM information WHERE pid=id;
SET due = price - starting_value;
RETURN due;
END; //
DELIMITER ;

SELECT calc_due_price(2000,1);

--TRIGGER
delimiter //
DELIMITER $$

    CREATE TRIGGER viva_trigger BEFORE UPDATE ON `booking`
    FOR EACH ROW BEGIN
      IF (NEW.cost < 3000) THEN
            SET NEW.reward="you get free breakfast";
      ELSE
            SET NEW.reward="you get free breakfast and lunch";
      END IF;
    END$$
DELIMITER ;

--CURSOR
  
DELIMITER $$
CREATE PROCEDURE cEmailList (
	INOUT emailList varchar(4000)
)
BEGIN
	DECLARE finished INTEGER DEFAULT 0;
	DECLARE emailAddress varchar(100) DEFAULT "";

	DEClARE curEmail 
		CURSOR FOR 
			SELECT email FROM booking;

	DECLARE CONTINUE HANDLER 
        FOR NOT FOUND SET finished = 1;

	OPEN curEmail;

	getEmail: LOOP
		FETCH curEmail INTO emailAddress;
		IF finished = 1 THEN 
			LEAVE getEmail;
		END IF;
		SET emailList = CONCAT(emailAddress,";",emailList);
	END LOOP getEmail;
	CLOSE curEmail;
END$$
DELIMITER ;

SET @emailList = ""; 
CALL createEmailList(@emailList); 
SELECT @emailList;



--TRIGGER
delimiter //



DELIMITER $$

    CREATE TRIGGER add_tax BEFORE UPDATE ON `information`
    FOR EACH ROW BEGIN
      IF (NEW.cost < 5000) THEN
            SET NEW.cost = NEW.cost+20;
      ELSE
            SET NEW.cost = PNEW.cost+50;
      END IF;
    END$$

DELIMITER ;


--TRIGGER 2

DELIMITER$$
CREATE TRIGGER esa_trigger BEFORE UPDATE on `booking`
FOR EACH ROW
BEGIN
DECLARE error_msg varchar(100)
SET error_msg = ('NOT POSSIBLE SIR')
IF NEW.qty > 2*(old.qty) THEN
  SIGNAL SQLSTATE '45000'
  SET MESSAGE_TEXT = error_msg
END IF
END$$
DELIMITER;



INSERT INTO bookedpackages( bid, pid, fname, pname, cost,reward)
SELECT name, bid, pid, fname, pname, cost
FROM booking ,information
WHERE booking.aid=information.pid if(bid not in bookedpackages.bid )



CREATE TABLE `bookedpackages` (
  `bid` int(10) NOT NULL,
  `pid` int(10) NOT NULL,
  `fname` varchar(20) NOT NULL,
  `pname` varchar(30) NOT NULL,
  `cost` int(20) NOT NULL,
  `reward` varchar(30) NOT NULL;
DELIMITER $$

    CREATE TRIGGER add_tax BEFORE UPDATE ON `information`
    FOR EACH ROW BEGIN
      IF (NEW.cost < 5000) THEN
            SET NEW.cost = NEW.cost+20;
      ELSE
            SET NEW.cost = PNEW.cost+50;
      END IF;
    END$$

DELIMITER ;


ALTER TABLE booking ALTER COLUMN rewards varchar(50) NOT NULL,;