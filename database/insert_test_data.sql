/* ******************************************************
Insert test data into the employee_training database.
********************************************************/

-- Switch to the employee_training database.
USE `research_paper_network`;

-- Insert data into the employees table.
INSERT INTO `authors` (first_name, middle_name, last_name)
VALUES 
('Alice', 'Marie', 'Nguyen'),
('Brian', NULL , 'Lee'),
('Carla', 'Jane', 'Smith'),
('David', 'Rahul', 'Patel'),
('Ella', 'Sofia', 'Rodriguez');

INSERT INTO papers (paper_title, publication_year, category)
VALUES
('Machine Learning for Climate Models', 2024, 'Artificial Intelligence'),
('Neural Graph Architectures', 2023, 'Deep Learning'),
('Quantum Encryption Protocols', 2025, 'Cybersecurity'),
('Blockchain for Healthcare', 2024, 'Data Systems'),
('Ethical AI Governance', 2025, 'AI Ethics');

-- Insert data into paper_author_xref table.
-- Each row links a paper to an author and their contribution percentage.

INSERT INTO `paper_author_xref` (paper_id, author_id, contribution)
VALUES
-- Paper 1: Machine Learning for Climate Models
(1, 1, 60.00),  -- Alice Nguyen
(1, 2, 40.00),  -- Brian Lee

-- Paper 2: Neural Graph Architectures
(2, 2, 50.00),  -- Brian Lee
(2, 3, 50.00),  -- Carla Smith

-- Paper 3: Quantum Encryption Protocols
(3, 3, 70.00),  -- Carla Smith
(3, 4, 30.00),  -- David Patel

-- Paper 4: Blockchain for Healthcare
(4, 4, 55.00),  -- David Patel
(4, 1, 45.00),  -- Alice Nguyen

-- Paper 5: Ethical AI Governance
(5, 5, 100.00); -- Ella Rodriguez


INSERT INTO citation_xref (citing_id, cited_id)
VALUES
(2, 1),  -- Neural Graph Architectures cites Machine Learning for Climate Models
(3, 2),  -- Quantum Encryption Protocols cites Neural Graph Architectures
(4, 1),  -- Blockchain for Healthcare cites Machine Learning for Climate Models
(4, 3),  -- Blockchain for Healthcare cites Quantum Encryption Protocols
(5, 2),  -- Ethical AI Governance cites Neural Graph Architectures
(5, 4);  -- Ethical AI Governance cites Blockchain for Healthcare


