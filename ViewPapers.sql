CREATE OR REPLACE VIEW ViewPapers AS
SELECT 
    p.paper_id,
    p.paper_name,
    CONCAT(a.author_first_name, ' ', a.author_last_name) AS author_name
FROM papers p
JOIN paper_author_xref xref ON p.paper_id = xref.paper_author_xref_papers_id
JOIN authors a ON a.author_id = xref.paper_author_xref_authors_id
ORDER BY p.paper_id;