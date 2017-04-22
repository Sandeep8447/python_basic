-- MySQL dump 10.13  Distrib 5.6.19, for osx10.9 (x86_64)
--
-- Host: 192.168.2.211    Database: audit
-- ------------------------------------------------------
-- Server version	5.6.24-0ubuntu2

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
-- Table structure for table `audit_log`
--

DROP TABLE IF EXISTS `audit_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `audit_log` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `user` varchar(30) NOT NULL,
  `ip` varchar(30) NOT NULL,
  `host_user` varchar(30) NOT NULL,
  `cmd` varchar(30) NOT NULL,
  `date` datetime(6) NOT NULL ON UPDATE CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `audit_log`
--

LOCK TABLES `audit_log` WRITE;
/*!40000 ALTER TABLE `audit_log` DISABLE KEYS */;
INSERT INTO `audit_log` VALUES (45,'alex','192.168.2.211','alex','ls','2015-08-28 20:57:02.000000'),(46,'alex','192.168.2.211','alex','pwd','2015-08-28 20:57:02.000000'),(47,'alex','192.168.2.211','alex','df','2015-08-28 20:57:03.000000'),(48,'alex','192.168.2.211','alex','ls','2015-08-28 20:57:04.000000'),(49,'alex','192.168.2.211','alex','ls','2015-08-28 20:57:04.000000'),(50,'alex','192.168.2.211','alex','ls','2015-08-28 20:57:05.000000'),(51,'alex','192.168.2.211','alex','s','2015-08-28 20:57:05.000000'),(52,'alex','192.168.2.211','alex','s','2015-08-28 20:57:06.000000'),(53,'alex','192.168.2.211','alex','ls','2015-08-28 20:57:07.000000'),(54,'alex','192.168.2.211','alex','df','2015-08-28 20:57:07.000000'),(55,'alex','192.168.2.211','alex','ls','2015-08-28 20:57:08.000000');
/*!40000 ALTER TABLE `audit_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bind_hosts`
--

DROP TABLE IF EXISTS `bind_hosts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bind_hosts` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `host_id` int(10) NOT NULL,
  `host_user_id` int(10) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `host_id` (`host_id`),
  KEY `host_user_id` (`host_user_id`),
  CONSTRAINT `bind_hosts_ibfk_1` FOREIGN KEY (`host_id`) REFERENCES `hosts` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `bind_hosts_ibfk_2` FOREIGN KEY (`host_user_id`) REFERENCES `host_users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bind_hosts`
--

LOCK TABLES `bind_hosts` WRITE;
/*!40000 ALTER TABLE `bind_hosts` DISABLE KEYS */;
INSERT INTO `bind_hosts` VALUES (7,7,0),(8,8,1),(9,9,2),(10,10,3),(12,11,3),(13,8,0);
/*!40000 ALTER TABLE `bind_hosts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `groups`
--

DROP TABLE IF EXISTS `groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `groups` (
  `name` varchar(30) NOT NULL,
  `id` int(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `groups`
--

LOCK TABLES `groups` WRITE;
/*!40000 ALTER TABLE `groups` DISABLE KEYS */;
INSERT INTO `groups` VALUES ('BJ',0),('SH',1),('WEB',2);
/*!40000 ALTER TABLE `groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `host_groups`
--

DROP TABLE IF EXISTS `host_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `host_groups` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `user_id` int(10) NOT NULL,
  `bind_host_id` int(10) NOT NULL,
  `group_id` int(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `host_groups`
--

LOCK TABLES `host_groups` WRITE;
/*!40000 ALTER TABLE `host_groups` DISABLE KEYS */;
INSERT INTO `host_groups` VALUES (8,125,7,1),(9,125,8,2),(10,126,9,0),(11,125,8,0),(12,125,10,0),(13,125,11,0),(14,125,13,0);
/*!40000 ALTER TABLE `host_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `host_users`
--

DROP TABLE IF EXISTS `host_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `host_users` (
  `username` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  `id` int(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `host_users`
--

LOCK TABLES `host_users` WRITE;
/*!40000 ALTER TABLE `host_users` DISABLE KEYS */;
INSERT INTO `host_users` VALUES ('alex','alex3714',0),('root','edd',1),('alex','222',2),('mysql','dfd',3);
/*!40000 ALTER TABLE `host_users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hosts`
--

DROP TABLE IF EXISTS `hosts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hosts` (
  `hostname` varchar(30) NOT NULL,
  `ip` varchar(30) NOT NULL,
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `port` int(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hosts`
--

LOCK TABLES `hosts` WRITE;
/*!40000 ALTER TABLE `hosts` DISABLE KEYS */;
INSERT INTO `hosts` VALUES ('localhost','127.0.0.1',7,22),('ubuntu','192.168.2.211',8,22),('cent os','10.8.3.44',9,22),('redhat','172.0.34.55',10,22),('web server','192.168.2.211',11,22);
/*!40000 ALTER TABLE `hosts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `username` varchar(30) NOT NULL,
  `password` varchar(255) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=128 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('','alex',123),('jack','123',124),('alex','123',125),('jack','321',126),('eric','dfsfd',127);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-08-28 21:05:43
