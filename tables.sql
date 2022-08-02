CREATE TABLE `customers` (
  `customer_id` int NOT NULL AUTO_INCREMENT,
  `full_name` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `neighbourhood` varchar(50) DEFAULT NULL,
  `insta_url` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`customer_id`),
  UNIQUE KEY `customers_customer_id_uindex` (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `items` (
  `item_id` int NOT NULL AUTO_INCREMENT,
  `owner_id` int NOT NULL,
  `name` varchar(100) NOT NULL,
  `category` varchar(100) NOT NULL,
  `condition_status` varchar(100) DEFAULT NULL,
  `description` varchar(400) DEFAULT NULL,
  `png_url` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`item_id`),
  UNIQUE KEY `items_item_id_uindex` (`item_id`),
  KEY `items_customers_customer_id_fk` (`owner_id`),
  CONSTRAINT `items_customers_customer_id_fk` FOREIGN KEY (`owner_id`) REFERENCES `customers` (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
