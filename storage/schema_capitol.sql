-- MySQL dump 10.16  Distrib 10.1.48-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: fdb34.awardspace.net    Database: 4098422_capitol
-- ------------------------------------------------------
-- Server version	5.7.20-log

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
  `Start_time` Time NOT NULL,
  `End_time` Time NOT NULL,
  `NID` int(11) NOT NULL,
  PRIMARY KEY (`NID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Clerk`
--

LOCK TABLES `Clerk` WRITE;
/*!40000 ALTER TABLE `Clerk` DISABLE KEYS */;
/*!40000 ALTER TABLE `Clerk` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Client`
--

DROP TABLE IF EXISTS `Client`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Client` (
  `NID` int(11) NOT NULL,
  PRIMARY KEY (`NID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Client`
--

LOCK TABLES `Client` WRITE;
/*!40000 ALTER TABLE `Client` DISABLE KEYS */;
/*!40000 ALTER TABLE `Client` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Electronic_Ticket`
--

DROP TABLE IF EXISTS `Electronic_Ticket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Electronic_Ticket` (
  `Ticket_ID` int(11) NOT NULL,
  PRIMARY KEY (`Ticket_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Electronic_Ticket`
--

LOCK TABLES `Electronic_Ticket` WRITE;
/*!40000 ALTER TABLE `Electronic_Ticket` DISABLE KEYS */;
/*!40000 ALTER TABLE `Electronic_Ticket` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Manager`
--

DROP TABLE IF EXISTS `Manager`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Manager` (
  `NID` int(11) NOT NULL,
  PRIMARY KEY (`NID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Manager`
--

LOCK TABLES `Manager` WRITE;
/*!40000 ALTER TABLE `Manager` DISABLE KEYS */;
/*!40000 ALTER TABLE `Manager` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Paper_Ticket`
--

DROP TABLE IF EXISTS `Paper_Ticket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Paper_Ticket` (
  `Ticket_ID` int(11) NOT NULL,
  PRIMARY KEY (`Ticket_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Paper_Ticket`
--

LOCK TABLES `Paper_Ticket` WRITE;
/*!40000 ALTER TABLE `Paper_Ticket` DISABLE KEYS */;
/*!40000 ALTER TABLE `Paper_Ticket` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Person`
--

DROP TABLE IF EXISTS `Person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Person` (
  `NID` int(11) NOT NULL,
  `Phone_No` int(11) NOT NULL,
  `Email` varchar(150) NOT NULL,
  `DOB` date NOT NULL,
  `Gender` tinyint(1) NOT NULL,
  `Password` varchar(150) NOT NULL,
  PRIMARY KEY (`NID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Person`
--

LOCK TABLES `Person` WRITE;
/*!40000 ALTER TABLE `Person` DISABLE KEYS */;
/*!40000 ALTER TABLE `Person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Seat`
--

DROP TABLE IF EXISTS `Seat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Seat` (
  `SeatID` int(11) NOT NULL,
  `CarNo` int(11) NOT NULL,
  `TripID` int(11) NOT NULL,
  `Ticket_ID` int(11) NOT NULL,
  PRIMARY KEY (`SeatID`,`TripID`,`Ticket_ID`),
  KEY `TripID` (`TripID`),
  KEY `Ticket_ID` (`Ticket_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Seat`
--

LOCK TABLES `Seat` WRITE;
/*!40000 ALTER TABLE `Seat` DISABLE KEYS */;
/*!40000 ALTER TABLE `Seat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Seat_bookedInterval`
--

DROP TABLE IF EXISTS `Seat_bookedInterval`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Seat_bookedInterval` (
  `bookedInterval` int(11) NOT NULL,
  `SeatID` int(11) NOT NULL,
  `TripID` int(11) NOT NULL,
  `Ticket_ID` int(11) NOT NULL,
  PRIMARY KEY (`bookedInterval`,`SeatID`,`TripID`,`Ticket_ID`),
  KEY `SeatID` (`SeatID`,`TripID`,`Ticket_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Seat_bookedInterval`
--

LOCK TABLES `Seat_bookedInterval` WRITE;
/*!40000 ALTER TABLE `Seat_bookedInterval` DISABLE KEYS */;
/*!40000 ALTER TABLE `Seat_bookedInterval` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Station`
--

DROP TABLE IF EXISTS `Station`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Station` (
  `StationID` int(11) NOT NULL,
  `SName` varchar(150) NOT NULL,
  PRIMARY KEY (`StationID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Station`
--

LOCK TABLES `Station` WRITE;
/*!40000 ALTER TABLE `Station` DISABLE KEYS */;
/*!40000 ALTER TABLE `Station` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Ticket`
--

DROP TABLE IF EXISTS `Ticket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Ticket` (
  `Ticket_ID` int(11) NOT NULL,
  `Price` int(11) NOT NULL,
  `TDate` Date NOT NULL,
  `TripID` int(11) NOT NULL,
  PRIMARY KEY (`Ticket_ID`),
  KEY `TripID` (`TripID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Ticket`
--

LOCK TABLES `Ticket` WRITE;
/*!40000 ALTER TABLE `Ticket` DISABLE KEYS */;
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
  `TrainID` int(11) NOT NULL,
  `DepartureTime` TIME NOT NULL,
  `ArrivalTime` TIME NOT NULL,
  `DepartureDate` DATE NOT NULL,
  `sourceStation` int(11) NOT NULL,
  `destinationStation` int(11) NOT NULL,
  PRIMARY KEY (`TripID`),
  FOREIGN KEY (`sourceStation`) REFERENCES `Station`(`StationID`),
  FOREIGN KEY (`destinationStation`) REFERENCES `Station`(`StationID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Trip`
--

LOCK TABLES `Trip` WRITE;
/*!40000 ALTER TABLE `Trip` DISABLE KEYS */;
/*!40000 ALTER TABLE `Trip` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database '4098422_capitol'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-08 22:50:20
