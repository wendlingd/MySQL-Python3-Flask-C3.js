DROP database IF EXISTS bartest;

create database bartest;

DROP TABLE IF EXISTS bartest.groupedbar;

CREATE TABLE bartest.groupedbar (
	Id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	GroupCode INT NOT NULL,
	ReportMonth VARCHAR(25) NOT NULL,
	UniquePVs int NULL,
	UniqueSearches int NULL 
 );

INSERT INTO bartest.groupedbar (GroupCode, ReportMonth, UniquePVs, UniqueSearches)
select 102,'2016-10',1061,270 union
select 102,'2016-11',878,156 union
select 102,'2016-12',721,138 union
select 102,'2017-01',789,191 union
select 102,'2017-02',762,157 union
select 102,'2017-03',822,230 union
select 102,'2017-04',769,306 union
select 102,'2017-05',852,207 union
select 102,'2017-06',645,111;
