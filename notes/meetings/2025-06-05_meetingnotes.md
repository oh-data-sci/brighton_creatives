2025-06-05 project hackastroll
====
# introduction
meeting notes of the brighton creatives project kickoff meeting

## in attendance
- oskar holm
- andrew jeavons
- fiona macneill

# agenda

- who likes doing what? who'd like to learn to do what?
- who needs support with what?
    + is everyone set up?
    + python,
    + github,
    + R,
    + SQL
- how do we hone in on an actual question.


# task list
- **research**: find more data sources, filter data found.
- **code**: collect, scrape, gather, request more data files.
- **code**: clean/format/pivot/unpivot/serialise into tabular data formats.
- **data engineering**: data modelling and ingestion, ddl, joins, enrichments, etc.
- **analytics**: exploratory data analysis and insight discovery: *discover the question*.
- **science**: statistical modelling, machine learning, forecasting, etc. 


# person and task
- keith  -> scraper. pass the source urls to him!
- fiona  -> describe what's needed and keep focus, and trim the fat.
- andrew -> ? quantify unstructured data? access intelligent agents or notebook lm?
- others unknown.

# more sources:
- academic papers
    + qualitative information -> can be turned quantitative, needs guidance from fiona. 
    + scrape references from papers, and look them up?
        + ai-agent/llms/notebook lm + list of references --> link to original
- hard data from arts council map: 
    + https://www.artscouncil.org.uk/your-area/culture-and-place-data-explorer
    + https://www.artscouncil.org.uk/sites/default/files/2024-09/Culture%20and%20Place%20Data%20Explorer%20-%20Quick%20Start%20Guide%20%20ACE%20%281%29.pdf, https://www.artscouncil.org.uk/our-organisation/expenditure-data, https://www.artscouncil.org.uk/research-and-data/our-data, https://culture.localinsight.org/#/map
    + fiona shared a report from the oxford consultancy group and art council england.
    + fiona shared a powerbi dashboard

# data cleaning and processing
ons data with odd shaped header, hard to bring into 
 oskar showed how to read and analyse ons csv files (python notebook). more file types need cleaning code. especially excel. and loaded duckdb database loaded.

need to focus the search for information. look for one of these:

1. how much is being spent in public grants?
2. where is this money going to? what else can we know about the areas where the grants are going? median income, demographics, etc.
3. we have found over 400 empty spaces in brighton. how many of these are artistic places

# need to do: 
- 
