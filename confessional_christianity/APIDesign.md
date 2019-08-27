# Data Layer
Details a pattern for the shape of the database.

## Foreign Keys
* confessionId = (WCF | WSC | WLC | BLG | HC | CD | 39A = Westminster Confession of Faith, Westminster Shorter Catechism, Westminster Larger Catechism, Belgic Confession, Heidelberg Catechism, Cannons of Dordt, 39 Articles) 
* headingId = confessionId + heading_number (WCF_1 = westminster confession chapter 1)
* contentId = confession_id_heading_number_content_number (WCF_1_2 = westminster confession chapter 1 paragraph 2)
* citationId = contentId_referenceIdentifier (WCF_1_2_A = westminster confession chapter 1 paragraph 2 citation a)

## Tables
1. CONFESSIONS: (Name of Confession w/ ancillary info)
	* id (primaryKey) = confessionId
	* Date = date of publication
	* Summary = historical info

2. HEADING: (Questions for Catechisms OR Titles for Articles in Confession)
	* id (primaryKey) = headingId
	* confessionId (foreignKey1) = confessionId
	* title = string 
	
3. CONFESSION: (Answers, Paragraphs)
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
	* scripture = arrayOf(string)
	* tags

Materialized Views for each confession? Organizing it this way for future data analysis.

## Services
Details the service modules which implement the API

1. Confessions: builds the Confessions, Confession, and Heading Model
2. Citations: builds the Citations model

### Future Services?
3. 
## API
Details the requests to be made.

# GET Requests
1. getConfession: api/confessionId
2. getChapter: api/confessionId/chapterId
3. getParagraph: api/confessionId/chapterId/paragraphId
4. getCitations: api/citations/citationId

# getConfession(confessionId)  confessionObj {
```sql
    select 
        h.title as HeadingTitle,
        c.detail as ContentDetail
        ct.citations as Citations -- ie. citation (g)
        ct.scripture as Scripture -- ie. Matthew 5: 10
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