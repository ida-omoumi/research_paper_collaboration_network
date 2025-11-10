
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