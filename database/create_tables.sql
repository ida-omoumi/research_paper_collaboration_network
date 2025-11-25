/* *************************************************************
Drop and Create the tables for the research_paper_network.
*************************************************************** */

USE `research_paper_network`;
-- Switching to research_paper_network

-- Table: authors
-- Stores author names ; each author gets a unique ID
SET FOREIGN_KEY_CHECKS = 0;

-- Drop table authors if exists 
DROP TABLE IF EXISTS `authors`;

-- Drop table papers if exists 
DROP TABLE IF EXISTS `papers`;

-- Drop table paper_author_xref if exists
DROP TABLE IF EXISTS `paper_author_xref`;

SET FOREIGN_KEY_CHECKS = 1;


CREATE TABLE IF NOT EXISTS `authors` (
  `id` int(11) NOT NULL,
  `first_name` varchar(25) NOT NULL,
  `middle_name` varchar(25),
  `last_name` varchar(25) NOT NULL
);

-- Designate the `id` column as the primary key
ALTER TABLE `authors`
  ADD PRIMARY KEY (`id`);

-- Make `id` column auto increment on inserts
ALTER TABLE `authors`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

-- -------------------------------------------------------
-- Table: papers
-- Stores paper titles ; each paper gets a unique ID
-- -------------------------------------------------------


CREATE TABLE IF NOT EXISTS `papers` (
  `id` int(11) NOT NULL,
  `paper_title` varchar(250) NOT NULL, 
  `publication_year` YEAR DEFAULT NULL, 
  `category` VARCHAR(100) DEFAULT NULL
);

-- Designate the `id` column as the primary key
ALTER TABLE `papers`
  ADD PRIMARY KEY (`id`);

-- Make `id` column auto increment on inserts
ALTER TABLE `papers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

-- -------------------------------------------------------
-- Table: paper_author_xref
-- Links authors to papers (many-to-many relationship)
-- -------------------------------------------------------


-- Create paper_author_xref table
CREATE TABLE `paper_author_xref` (
  `author_id` int(11) NOT NULL,
  `paper_id` int(11) NOT NULL,
  `contribution` DECIMAL(5,2) NOT NULL
);

-- Create indexes on paper_id and author_id columns
ALTER TABLE `paper_author_xref`
  ADD KEY `paper_author_ibfk_1` (`author_id`),
  ADD KEY `paper_author_ibfk_2` (`paper_id`);

-- Add Cascade Delete Constraint on paper_id column
ALTER TABLE `paper_author_xref`
  ADD CONSTRAINT `paper_author_ibfk_1`
  FOREIGN KEY (`author_id`) REFERENCES `authors` (`id`)
  ON DELETE CASCADE
  ON UPDATE CASCADE;

-- Add Cascade Delete Constraint on author_id column
ALTER TABLE `paper_author_xref`
  ADD CONSTRAINT `paper_author_ibfk_2`
  FOREIGN KEY (`paper_id`) REFERENCES `papers` (`id`)
  ON DELETE CASCADE
  ON UPDATE CASCADE;
  
  
  -- -------------------------------------------------------
-- Table: citation_xref
-- Links papers to papers (self-referential many-to-many relationship)
-- -------------------------------------------------------

-- Drop table citation_xref if exists
DROP TABLE IF EXISTS `citation_xref`;

-- Create citation_xref table
CREATE TABLE `citation_xref` (
  `citing_id` int(11) NOT NULL,
  `cited_id` int(11) NOT NULL
);

-- Create indexes on citing_id and cited_id columns
ALTER TABLE `citation_xref`
  ADD KEY `citation_ibfk_1` (`citing_id`),
  ADD KEY `citation_ibfk_2` (`cited_id`);

-- Add Cascade Delete Constraint on citing_id column
ALTER TABLE `citation_xref`
  ADD CONSTRAINT `citation_ibfk_1`
  FOREIGN KEY (`citing_id`) REFERENCES `papers` (`id`)
  ON DELETE CASCADE
  ON UPDATE CASCADE;

-- Add Cascade Delete Constraint on cited_id column
ALTER TABLE `citation_xref`
  ADD CONSTRAINT `citation_ibfk_2`
  FOREIGN KEY (`cited_id`) REFERENCES `papers` (`id`)
  ON DELETE CASCADE
  ON UPDATE CASCADE;
-- To prevent duplicates
  ALTER TABLE `citation_xref`
  ADD PRIMARY KEY (`citing_id`, `cited_id`);

  
  
  