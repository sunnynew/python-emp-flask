CREATE TABLE `tbl_emp` (
  `userId` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `jobTitleName` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `firstName` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `lastName` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `preferredFullName` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `employeeCode` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `region` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `phoneNumber` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `emailAddress` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`employeeCode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
