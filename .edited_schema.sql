-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- Clean start: remove any existing version of the schema
DROP SCHEMA IF EXISTS `research_paper_collaboration_network` ;

-- Create the research_paper_collaboration_network database and switch to it 

CREATE SCHEMA IF NOT EXISTS `research_paper_collaboration_network` DEFAULT CHARACTER SET utf8mb3 ;
USE `research_paper_collaboration_network` ;

-- Table: authors
-- Holds basic author info (first and last names)
CREATE TABLE IF NOT EXISTS `research_paper_collaboration_network`.`authors` (
  `author_id` INT NOT NULL AUTO_INCREMENT,
  `author_first_name` VARCHAR(45) NOT NULL,
  `author_last_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`author_id`),
  UNIQUE INDEX `idAuthor_UNIQUE` (`author_id` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb3;


-- Table: papers
-- Stores paper titles; each paper gets a unique ID

CREATE TABLE IF NOT EXISTS `research_paper_collaboration_network`.`papers` (
  `paper_id` INT NOT NULL AUTO_INCREMENT,
  `paper_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`paper_id`),
  UNIQUE INDEX `idPaper_UNIQUE` (`paper_id` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb3;

-- Table: paper_author_xref
-- Links authors and papers (many-to-many relationship)

CREATE TABLE IF NOT EXISTS `research_paper_collaboration_network`.`paper_author_xref` (
  `paper_author_xref_id` INT NOT NULL AUTO_INCREMENT,
  `paper_author_xref_papers_id` INT NOT NULL,
  `paper_author_xref_authors_id` INT NOT NULL,
  `contribution_percent` DECIMAL(5,2) DEFAULT NULL, -- need to update
  PRIMARY KEY (`paper_author_xref_id`),
  UNIQUE INDEX `idPaperAuthorXref_UNIQUE` (`paper_author_xref_id` ASC) VISIBLE,
  INDEX `PapersAuthorsXref_AuthorsID_idx` (`paper_author_xref_authors_id` ASC) VISIBLE,
  INDEX `PapersAuthorsXref_PapersID_idx` (`paper_author_xref_papers_id` ASC) VISIBLE,
  CONSTRAINT `papers_authors_xref_authors_id`
    FOREIGN KEY (`paper_author_xref_authors_id`)
    REFERENCES `research_paper_collaboration_network`.`authors` (`author_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `papers_authors_xref_papers_id`
    FOREIGN KEY (`paper_author_xref_papers_id`)
    REFERENCES `research_paper_collaboration_network`.`papers` (`paper_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb3;

-- Table: paper_citations
-- Keeps track of which paper cites which

CREATE TABLE IF NOT EXISTS `research_paper_collaboration_network`.`paper_citations` (
  `paper_citations_id` INT NOT NULL AUTO_INCREMENT,
  `citing_paper_id` INT NOT NULL,
  `cited_paper_id` INT NOT NULL,
  PRIMARY KEY (`paper_citations_id`),
  INDEX `citing_paper_id_idx` (`citing_paper_id` ASC) VISIBLE,
  INDEX `citied_paper_id_idx` (`cited_paper_id` ASC) VISIBLE,
  CONSTRAINT `citing_paper_id`
    FOREIGN KEY (`citing_paper_id`)
    REFERENCES `research_paper_collaboration_network`.`papers` (`paper_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `citied_paper_id`
    FOREIGN KEY (`cited_paper_id`)
    REFERENCES `research_paper_collaboration_network`.`papers` (`paper_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;

USE `research_paper_collaboration_network` ;


-- Placeholder table for view 
CREATE TABLE IF NOT EXISTS `research_paper_collaboration_network`.`ViewPapers` (`paper_id` INT, `paper_name` INT, `author_name` INT);


CREATE TABLE IF NOT EXISTS `research_paper_collaboration_network`.`ViewPaperNetwork` (`citing_paper` INT, `citing_authors` INT, `cited_paper` INT);


-- View: ViewPapers
-- Shows each paper with its author’s full name

DROP TABLE IF EXISTS `research_paper_collaboration_network`.`ViewPapers`;
USE `research_paper_collaboration_network`;
CREATE OR REPLACE VIEW ViewPapers AS
SELECT 
    p.paper_id,
    p.paper_name,
    CONCAT(a.author_first_name, ' ', a.author_last_name) AS author_name
FROM papers p
JOIN paper_author_xref xref ON p.paper_id = xref.paper_author_xref_papers_id
JOIN authors a ON a.author_id = xref.paper_author_xref_authors_id
ORDER BY p.paper_id;

-- View: ViewPaperNetwork
-- Shows which papers cite others and who wrote them

DROP TABLE IF EXISTS `research_paper_collaboration_network`.`ViewPaperNetwork`;
USE `research_paper_collaboration_network`;
CREATE OR REPLACE VIEW ViewPaperNetwork AS
SELECT 
    p1.paper_name AS citing_paper,
    GROUP_CONCAT(DISTINCT CONCAT(a.author_first_name, ' ', a.author_last_name) SEPARATOR ', ') AS citing_authors,
    p2.paper_name AS cited_paper
FROM paper_citations pc
JOIN papers p1 ON pc.citing_paper_id = p1.paper_id
JOIN papers p2 ON pc.cited_paper_id = p2.paper_id
JOIN paper_author_xref x ON p1.paper_id = x.paper_author_xref_papers_id
JOIN authors a ON x.paper_author_xref_authors_id = a.author_id
GROUP BY p1.paper_name, p2.paper_name
ORDER BY p1.paper_name;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
