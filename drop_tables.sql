

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

-- Drop table paper_author_xref if exists
DROP TABLE IF EXISTS `citation_xref`;

SET FOREIGN_KEY_CHECKS = 1;