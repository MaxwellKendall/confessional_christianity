# GET Requests

1. getConfession
2. getChapter
3. getParagraphs
4. getCitations

# Foreign Keys
* confessionId = (WCF | WSC | WLC | BLG | HC | CD | 39A)
* headingId = confessionId + heading_number (WCF_1)
* contentId = confession_id_heading_number_content_number (WCF_1_2)
* citationId = contentId_citation_reference (WCF_1_2_A)

# Tables
1. CONFESSIONS: (Name of Confession w/ ancillary info)
	* id (primaryKey) = confessionId
	* Date = date of publication
	* Summary = historical info

2. HEADINGS: (Questions, Titles)
	* id (primaryKey) = headingId
	* confessionId (foreignKey1) = confessionId
	* title = string 
	
3. CONTENT: (Answers, Paragraphs)
	* id (primaryKey) = contentId
	* headingId (foreignKey1) = headingId
	* confessionId (foreignKey2) = confessionId
	* detail = string

4. CITATIONS: (Biblical References)
	* id (primaryKey) = citationId
	* contentId (foreignKey1) = contentId
	* headingId (foreignKey2) = headingId
	* confessionId (foreignKey3) = confessionId
	* referenceIdentifier = string (e.g. (a), 1/2/3)
	* scripture = string
	* tags

# getConfession(confessionId)  confessionObj {
```sql
    select 
        h.title as HeadingTitle,
        c.detail as ContentDetail
        c.citations as Citations
        ct.scripture as Scripture
    FROM HEADINGS h, CONTENT c, CITATIONS ct
    WHERE h.confessionId = c.confessionId AND c.confessionId = ct.confessionId;
```
}

# getHeading(headingId) chapterObj {
```sql
	select
		h.title as HeadingTitle,
		c.detail as ContentDetail
		ct.referenceIdentifier as CitationReference
		ct.scripture as ContentScriptureProofs
	FROM HEADINGS h, CONTENT c, CITATIONS ct 
		where h.id = c.headingId and h.headingId = ct.headingId
```
}

# getParagraph(contentId) {
```sql
	select
		c.detail as ContentDetail
		ct.referenceIdentifer as ContentCitations
		ct.scripture as ContentScriptureProofs
	FROM HEADINGS h, CONTENT c, CITATIONS ct 
		c.id = ct.contentId
```
}

# getCitations(tag/confessionId/contentId/headingId) {
```sql
	select * from CITATIONS where tag in (tag);
	OR
	select * from CITATIONS where confessionId = confessionId;
	OR
	select * from CITATIONS where headingId = headingId;
	OR
	select * from CITATIONS where contentId = contentId;
```
}