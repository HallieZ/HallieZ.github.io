-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Apr 01, 2020 at 05:11 AM
-- Server version: 5.7.24
-- PHP Version: 7.3.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `linku`
--

-- --------------------------------------------------------

--
-- Table structure for table `newsall`
--

CREATE TABLE `newsall` (
  `title` varchar(40) NOT NULL,
  `cover` varchar(255) NOT NULL,
  `brief` varchar(90) DEFAULT NULL,
  `url` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `newsall`
--

INSERT INTO `newsall` (`title`, `cover`, `brief`, `url`) VALUES
('B站/抖音/Keep 平台特性有哪些差别', 'http://edu.cnr.cn/list/20150922/W020150922360259944631.jpg', '逐个击破还是全面撒网？', 'news3.html'),
('中外健身KOL现状对比：差距明显', 'http://img4.imgtn.bdimg.com/it/u=411905806,1437895098&fm=11&gp=0.jpg', '健身KOL变现渠道狭窄', 'news2.html'),
('迪卡侬营销案例分享 你离与大牌合作还有多远', 'http://pic1.jumeili.cn/upload/2019/5/30/c349f54c-79a3-4175-99cc-4e2cee6330c6.jpg', '广告商青睐的KOL是这样的', 'news1.html');

-- --------------------------------------------------------

--
-- Table structure for table `newscase`
--

CREATE TABLE `newscase` (
  `title` varchar(40) NOT NULL,
  `cover` varchar(255) NOT NULL,
  `brief` varchar(90) DEFAULT NULL,
  `url` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `newscase`
--

INSERT INTO `newscase` (`title`, `cover`, `brief`, `url`) VALUES
('迪卡侬营销案例分享 你离与大牌合作还有多远', 'http://pic1.jumeili.cn/upload/2019/5/30/c349f54c-79a3-4175-99cc-4e2cee6330c6.jpg', '广告商青睐的KOL是这样的', 'news1.html');

-- --------------------------------------------------------

--
-- Table structure for table `newsexp`
--

CREATE TABLE `newsexp` (
  `title` varchar(40) NOT NULL,
  `cover` varchar(255) NOT NULL,
  `brief` varchar(90) DEFAULT NULL,
  `url` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `newsexp`
--

INSERT INTO `newsexp` (`title`, `cover`, `brief`, `url`) VALUES
('B站/抖音/Keep 平台特性有哪些差别', 'http://edu.cnr.cn/list/20150922/W020150922360259944631.jpg', '逐个击破还是全面撒网？', 'news3.html');

-- --------------------------------------------------------

--
-- Table structure for table `newsmkt`
--

CREATE TABLE `newsmkt` (
  `title` varchar(40) NOT NULL,
  `cover` varchar(255) NOT NULL,
  `brief` varchar(90) DEFAULT NULL,
  `url` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `newsmkt`
--

INSERT INTO `newsmkt` (`title`, `cover`, `brief`, `url`) VALUES
('中外健身KOL现状对比：差距明显', 'http://img4.imgtn.bdimg.com/it/u=411905806,1437895098&fm=11&gp=0.jpg', '健身KOL变现渠道狭窄', 'news2.html');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `newscase`
--
ALTER TABLE `newscase`
  ADD PRIMARY KEY (`title`);

--
-- Indexes for table `newsexp`
--
ALTER TABLE `newsexp`
  ADD PRIMARY KEY (`title`);

--
-- Indexes for table `newsmkt`
--
ALTER TABLE `newsmkt`
  ADD PRIMARY KEY (`title`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
