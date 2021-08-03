

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `ordersystem_db` DEFAULT CHARACTER SET utf8 ;
USE `ordersystem_db` ;

-- -----------------------------------------------------
-- Table `ordersystem_db`.`group`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ordersystem_db`.`upper_cat` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `uppercat_name` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `ordersystem_db`.`sub_cat` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `subcat_name` VARCHAR(45) NULL DEFAULT NULL,
  `upper_cat` INT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `subcat_uppercat`
   FOREIGN KEY (`upper_cat`)
        REFERENCES ordersystem_db.upper_cat(id)
        ON DELETE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `ordersystem_db`.`product` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `product_name` VARCHAR(45) NULL DEFAULT NULL,
  `product_price` FLOAT NULL DEFAULT NULL,
  `product_desc` VARCHAR(45) NULL DEFAULT NULL,
  `menu` INT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `prduct_menu`
   FOREIGN KEY (`menu`)
        REFERENCES ordersystem_db.menu(id)
        ON DELETE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `ordersystem_db`.`order` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `order_quantity` VARCHAR(45) NULL DEFAULT NULL,
  `order_wish` VARCHAR(45) NULL DEFAULT NULL,
  `product` INT NOT NULL,
  `table_` INT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `order_product`
   FOREIGN KEY (`product`)
        REFERENCES ordersystem_db.product(id)
        ON DELETE CASCADE,
        CONSTRAINT `order_table_`
   FOREIGN KEY (`table_`)
        REFERENCES ordersystem_db.table_(id)
        ON DELETE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `ordersystem_db`.`table_` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `table_status` INT NULL DEFAULT NULL,
  `paymentmethod` VARCHAR(45) NULL DEFAULT NULL,
  `netto_amount` FLOAT NULL DEFAULT NULL,
  `brutto_amount` FLOAT NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

