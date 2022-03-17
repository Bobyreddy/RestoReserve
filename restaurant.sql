-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 17, 2022 at 09:57 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 7.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `restaurant`
--

-- --------------------------------------------------------

--
-- Table structure for table `bookinguser`
--

CREATE TABLE `bookinguser` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `r_code` varchar(50) NOT NULL,
  `ph` int(11) NOT NULL,
  `address` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bookinguser`
--

INSERT INTO `bookinguser` (`id`, `name`, `r_code`, `ph`, `address`) VALUES
(11, 'Damara', 'r2', 2147483647, 'Mullur'),
(12, 'ABHI', 'r2', 234567, 'Mullur');

-- --------------------------------------------------------

--
-- Table structure for table `restodata`
--

CREATE TABLE `restodata` (
  `id` int(11) NOT NULL,
  `r_code` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `tables` int(11) NOT NULL,
  `dishes` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `restodata`
--

INSERT INTO `restodata` (`id`, `r_code`, `name`, `tables`, `dishes`) VALUES
(6, 'R2', 'Name', 8, 13);

-- --------------------------------------------------------

--
-- Table structure for table `restouser`
--

CREATE TABLE `restouser` (
  `id` int(11) NOT NULL,
  `r_code` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email_id` varchar(50) NOT NULL,
  `password` varchar(10000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `restouser`
--

INSERT INTO `restouser` (`id`, `r_code`, `name`, `email_id`, `password`) VALUES
(23, 'R1', 'dine', 'sce19cs135@sairamtap.edu.in', 'pbkdf2:sha256:260000$q7q347nbbPsGX2yq$4fd8674af6d5ce34b75150257f629597011ab4ae88ac69e949b18cc3b94497f0'),
(26, 'R2', 'Name', 'damaramohanreddy.1439@gmail.com', 'pbkdf2:sha256:260000$DExc7n4BmXC2l8wv$d38a1605ca08755ac23c7bb6a9998abea2ee50f4ad3912aeec62c52e19d4b4be'),
(30, 'R7', 'Abhi daba', 'abhibglr01@gmail.com', 'pbkdf2:sha256:260000$65UFqV3woW7Uej47$9fbf5dfc0f5029fbf4fc3c88463aaa7ccf4f1c65add282e945b93daba8fca7c8');

-- --------------------------------------------------------

--
-- Table structure for table `test`
--

CREATE TABLE `test` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `test`
--

INSERT INTO `test` (`id`, `name`) VALUES
(1, 'anees'),
(2, 'rehan');

-- --------------------------------------------------------

--
-- Table structure for table `trig`
--

CREATE TABLE `trig` (
  `id` int(11) NOT NULL,
  `r_code` varchar(50) NOT NULL,
  `tables` int(11) NOT NULL,
  `dishes` int(11) NOT NULL,
  `querys` varchar(50) NOT NULL,
  `date` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email_id` varchar(50) NOT NULL,
  `password` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `name`, `email_id`, `password`) VALUES
(11, 'Damara', 'damaramohanreddy.333@gmail.com', 'pbkdf2:sha256:260000$x1w1BPq1a40eXtD8$4f0ac310550f2a6e7267ac1937dad415eb698447c7bb88fd1fb65bd95124b53c'),
(12, 'ABHI', 'ABHI123@GMAIL', 'pbkdf2:sha256:260000$CanrXv3P6mUqlkYd$40da83c911fb41df3a7594be69587e7bfb94ddee6bed7358ddc65ebcd19e347b');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bookinguser`
--
ALTER TABLE `bookinguser`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `restodata`
--
ALTER TABLE `restodata`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `r_code` (`r_code`);

--
-- Indexes for table `restouser`
--
ALTER TABLE `restouser`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `r_code` (`r_code`),
  ADD UNIQUE KEY `email_id` (`email_id`);

--
-- Indexes for table `test`
--
ALTER TABLE `test`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `trig`
--
ALTER TABLE `trig`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email_id` (`email_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bookinguser`
--
ALTER TABLE `bookinguser`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `restodata`
--
ALTER TABLE `restodata`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `restouser`
--
ALTER TABLE `restouser`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `test`
--
ALTER TABLE `test`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `trig`
--
ALTER TABLE `trig`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
