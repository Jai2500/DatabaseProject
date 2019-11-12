-- MySQL dump 10.13  Distrib 5.7.27, for Linux (x86_64)
--
-- Host: localhost    Database: INCUBATOR
-- ------------------------------------------------------
-- Server version	5.7.27-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `BASED_IN`
--

DROP DATABASE IF EXISTS incubator;

CREATE DATABASE incubator;
USE incubator;

DROP TABLE IF EXISTS `BASED_IN`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `BASED_IN` (
  `StartupID` int(11) NOT NULL,
  `LocationID` int(11) NOT NULL,
  PRIMARY KEY (`StartupID`,`LocationID`),
 /*added */ FOREIGN KEY (`StartupID`) REFERENCES STARTUP(`StartupID`) ON UPDATE CASCADE ON DELETE CASCADE,
 /*added */ FOREIGN KEY (`LocationID`) REFERENCES LOCATION(`Pincode`) ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BASED_IN`
--

LOCK TABLES `BASED_IN` WRITE;
/*!40000 ALTER TABLE `BASED_IN` DISABLE KEYS */;
INSERT INTO `BASED_IN` VALUES (1,400094),(1,500032),(2,250001);
/*!40000 ALTER TABLE `BASED_IN` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DIRECTOR`
--

DROP TABLE IF EXISTS `DIRECTOR`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DIRECTOR` (
  `Name` varchar(50) NOT NULL,
  `StartupID` int(11) NOT NULL,
  `Sex` varchar(20) NOT NULL,
  `Experience` int(11) NOT NULL,
  PRIMARY KEY (`Name`,`StartupID`),
 /*added */ FOREIGN KEY (`StartupID`) REFERENCES STARTUP(`StartupID`) ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DIRECTOR`
--

LOCK TABLES `DIRECTOR` WRITE;
/*!40000 ALTER TABLE `DIRECTOR` DISABLE KEYS */;
INSERT INTO `DIRECTOR` VALUES ('Kamal',1,'Male',10),('Nonidh',2,'Male',2);
/*!40000 ALTER TABLE `DIRECTOR` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DIRECTOR_EDUCATION`
--

DROP TABLE IF EXISTS `DIRECTOR_EDUCATION`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DIRECTOR_EDUCATION` (
  `Name` varchar(50) NOT NULL,
  `StartupID` int(11) NOT NULL,
  `Degree` varchar(50) NOT NULL,
  `Branch` varchar(50) NOT NULL,
  `Year` int(11) NOT NULL,
  PRIMARY KEY (`Name`,`StartupID`,`Degree`,`Branch`,`Year`),
 /*added */ FOREIGN KEY (`StartupID`) REFERENCES STARTUP(`StartupID`) ON UPDATE CASCADE ON DELETE CASCADE
 /*added */ FOREIGN KEY (`Name`) REFERENCES DIRECTOR(`Name`) ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DIRECTOR_EDUCATION`
--

LOCK TABLES `DIRECTOR_EDUCATION` WRITE;
/*!40000 ALTER TABLE `DIRECTOR_EDUCATION` DISABLE KEYS */;
INSERT INTO `DIRECTOR_EDUCATION` VALUES ('Kamal',1,'B.Tech','Computer Science',1990),('Kamal',1,'PhD','Computer Science',2000),('Nonidh',2,'B.Tech','Computer Science',2010),('Nonidh',2,'M.Sc','Natural Sciences',2015);
/*!40000 ALTER TABLE `DIRECTOR_EDUCATION` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `EMPLOYEE`
--

DROP TABLE IF EXISTS `EMPLOYEE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `EMPLOYEE` (
  `EmployeeID` int(11) NOT NULL,
  `EmployeeName` varchar(100) NOT NULL,
  `EmployeeDept` varchar(50) NOT NULL,
  `EmployeeSalary` int(11) NOT NULL,
  `EmployeeSex` varchar(15) NOT NULL,
  `ResourceID` int(11) DEFAULT NULL,
  PRIMARY KEY (`EmployeeID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `EMPLOYEE`
--

LOCK TABLES `EMPLOYEE` WRITE;
/*!40000 ALTER TABLE `EMPLOYEE` DISABLE KEYS */;
INSERT INTO `EMPLOYEE` VALUES (57,'Rajesh','HR',50000,'Male',101),(91,'Ramesh','Sales',20000,'Male',102),(123,'Rita','Finance',100000,'Female',103);
/*!40000 ALTER TABLE `EMPLOYEE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `INDUSTRY`
--

DROP TABLE IF EXISTS `INDUSTRY`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `INDUSTRY` (
  `IndustryID` int(11) NOT NULL,
  `IndustryName` varchar(100) NOT NULL,
  `IndustryType` varchar(100) NOT NULL,
  PRIMARY KEY (`IndustryID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `INDUSTRY`
--

LOCK TABLES `INDUSTRY` WRITE;
/*!40000 ALTER TABLE `INDUSTRY` DISABLE KEYS */;
INSERT INTO `INDUSTRY` VALUES (1,'Transportation','Tertiary'),(2,'Textile','Secondary'),(3,'Agriculture','Primary'),(4,'Horticulture','Primary'),(5,'IT','Tertiary');
/*!40000 ALTER TABLE `INDUSTRY` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `INVESTOR`
--

DROP TABLE IF EXISTS `INVESTOR`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `INVESTOR` (
  `InvestorID` int(11) NOT NULL,
  `DOB` date NOT NULL,
  `Sex` varchar(50) NOT NULL,
  `FirstName` varchar(50) NOT NULL,
  `LastName` varchar(50) NOT NULL,
  `LocationID` int(11) ,
  PRIMARY KEY (`InvestorID`),
 /*added */ FOREIGN KEY (`LocationID`) REFERENCES LOCATION(`Pincode`) ON UPDATE CASCADE ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `INVESTOR`
--

LOCK TABLES `INVESTOR` WRITE;
/*!40000 ALTER TABLE `INVESTOR` DISABLE KEYS */;
INSERT INTO `INVESTOR` VALUES (1,'1990-07-10','Male','Shyam','Gopal',250001),(2,'1991-05-02','Female','Rama','Dewam',400094),(3,'1992-03-29','Male','Anubhav','Trump',710094);
/*!40000 ALTER TABLE `INVESTOR` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `INVESTOR_EDUCATION`
--

DROP TABLE IF EXISTS `INVESTOR_EDUCATION`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `INVESTOR_EDUCATION` (
  `InvestorID` int(11) NOT NULL,
  `Degree` varchar(50) NOT NULL,
  `Branch` varchar(50) NOT NULL,
  `Year` int(11) NOT NULL,
  PRIMARY KEY (`InvestorID`,`Degree`,`Branch`,`Year`),
 /*added*/ FOREIGN KEY (`InvestorID`) REFERENCES INVESTOR(`InvestorID`) ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `INVESTOR_EDUCATION`
--

LOCK TABLES `INVESTOR_EDUCATION` WRITE;
/*!40000 ALTER TABLE `INVESTOR_EDUCATION` DISABLE KEYS */;
INSERT INTO `INVESTOR_EDUCATION` VALUES (1,'B.Tech','Computer Science',1990),(1,'PhD','Computer Science',2000),(2,'B.Tech','Computer Science',2010),(3,'B.Sc','Aeronautical Science',2015);
/*!40000 ALTER TABLE `INVESTOR_EDUCATION` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `INVESTS`
--

DROP TABLE IF EXISTS `INVESTS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `INVESTS` (
  `IndustryID` int(11) NOT NULL ,
  `InvestorID` int(11) NOT NULL,
  `StartupID` int(11) NOT NULL,
  `ResourceID` int(11) NOT NULL,
  `StartDate` date NOT NULL,
  PRIMARY KEY (`IndustryID`,`InvestorID`,`StartupID`,`ResourceID`),
 /*added */ FOREIGN KEY (`StartupID`) REFERENCES STARTUP(`StartupID`) ON UPDATE CASCADE ON DELETE CASCADE,
 /*added */ FOREIGN KEY (`IndustryID`) REFERENCES INDUSTRY(`IndustryID`) ON UPDATE CASCADE ON DELETE CASCADE,
 /*added */ FOREIGN KEY (`InvestorID`) REFERENCES INVESTOR(`InvestorID`) ON UPDATE CASCADE ON DELETE CASCADE,
 /*added */ FOREIGN KEY (`ResourceID`) REFERENCES RESOURCE(`ResourceID`) ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `INVESTS`
--

LOCK TABLES `INVESTS` WRITE;
/*!40000 ALTER TABLE `INVESTS` DISABLE KEYS */;
INSERT INTO `INVESTS` VALUES (1,2,1,101,'2008-01-09'),(2,1,1,101,'2008-01-09'),(2,3,2,102,'2010-10-10');
/*!40000 ALTER TABLE `INVESTS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `LOCATION`
--

DROP TABLE IF EXISTS `LOCATION`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `LOCATION` (
  `Pincode` int(11) NOT NULL,
  `City` varchar(50) NOT NULL,
  `Country` varchar(50) NOT NULL,
  PRIMARY KEY (`Pincode`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LOCATION`
--

LOCK TABLES `LOCATION` WRITE;
/*!40000 ALTER TABLE `LOCATION` DISABLE KEYS */;
INSERT INTO `LOCATION` VALUES (250001,'Meerut','India'),(400094,'Mumbai','India'),(500032,'Hyderabad','India'),(710094,'Hyderabad','Pakistan');
/*!40000 ALTER TABLE `LOCATION` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PROJECT`
--

DROP TABLE IF EXISTS `PROJECT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PROJECT` (
  `ProjectName` varchar(50) NOT NULL,
  `StartupID` int(11) NOT NULL,
  `TimeFrame` int(11) NOT NULL,
  `StartDate` date NOT NULL,
  `NoofEmployees` int(11) NOT NULL,
  PRIMARY KEY (`ProjectName`,`StartupID`),
 /*added */ FOREIGN KEY (`StartupID`) REFERENCES STARTUP(`StartupID`) ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PROJECT`
--

LOCK TABLES `PROJECT` WRITE;
/*!40000 ALTER TABLE `PROJECT` DISABLE KEYS */;
INSERT INTO `PROJECT` VALUES ('AlphaQ',1,200,'2010-10-10',32),('BetaG',2,100,'2000-10-20',25);
/*!40000 ALTER TABLE `PROJECT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `RESOURCE`
--

DROP TABLE IF EXISTS `RESOURCE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `RESOURCE` (
  `ResourceID` int(11) NOT NULL,
  `ResourceValue` int(11) NOT NULL,
  `ResourceType` varchar(100) NOT NULL,
  PRIMARY KEY (`ResourceID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `RESOURCE`
--

LOCK TABLES `RESOURCE` WRITE;
/*!40000 ALTER TABLE `RESOURCE` DISABLE KEYS */;
INSERT INTO `RESOURCE` VALUES (101,1000000,'Capital'),(102,50000,'Workspaces'),(103,50000,'Computers'),(104,10000,'Manufacturing Space');
/*!40000 ALTER TABLE `RESOURCE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `STARTUP`
--

DROP TABLE IF EXISTS `STARTUP`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `STARTUP` (
  `StartupID` int(11) NOT NULL,
  `StartupName` varchar(50) NOT NULL,
  `NoofEmployees` int(11) NOT NULL,
  `Networth` int(11) NOT NULL,
  `ResourceID` int(11) ,
  PRIMARY KEY (`StartupID`),
 /*added */ FOREIGN KEY (`ResourceID`) REFERENCES RESOURCE(`ResourceID`) ON UPDATE CASCADE ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `STARTUP`
--

LOCK TABLES `STARTUP` WRITE;
/*!40000 ALTER TABLE `STARTUP` DISABLE KEYS */;
INSERT INTO `STARTUP` VALUES (1,'Dream View',100,1000000,  101),(2,'Ober Cab Services',200,200000,102);
/*!40000 ALTER TABLE `STARTUP` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `STARTUP_FOUNDERS`
--

DROP TABLE IF EXISTS `STARTUP_FOUNDERS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `STARTUP_FOUNDERS` (
  `StartupID` int(11) NOT NULL,
  `Founder` varchar(50) NOT NULL,
  PRIMARY KEY (`StartupID`,`Founder`),
 /*added */ FOREIGN KEY (`StartupID`) REFERENCES STARTUP(`StartupID`) ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `STARTUP_FOUNDERS`
--

LOCK TABLES `STARTUP_FOUNDERS` WRITE;
/*!40000 ALTER TABLE `STARTUP_FOUNDERS` DISABLE KEYS */;
INSERT INTO `STARTUP_FOUNDERS` VALUES (1,'Ahish Deshpande'),(1,'Utkarsh Mishra'),(2,'Trunapushpa'),(2,'Yoogottam');
/*!40000 ALTER TABLE `STARTUP_FOUNDERS` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-11-11 15:25:46
