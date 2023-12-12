-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 12, 2023 at 07:53 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `myblog`
--

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `srno` int(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `mobile_no` varchar(50) NOT NULL,
  `message` text NOT NULL,
  `name` text NOT NULL,
  `date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`srno`, `email`, `mobile_no`, `message`, `name`, `date`) VALUES
(1, 'h@m.com', '61313300155', 'tefgkfghk;g;mdmhh.', 'Hiral', '2023-12-05 08:12:17'),
(2, 'hiral.dharod@gmail.com', '+919821087355', 'bnv bm vmm', 'Hiral Dharod', NULL),
(3, 'hiral.dharod@gmail.com', '+919821087355', 'bnv bm vmm', 'Hiral Dharod', '2023-12-05 13:41:23'),
(4, 'bbc@gmail.com', '1346790000', 'Hi this is testing dte vlue', 'Hiral', '2023-12-05 13:41:54'),
(5, 'bbc@gmail.com', '1346790000', 'Hi this is testing dte vlue', 'Hiral', '2023-12-06 11:07:15'),
(6, 'ds@h.com', '23135465464', 'this is test message to test mail', 'kffkgn', '2023-12-06 11:08:42'),
(7, 'fgf@h.mcom', '131354444+4', 'fdfm', 'fv', '2023-12-06 11:17:51'),
(8, 'cddb@gmail.com', 'vdfb', 'cfff', 'vvvv', '2023-12-06 11:25:34'),
(9, 'aaa@m.com', '1111111111', 'testr', 'aaa', '2023-12-06 11:43:01');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `srno` int(50) NOT NULL,
  `title` text NOT NULL,
  `subheading` varchar(500) NOT NULL,
  `slug` varchar(20) NOT NULL,
  `content` text NOT NULL,
  `img_file` varchar(50) NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`srno`, `title`, `subheading`, `slug`, `content`, `img_file`, `date`) VALUES
(1, 'This is my first post', 'This is subheading', 'first-post', 'This is first post content. This is first post content. This is first post content. This is first post content. This is first post content. This is first post content.', 'assets/img/post-bg.jpg', '2023-12-06 11:55:31'),
(5, 'second post', 'second post subheding', 'second-post', 'This is second post content. This is second post content. This is second post content. This is second post content. This is second post content. This is second post content. This is second post content. This is second post content.', '2.png', '2023-12-08 13:50:31'),
(6, 'third post', 'third post subheading', 'third-post', 'This is third post content. This is third post content. This is third post content. This is third post content. This is third post content. This is third post content. This is third post content. This is third post content. ', '3.png', '2023-12-08 13:51:38'),
(7, 'fourth post', 'fourth post subheading', 'fourth-post', 'This is fourth post content. This is fourth post content. This is fourth post content. This is fourth post content. This is fourth post content. This is fourth post content. This is fourth post content. This is fourth post content. This is fourth post content. This is fourth post content. ', '4.png', '2023-12-08 13:52:58'),
(8, 'fifth post', 'fifth post subheading', 'fifth-post', 'This is fifth post content. This is fifth post content. This is fifth post content. This is fifth post content. This is fifth post content. This is fifth post content. This is fifth post content. This is fifth post content. This is fifth post content. This is fifth post content. ', '5.png', '2023-12-08 13:53:50'),
(9, 'sixth post', 'sixth post subheading', 'sixth-post', 'This is sixth post content. This is sixth post content. This is sixth post content. This is sixth post content. This is sixth post content. This is sixth post content. This is sixth post content. This is sixth post content. This is sixth post content. This is sixth post content. This is sixth post content. ', '6.png', '2023-12-08 13:55:06'),
(10, '7th post', '7th post subheading', '7-post', 'This is seventh post content. This is seventh post content. This is seventh post content. This is seventh post content. This is seventh post content. This is seventh post content. This is seventh post content. This is seventh post content. This is seventh post content. ', '7.png', '2023-12-08 13:57:05');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`srno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`srno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `srno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `srno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
