-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema research_paper_collaboration_network
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `research_paper_collaboration_network` ;

-- -----------------------------------------------------
-- Schema research_paper_collaboration_network
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `research_paper_collaboration_network` DEFAULT CHARACTER SET utf8 ;
USE `research_paper_collaboration_network` ;

-- -----------------------------------------------------
-- Table `research_paper_collaboration_network`.`Papers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `research_paper_collaboration_network`.`Papers` (
  `idPaper` INT NOT NULL AUTO_INCREMENT,
  `PaperName` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idPaper`),
  UNIQUE INDEX `idPaper_UNIQUE` (`idPaper` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `research_paper_collaboration_network`.`Authors`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `research_paper_collaboration_network`.`Authors` (
  `idAuthor` INT NOT NULL AUTO_INCREMENT,
  `AuthorName` VARCHAR(45) NULL,
  PRIMARY KEY (`idAuthor`),
  UNIQUE INDEX `idAuthor_UNIQUE` (`idAuthor` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `research_paper_collaboration_network`.`PaperAuthorXref`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `research_paper_collaboration_network`.`PaperAuthorXref` (
  `idPaperAuthorXref` INT NOT NULL AUTO_INCREMENT,
  `PaperAuthorXref_PapersID` INT NOT NULL,
  `PaperAuthorXref_AuthorsID` INT NOT NULL,
  PRIMARY KEY (`idPaperAuthorXref`),
  UNIQUE INDEX `idPaperAuthorXref_UNIQUE` (`idPaperAuthorXref` ASC) VISIBLE,
  INDEX `PapersAuthorsXref_AuthorsID_idx` (`PaperAuthorXref_AuthorsID` ASC) VISIBLE,
  INDEX `PapersAuthorsXref_PapersID_idx` (`PaperAuthorXref_PapersID` ASC) VISIBLE,
  CONSTRAINT `PapersAuthorsXref_PapersID`
    FOREIGN KEY (`PaperAuthorXref_PapersID`)
    REFERENCES `research_paper_collaboration_network`.`Papers` (`idPaper`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `PapersAuthorsXref_AuthorsID`
    FOREIGN KEY (`PaperAuthorXref_AuthorsID`)
    REFERENCES `research_paper_collaboration_network`.`Authors` (`idAuthor`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

