-- MariaDB dump 10.19  Distrib 10.4.24-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: Transportation-System
-- ------------------------------------------------------
-- Server version    10.4.24-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Clerk`
--

CREATE DATABASE IF NOT EXISTS `Transportation-System`;

USE `Transportation-System`;

DROP TABLE IF EXISTS `Clerk`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Clerk` (
  `Station` int(11) NOT NULL,
  `Start_time` time NOT NULL,
  `End_time` time NOT NULL,
  `NID` bigint(20) NOT NULL,
  PRIMARY KEY (`NID`),
  CONSTRAINT `Clerk_ibfk_1` FOREIGN KEY (`NID`) REFERENCES `Person` (`NID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Clerk`
--

LOCK TABLES `Clerk` WRITE;
/*!40000 ALTER TABLE `Clerk` DISABLE KEYS */;
INSERT INTO `Clerk` VALUES (1,'04:42:00','08:42:00',1542);
/*!40000 ALTER TABLE `Clerk` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Manager`
--

DROP TABLE IF EXISTS `Manager`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Manager` (
  `NID` bigint(20) NOT NULL,
  PRIMARY KEY (`NID`),
  CONSTRAINT `Manager_ibfk_1` FOREIGN KEY (`NID`) REFERENCES `Person` (`NID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Manager`
--

LOCK TABLES `Manager` WRITE;
/*!40000 ALTER TABLE `Manager` DISABLE KEYS */;
INSERT INTO `Manager` VALUES (456789);
/*!40000 ALTER TABLE `Manager` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Person`
--

DROP TABLE IF EXISTS `Person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Person` (
  `NID` bigint(20) NOT NULL,
  `Pname` varchar(120) NOT NULL,
  `Phone_No` int(11) NOT NULL,
  `Email` varchar(120) NOT NULL UNIQUE,
  `DOB` date NOT NULL,
  `Gender` tinyint(1) NOT NULL,
  `Ppassword` varchar(120) NOT NULL,
  PRIMARY KEY (`NID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Person`
--

LOCK TABLES `Person` WRITE;
/*!40000 ALTER TABLE `Person` DISABLE KEYS */;
INSERT INTO `Person` VALUES (20,'sakfk',2021,'scv','2002-12-05',0,'0210'),(554,'sdfsg',215425,'dff','2004-09-28',0,'dfgd'),(1542,'amer',542156,'clerk@clerk.com','2022-05-10',0,'123'),(123456,'user',123456,'user@user.com','2022-05-10',0,'123'),(456789,'manager',123456,'manager@manager.com','2002-12-05',0,'123'),(789456,'wrere',4854,'rere@rere.com','2022-05-04',0,'123');
/*!40000 ALTER TABLE `Person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Seat`
--

DROP TABLE IF EXISTS `Seat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Seat` (
  `SeatID` varchar(10) NOT NULL,
  `CarNo` int(11) NOT NULL,
  `TripID` int(11) NOT NULL,
  `Ticket_ID` int(11) NOT NULL,
  PRIMARY KEY (`SeatID`,`TripID`),
  KEY `TripID` (`TripID`),
  KEY `Ticket_ID` (`Ticket_ID`),
  CONSTRAINT `Seat_ibfk_1` FOREIGN KEY (`TripID`) REFERENCES `Trip` (`TripID`),
  CONSTRAINT `Seat_ibfk_2` FOREIGN KEY (`Ticket_ID`) REFERENCES `Ticket` (`Ticket_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Seat`
--

LOCK TABLES `Seat` WRITE;
/*!40000 ALTER TABLE `Seat` DISABLE KEYS */;
INSERT INTO `Seat` VALUES ('10B',10,874,18),('2B',10,514,16),('4C',10,456,20),('5B',10,515,17),('9D',10,515,19);
/*!40000 ALTER TABLE `Seat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Station`
--

DROP TABLE IF EXISTS `Station`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Station` (
  `StationID` int(11) NOT NULL AUTO_INCREMENT,
  `Sname` varchar(50) NOT NULL,
  PRIMARY KEY (`StationID`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Station`
--

LOCK TABLES `Station` WRITE;
/*!40000 ALTER TABLE `Station` DISABLE KEYS */;
INSERT INTO `Station` VALUES (1,'Alexandria'),(2,'Assiut'),(3,'Aswan'),(4,'Beheira'),(5,'Bani Suef'),(6,'Cairo'),(7,'Daqahliya'),(8,'Damietta'),(9,'Fayyoum'),(10,'Gharbiya'),(11,'Giza'),(12,'Helwan'),(13,'Ismailia'),(14,'Kafr El Sheikh'),(15,'Luxor'),(16,'Marsa Matrouh'),(17,'Minya'),(18,'Monofiya'),(19,'New Valley'),(20,'North Sinai'),(21,'Port Said'),(22,'Qalioubiya'),(23,'Qena'),(24,'Red Sea'),(25,'Sharqiya'),(26,'Sohag'),(27,'South Sinai'),(28,'Suez'),(29,'Tanta');
/*!40000 ALTER TABLE `Station` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Ticket`
--

DROP TABLE IF EXISTS `Ticket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Ticket` (
  `Ticket_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Price` int(11) NOT NULL,
  `TDate` date NOT NULL,
  `TripID` int(11) NOT NULL,
  `Owner_NID` bigint(20) NOT NULL,
  PRIMARY KEY (`Ticket_ID`),
  KEY `TripID` (`TripID`),
  KEY `Owner_NID` (`Owner_NID`),
  CONSTRAINT `Ticket_ibfk_1` FOREIGN KEY (`TripID`) REFERENCES `Trip` (`TripID`),
  CONSTRAINT `Ticket_ibfk_2` FOREIGN KEY (`Owner_NID`) REFERENCES `Person` (`NID`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Ticket`
--

LOCK TABLES `Ticket` WRITE;
/*!40000 ALTER TABLE `Ticket` DISABLE KEYS */;
INSERT INTO `Ticket` VALUES (16,250,'2022-05-19',514,123456),(17,250,'2022-05-19',515,123456),(18,250,'2022-05-19',874,123456),(19,250,'2022-05-19',515,123456),(20,250,'2022-05-19',456,123456);
/*!40000 ALTER TABLE `Ticket` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Trip`
--

DROP TABLE IF EXISTS `Trip`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Trip` (
  `TripID` int(11) NOT NULL AUTO_INCREMENT,
  `DepartureDate` date NOT NULL,
  `DepartureTime` time NOT NULL,
  `ArrivalTime` time NOT NULL,
  `StationID` int(11) NOT NULL,
  `TOStationID` int(11) NOT NULL,
  PRIMARY KEY (`TripID`),
  KEY `StationID` (`StationID`),
  KEY `TOStationID` (`TOStationID`),
  CONSTRAINT `Trip_ibfk_1` FOREIGN KEY (`StationID`) REFERENCES `Station` (`StationID`),
  CONSTRAINT `Trip_ibfk_2` FOREIGN KEY (`TOStationID`) REFERENCES `Station` (`StationID`)
) ENGINE=InnoDB AUTO_INCREMENT=875 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Trip`
--

LOCK TABLES `Trip` WRITE;
/*!40000 ALTER TABLE `Trip` DISABLE KEYS */;
INSERT INTO `Trip` VALUES (456,'2022-05-21','04:44:00','07:44:00',1,6),(514,'2022-05-20','11:45:00','18:45:00',17,26),(515,'2022-05-23','06:44:00','08:44:00',6,9),(874,'2022-05-30','06:45:00','10:45:00',5,16);
/*!40000 ALTER TABLE `Trip` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `User` (
  `NID` bigint(20) NOT NULL,
  PRIMARY KEY (`NID`),
  CONSTRAINT `User_ibfk_1` FOREIGN KEY (`NID`) REFERENCES `Person` (`NID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (123456);
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-14 23:34:44
