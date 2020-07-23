-- MySQL dump 10.13  Distrib 8.0.20, for macos10.15 (x86_64)
--
-- Host: localhost    Database: GlenDB
-- ------------------------------------------------------
-- Server version	8.0.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `DivTab`
--

DROP TABLE IF EXISTS `DivTab`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `DivTab` (
  `Div_ID` int NOT NULL,
  `Div_name` text,
  PRIMARY KEY (`Div_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DivTab`
--

LOCK TABLES `DivTab` WRITE;
/*!40000 ALTER TABLE `DivTab` DISABLE KEYS */;
INSERT INTO `DivTab` VALUES (1,'Glenburn'),(2,'Kimble'),(3,'Simbong');
/*!40000 ALTER TABLE `DivTab` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `FieldEntry`
--

DROP TABLE IF EXISTS `FieldEntry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `FieldEntry` (
  `Field_id` int NOT NULL,
  `Date` datetime DEFAULT NULL,
  `Job_ID` int DEFAULT NULL,
  `Sec_ID` int DEFAULT NULL,
  `Squ_ID` int DEFAULT NULL,
  `Mnd_Val` float DEFAULT NULL,
  `Area_Val` float(4,2) DEFAULT NULL,
  `GL_Val` float DEFAULT NULL,
  PRIMARY KEY (`Field_id`),
  KEY `Job_ID_idx` (`Job_ID`),
  KEY `Sec_ID_idx` (`Sec_ID`),
  KEY `Squ_ID_idx` (`Squ_ID`),
  CONSTRAINT `Job_ID` FOREIGN KEY (`Job_ID`) REFERENCES `Jobtab` (`Job_ID`),
  CONSTRAINT `Sec_ID` FOREIGN KEY (`Sec_ID`) REFERENCES `SecTab` (`Sec_ID`),
  CONSTRAINT `Squ_ID` FOREIGN KEY (`Squ_ID`) REFERENCES `SquTab` (`Squ_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `FieldEntry`
--

LOCK TABLES `FieldEntry` WRITE;
/*!40000 ALTER TABLE `FieldEntry` DISABLE KEYS */;
INSERT INTO `FieldEntry` VALUES (1,'2020-07-01 00:00:00',1,1,7,30,2.20,320),(2,'2020-07-01 00:00:00',1,2,6,40,2.40,430),(3,'2020-07-01 00:00:00',1,3,5,35,2.30,340),(4,'2020-07-01 00:00:00',2,4,4,30,1.60,NULL),(5,'2020-07-01 00:00:00',2,5,3,40,3.20,NULL),(6,'2020-07-01 00:00:00',3,6,2,30,2.40,NULL),(7,'2020-07-01 00:00:00',4,7,1,20,2.40,NULL),(8,'2020-07-01 00:00:00',5,NULL,NULL,25,NULL,NULL),(9,'2020-07-01 00:00:00',6,NULL,NULL,20,NULL,NULL),(10,'2020-07-01 00:00:00',7,NULL,NULL,15,NULL,NULL),(11,'2020-07-02 00:00:00',1,10,1,30,2.20,350),(12,'2020-07-02 00:00:00',1,9,2,40,2.40,320),(13,'2020-07-02 00:00:00',1,8,3,35,2.30,400),(18,'2020-07-02 00:00:00',5,NULL,NULL,25,NULL,NULL),(19,'2020-07-02 00:00:00',6,NULL,NULL,20,NULL,NULL),(20,'2020-07-02 00:00:00',7,NULL,NULL,15,NULL,NULL),(21,'2020-07-03 00:00:00',1,1,7,30,2.20,450),(22,'2020-07-03 00:00:00',1,2,6,40,2.40,380),(23,'2020-07-03 00:00:00',1,3,5,35,2.30,320),(28,'2020-07-03 00:00:00',5,NULL,NULL,25,NULL,NULL),(29,'2020-07-03 00:00:00',6,NULL,NULL,20,NULL,NULL),(30,'2020-07-03 00:00:00',7,NULL,NULL,15,NULL,NULL),(31,'2020-07-04 00:00:00',1,10,1,30,2.20,520),(32,'2020-07-04 00:00:00',1,9,2,40,2.40,380),(33,'2020-07-04 00:00:00',1,8,3,35,2.30,340),(38,'2020-07-04 00:00:00',5,NULL,NULL,25,NULL,NULL),(39,'2020-07-04 00:00:00',6,NULL,NULL,20,NULL,NULL),(40,'2020-07-04 00:00:00',7,NULL,NULL,15,NULL,NULL),(41,'2020-07-05 00:00:00',1,1,7,30,2.20,320),(42,'2020-07-05 00:00:00',1,2,6,40,2.40,430),(43,'2020-07-05 00:00:00',1,3,5,35,2.30,340),(48,'2020-07-05 00:00:00',5,NULL,NULL,25,NULL,NULL),(49,'2020-07-05 00:00:00',6,NULL,NULL,20,NULL,NULL),(50,'2020-07-06 00:00:00',7,NULL,NULL,15,NULL,NULL),(51,'2020-07-05 00:00:00',1,10,1,30,2.20,320),(52,'2020-07-06 00:00:00',1,9,2,40,2.40,430),(53,'2020-07-06 00:00:00',1,8,3,35,2.30,340),(58,'2020-07-06 00:00:00',5,NULL,NULL,25,NULL,NULL),(59,'2020-07-06 00:00:00',6,NULL,NULL,20,NULL,NULL),(60,'2020-07-06 00:00:00',7,NULL,NULL,15,NULL,NULL),(100,'2020-07-11 00:00:00',1,1,7,30,320.00,2.2),(101,'2020-07-11 00:00:00',1,2,6,40,430.00,2.4),(102,'2020-07-12 00:00:00',1,3,5,35,340.00,2.3),(103,'2020-07-12 00:00:00',2,4,4,30,NULL,1.6),(104,'2020-07-13 00:00:00',2,5,3,40,NULL,3.2),(105,'2020-07-13 00:00:00',3,6,2,30,NULL,2.4),(106,'2020-07-14 00:00:00',4,7,1,20,NULL,2.4),(107,'2020-07-14 00:00:00',5,NULL,NULL,25,NULL,NULL);
/*!40000 ALTER TABLE `FieldEntry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `FLEntry`
--

DROP TABLE IF EXISTS `FLEntry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `FLEntry` (
  `FL_ID` int NOT NULL,
  `Date` datetime DEFAULT NULL,
  `Div_ID` int DEFAULT NULL,
  `FL_Per` float DEFAULT NULL,
  PRIMARY KEY (`FL_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `FLEntry`
--

LOCK TABLES `FLEntry` WRITE;
/*!40000 ALTER TABLE `FLEntry` DISABLE KEYS */;
INSERT INTO `FLEntry` VALUES (1,'2020-07-02 00:00:00',1,56),(2,'2020-07-02 00:00:00',2,59),(3,'2020-07-02 00:00:00',3,60),(4,'2020-07-02 00:00:00',1,58),(5,'2020-07-02 00:00:00',2,57),(6,'2020-07-02 00:00:00',3,61),(7,'2020-07-03 00:00:00',1,59),(8,'2020-07-03 00:00:00',2,62),(9,'2020-07-03 00:00:00',3,60);
/*!40000 ALTER TABLE `FLEntry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `FuelEntry`
--

DROP TABLE IF EXISTS `FuelEntry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `FuelEntry` (
  `Fue_ID` int NOT NULL,
  `Date` datetime DEFAULT NULL,
  `Fuel_ID` int DEFAULT NULL,
  `Mach_ID` int DEFAULT NULL,
  `Fuel_Val` float DEFAULT NULL,
  PRIMARY KEY (`Fue_ID`),
  KEY `Fuel_id_idx` (`Fuel_ID`),
  KEY `Mach_ID_idx` (`Mach_ID`),
  CONSTRAINT `Fuel_id` FOREIGN KEY (`Fuel_ID`) REFERENCES `FuelTab` (`Fuel_ID`),
  CONSTRAINT `Mach_ID` FOREIGN KEY (`Mach_ID`) REFERENCES `MachineTab` (`Mach_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `FuelEntry`
--

LOCK TABLES `FuelEntry` WRITE;
/*!40000 ALTER TABLE `FuelEntry` DISABLE KEYS */;
INSERT INTO `FuelEntry` VALUES (1,'2020-07-01 00:00:00',1,1,10),(2,'2020-07-01 00:00:00',1,2,30),(3,'2020-07-01 00:00:00',2,3,80),(4,'2020-07-02 00:00:00',1,1,20),(5,'2020-07-02 00:00:00',1,2,40),(6,'2020-07-02 00:00:00',2,3,90),(7,'2020-07-03 00:00:00',1,1,30),(8,'2020-07-03 00:00:00',1,2,40),(9,'2020-07-03 00:00:00',2,3,70);
/*!40000 ALTER TABLE `FuelEntry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `FuelTab`
--

DROP TABLE IF EXISTS `FuelTab`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `FuelTab` (
  `Fuel_ID` int NOT NULL,
  `Fuel_Name` text,
  PRIMARY KEY (`Fuel_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `FuelTab`
--

LOCK TABLES `FuelTab` WRITE;
/*!40000 ALTER TABLE `FuelTab` DISABLE KEYS */;
INSERT INTO `FuelTab` VALUES (1,'HSD'),(2,'Coal');
/*!40000 ALTER TABLE `FuelTab` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `InvoiceEntry`
--

DROP TABLE IF EXISTS `InvoiceEntry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `InvoiceEntry` (
  `Inv_ID` int NOT NULL,
  `Packdate` datetime DEFAULT NULL,
  `Invoice_No` text,
  `TeaGrade_ID` int DEFAULT NULL,
  `Net_Wt` float DEFAULT NULL,
  `Papersacks` int DEFAULT NULL,
  `Dispatch Date` datetime DEFAULT NULL,
  PRIMARY KEY (`Inv_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `InvoiceEntry`
--

LOCK TABLES `InvoiceEntry` WRITE;
/*!40000 ALTER TABLE `InvoiceEntry` DISABLE KEYS */;
INSERT INTO `InvoiceEntry` VALUES (1,'2020-07-01 00:00:00','DJ1',1,150,6,'2020-07-03 00:00:00'),(2,'2020-07-01 00:00:00','DJ2',2,200,7,'2020-07-03 00:00:00'),(3,'2020-07-01 00:00:00','DJ3',3,150,5,'2020-07-03 00:00:00'),(4,'2020-07-01 00:00:00','DJ4',4,130,6,'2020-07-03 00:00:00'),(5,'2020-07-01 00:00:00','DJ5',5,150,5,'2020-07-03 00:00:00');
/*!40000 ALTER TABLE `InvoiceEntry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Jobtab`
--

DROP TABLE IF EXISTS `Jobtab`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Jobtab` (
  `Job_ID` int NOT NULL,
  `Job_Name` text,
  PRIMARY KEY (`Job_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Jobtab`
--

LOCK TABLES `Jobtab` WRITE;
/*!40000 ALTER TABLE `Jobtab` DISABLE KEYS */;
INSERT INTO `Jobtab` VALUES (1,'Plucking'),(2,'Spray Foliar'),(3,'Spray Pest'),(4,'Spray Weed'),(5,'Sickling'),(6,'Hand Weeding'),(7,'Manuring'),(8,'Factory'),(9,'Nursery'),(10,'Chowkidar'),(11,'Hospital'),(12,'Transport'),(13,'Creche');
/*!40000 ALTER TABLE `Jobtab` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MachineTab`
--

DROP TABLE IF EXISTS `MachineTab`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `MachineTab` (
  `Mach_ID` int NOT NULL,
  `Mach_Name` text,
  PRIMARY KEY (`Mach_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MachineTab`
--

LOCK TABLES `MachineTab` WRITE;
/*!40000 ALTER TABLE `MachineTab` DISABLE KEYS */;
INSERT INTO `MachineTab` VALUES (1,'Drier'),(2,'Wither Drier'),(3,'Genset');
/*!40000 ALTER TABLE `MachineTab` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SecTab`
--

DROP TABLE IF EXISTS `SecTab`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `SecTab` (
  `Sec_ID` int NOT NULL,
  `Sec_Name` text,
  `Sec_Area` float DEFAULT NULL,
  `Div_ID` int DEFAULT NULL,
  `Sec_Jat` text,
  `Sec_Prune` text,
  PRIMARY KEY (`Sec_ID`),
  KEY `Div_ID_idx` (`Div_ID`),
  CONSTRAINT `Div_ID` FOREIGN KEY (`Div_ID`) REFERENCES `DivTab` (`Div_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SecTab`
--

LOCK TABLES `SecTab` WRITE;
/*!40000 ALTER TABLE `SecTab` DISABLE KEYS */;
INSERT INTO `SecTab` VALUES (1,'1a',2.4,1,'av2','UP'),(2,'1b',3.5,1,'av2','UP'),(3,'1c',5.3,1,'as','CA'),(4,'1d',3.6,1,'ch','UP'),(5,'2',3.1,1,'av2','UP'),(6,'3',3.5,2,'av2','CA'),(7,'4a',6.4,2,'ch','CA'),(8,'bjb',2.4,2,'as','UP'),(9,'cba1',3.5,2,'ch','CA'),(10,'cba2',5.3,2,'av2','UP'),(11,'8',3.6,2,'av2','UP'),(12,'9',3.1,2,'as','DS'),(13,'10',3.5,3,'as','DS'),(14,'11',6.4,3,'p312','DS'),(15,'12a',2.4,3,'av2','UP'),(16,'12b',3.5,3,'av2','UP'),(17,'12c',5.3,3,'as','UP');
/*!40000 ALTER TABLE `SecTab` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SortEntry`
--

DROP TABLE IF EXISTS `SortEntry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `SortEntry` (
  `Sort_ID` int NOT NULL,
  `Date` datetime DEFAULT NULL,
  `TM_Date` datetime DEFAULT NULL,
  `TeaGrade_ID` int DEFAULT NULL,
  `Sort_Kg` float DEFAULT NULL,
  PRIMARY KEY (`Sort_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SortEntry`
--

LOCK TABLES `SortEntry` WRITE;
/*!40000 ALTER TABLE `SortEntry` DISABLE KEYS */;
INSERT INTO `SortEntry` VALUES (1,'2020-07-02 00:00:00','2020-07-01 00:00:00',1,140),(2,'2020-07-02 00:00:00','2020-07-01 00:00:00',2,40),(3,'2020-07-02 00:00:00','2020-07-01 00:00:00',3,20),(4,'2020-07-02 00:00:00','2020-07-01 00:00:00',4,20),(5,'2020-07-02 00:00:00','2020-07-01 00:00:00',5,20),(6,'2020-07-02 00:00:00','2020-07-01 00:00:00',6,10),(7,'2020-07-03 00:00:00','2020-07-02 00:00:00',1,130),(8,'2020-07-03 00:00:00','2020-07-02 00:00:00',2,30),(9,'2020-07-03 00:00:00','2020-07-02 00:00:00',3,25),(10,'2020-07-03 00:00:00','2020-07-02 00:00:00',4,25),(11,'2020-07-03 00:00:00','2020-07-02 00:00:00',5,20),(12,'2020-07-03 00:00:00','2020-07-02 00:00:00',6,10);
/*!40000 ALTER TABLE `SortEntry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SquTab`
--

DROP TABLE IF EXISTS `SquTab`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `SquTab` (
  `Squ_ID` int NOT NULL,
  `Squ_Name` text,
  PRIMARY KEY (`Squ_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SquTab`
--

LOCK TABLES `SquTab` WRITE;
/*!40000 ALTER TABLE `SquTab` DISABLE KEYS */;
INSERT INTO `SquTab` VALUES (1,'Squad1'),(2,'Squad2'),(3,'Squad3'),(4,'Squad4'),(5,'Squad5'),(6,'Squad6'),(7,'Squad7'),(8,'Squad8'),(9,'Squad9'),(10,'Squad10');
/*!40000 ALTER TABLE `SquTab` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `StockEntry`
--

DROP TABLE IF EXISTS `StockEntry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `StockEntry` (
  `Stock_ID` int NOT NULL,
  `Date` datetime DEFAULT NULL,
  `TeaType_ID` int DEFAULT NULL,
  `TeaGrade_ID` int DEFAULT NULL,
  `Kg_Val` float DEFAULT NULL,
  PRIMARY KEY (`Stock_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `StockEntry`
--

LOCK TABLES `StockEntry` WRITE;
/*!40000 ALTER TABLE `StockEntry` DISABLE KEYS */;
INSERT INTO `StockEntry` VALUES (2,'2020-07-01 00:00:00',2,1,400),(3,'2020-07-01 00:00:00',2,2,200),(4,'2020-07-01 00:00:00',2,3,150),(5,'2020-07-01 00:00:00',2,4,100),(6,'2020-07-01 00:00:00',2,5,20),(7,'2020-07-01 00:00:00',2,6,10),(9,'2020-07-02 00:00:00',2,1,400),(10,'2020-07-02 00:00:00',2,2,200),(11,'2020-07-02 00:00:00',2,3,150),(12,'2020-07-02 00:00:00',2,4,100),(13,'2020-07-02 00:00:00',2,5,20),(14,'2020-07-02 00:00:00',2,6,10),(16,'2020-07-03 00:00:00',2,1,400),(17,'2020-07-03 00:00:00',2,2,200),(18,'2020-07-03 00:00:00',2,3,150),(19,'2020-07-03 00:00:00',2,4,100),(20,'2020-07-03 00:00:00',2,5,20),(21,'2020-07-03 00:00:00',2,6,10);
/*!40000 ALTER TABLE `StockEntry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TeaGradeTab`
--

DROP TABLE IF EXISTS `TeaGradeTab`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `TeaGradeTab` (
  `TeaGrade_ID` int NOT NULL,
  `TeaGrade_Name` text,
  PRIMARY KEY (`TeaGrade_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TeaGradeTab`
--

LOCK TABLES `TeaGradeTab` WRITE;
/*!40000 ALTER TABLE `TeaGradeTab` DISABLE KEYS */;
INSERT INTO `TeaGradeTab` VALUES (1,'FTGFOP1'),(2,'TGBOP'),(3,'TGOF'),(4,'OF'),(5,'BT'),(6,'LT');
/*!40000 ALTER TABLE `TeaGradeTab` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TeaTypeTab`
--

DROP TABLE IF EXISTS `TeaTypeTab`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `TeaTypeTab` (
  `TeaType_ID` int NOT NULL,
  `TeaType_Name` text,
  PRIMARY KEY (`TeaType_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TeaTypeTab`
--

LOCK TABLES `TeaTypeTab` WRITE;
/*!40000 ALTER TABLE `TeaTypeTab` DISABLE KEYS */;
INSERT INTO `TeaTypeTab` VALUES (1,'Unsorted'),(2,'Sorted');
/*!40000 ALTER TABLE `TeaTypeTab` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TMEntry`
--

DROP TABLE IF EXISTS `TMEntry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `TMEntry` (
  `TM_ID` int NOT NULL,
  `TM_Date` datetime DEFAULT NULL,
  `TM_Val` float DEFAULT NULL,
  PRIMARY KEY (`TM_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TMEntry`
--

LOCK TABLES `TMEntry` WRITE;
/*!40000 ALTER TABLE `TMEntry` DISABLE KEYS */;
INSERT INTO `TMEntry` VALUES (1,'2020-07-01 00:00:00',250),(2,'2020-07-02 00:00:00',240),(3,'2020-07-03 00:00:00',260);
/*!40000 ALTER TABLE `TMEntry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `WeatherEntry`
--

DROP TABLE IF EXISTS `WeatherEntry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `WeatherEntry` (
  `Date` datetime NOT NULL,
  `Rain` float DEFAULT NULL,
  `Max_Temp` float DEFAULT NULL,
  `Min_Temp` float DEFAULT NULL,
  PRIMARY KEY (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `WeatherEntry`
--

LOCK TABLES `WeatherEntry` WRITE;
/*!40000 ALTER TABLE `WeatherEntry` DISABLE KEYS */;
INSERT INTO `WeatherEntry` VALUES ('2020-07-01 00:00:00',1.2,31,23),('2020-07-02 00:00:00',0,29,22),('2020-07-03 00:00:00',0.8,18,24);
/*!40000 ALTER TABLE `WeatherEntry` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-07-23 15:35:08
