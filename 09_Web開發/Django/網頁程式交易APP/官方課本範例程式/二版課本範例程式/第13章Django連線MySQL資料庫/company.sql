/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50718
Source Host           : localhost:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 50718
File Encoding         : 65001

Date: 2018-06-08 16:42:40
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `company`
-- ----------------------------
DROP TABLE IF EXISTS `company`;
CREATE TABLE `company` (
  `StockID` int(10) unsigned NOT NULL,
  `Abbreviation` varchar(10) DEFAULT NULL,
  `URL` varchar(128) DEFAULT NULL,
  `Employees` int(10) unsigned DEFAULT NULL,
  `Capital` bigint(20) DEFAULT NULL,
  `IndustryName` varchar(16) NOT NULL,
  `ListedDate` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`StockID`),
  UNIQUE KEY `Abbrevuation_UNIQUE` (`Abbreviation`),
  UNIQUE KEY `URL_UNIQUE` (`URL`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of company
-- ----------------------------
