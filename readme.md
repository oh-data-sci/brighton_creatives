brighton creatives
===
# introduction
the covid pandemic, with its lockdowns and closures of public spaces had a complex effect on society. artists and others operating in the --already fickle-- creative industries we heavily impacted but the picture is complicated. by various metrics, the creative industries bounced back rapidly, but the post covid world still bears the marks of the interruption.

here we are focusing on the impact on the creative industries in brighton. our plan to investigate this is to collect available data from official sources

# project structure
```
├── data
│   ├── creatives.duckdb  --> central database for processed data
│   ├── csv               --> raw data files in csv format
│   │   ├── ons           --> raw csv by-region data files from the ons
│   │   └── time_series   --> raw csv time series from the ons 
│   ├── excel             --> raw excel formatted data reports from official sources
│   └── source_urls       --> lists of urls from where data is sourced
├── img                   --> graphical resources, including plots genrated or downloaded from sources
├── notebooks             --> processing, exploratory, and modelling code notebooks
├── notes                 --> various text or pdf documents containing relevant information 
├── readme.md             --> this file
├── sql                   --> transformations, joins and analytics on database tables
└── src                   --> (mostly python) source code for scraping/ingestion/processing/modelling
```

# Research questions 

## Are creative people leaving Brighton? 

Prompted by this article from the Brighton Chamber 
- [discussion at brighton chamber](https://www.brightonchamber.co.uk/blog/the-big-debate-is-brightons-creative-sector-an-undervalued-powerhouse)

- **Q1: What are the greatest barriers for creative people working in Brighton?**
    - Affordable spaces to make/do (e.g., the closure of New England House).
    - Spaces to show/sell
    - Supportive infrastructure (e.g., arts organisations, local funding)
    - Routes to audiences (e.g., tourism board, what's on guides, social media, ticketing sites)
    - Supplementary job opportunities, e.g., both universities have been hit with redundancies, how have creative subjects been impacted? Is there even information available?
    - Are there any factors which may have impacted creative incomes in Brighton?
        - e.g., has AI impacted photographers and visual designers? 

- **Q2: What are the greatest barriers for creative people living in Brighton?**
    - Cost of living versus average income.
        - Related to this, I am interested in finding out if there is a general trend of people leaving Brighton, beyond the usual changes to the student population.
    - Relative costs of rents in Brighton as compared to income
    - Issues with housing stock in more affordable areas. Related to this - just some ideas...
        - Crime in these areas
        - Quality of schools in these areas
        - Quality of doctors surgeries
        - Access to an NHS dentist


# specific notes 

## department for culture, media, and sport
[2016 report](https://assets.publishing.service.gov.uk/media/5a802de7e5274a2e87db850b/DCMS_Statistical_Handbook_-_28_September_2016.pdf)
[source: 1](https://www.thecreativeindustries.co.uk/facts-figures/creative-industries-add-ps124bn-of-value-to-uk), [and 2](https://www.gov.uk/government/statistics/dcms-and-digital-sector-gva-2022-provisional/dcms-sectors-economic-estimates-gross-value-added-2022-provisional)
> The economic contribution of the UK creative industries grew by 6.8 per cent in 2022 to reach £124.6bn, according to official UK government estimates.
> 
> In real terms, this means the economic value of the UK creative industries was 12 per cent bigger in 2022 than before the COVID pandemic and more than 50 per cent larger than its size in 2010.
> 
> Using the government's official economic measure of Gross Value Added (GVA) in chained volume measures, the creative industries grew more than twice as fast in 2022 as the UK economy as a whole. Since 2010, the creative industries have expanded according to this measure by 50.3 per cent, compared to the UK economy's average increase of 21.5 per cent during the same period. Creative industries account for 5.7 per cent of total UK GVA.
> 
> ‘IT, software and computer services’ comprises the largest subsector component of the creative industries by GVA (£53.4bn in 2022). It is more than twice the size of the next largest subsector, ‘Film, TV, video, radio and photography’ which contributed £20.8bn in 2022.
> 
> The largest contributions to the increase in creative Industries GVA from 2021 to 2022 were the ‘IT, software and computer services’ subsector, the ‘Publishing’ subsector and the ‘Film, TV, video, radio and photography’ subsector, which grew by 7.3 per cent, 10.1 per cent and 5.4 per cent respectively. All segments of the creative industries grew their GVA from 2021 to 2022, apart from the crafts subsector, which fell by 6.8 per cent.

## non-economic impact of the arts
- [example impact on baby names] (https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/livebirths/articles/fromstarwarstothekardashianstheculturalinfluencesthatcouldbedrivingbabynametrends/2022-10-05)


# sources

- [discussion at brighton chamber](https://www.brightonchamber.co.uk/blog/the-big-debate-is-brightons-creative-sector-an-undervalued-powerhouse)
- [ons: methodology](https://oflog.data.gov.uk/methodology?area=BN1+1ND)
- [ons: advice](https://blog.ons.gov.uk/2024/03/26/local-data-at-your-fingertips/)
- [arts](https://lginform.local.gov.uk/dataAndReports/search/3676?text=arts)
- [local gov](https://lginform.local.gov.uk) (*The Office for Local Government has now closed. This Data Explorer is being maintained and updated by the Ministry of Housing, Communities and Local Government (MHCLG).*)
- [brighton data from oflog](https://oflog.data.gov.uk/planning?area=BN1+1ND)
- [funding](https://reports.esd.org.uk/share/map)
- [expenditure](https://lginform.local.gov.uk/dataAndReports/explorer/6605?text=arts&metricType=6605&area=E10000008%2CAllLaInUK&period=latest)


# links for safe keeping 
**From Adam** 
- [mapping from UPRN  (Unique Property Reference Numbers) to geocoordinates](https://www.ordnancesurvey.co.uk/products/os-open-uprn)
- [Planning in Brighton and Hove](https://oflog.data.gov.uk/planning?area=BN1+1ND)
- [Total expenditure on arts, tourism and historic environment](https://lginform.local.gov.uk/dataAndReports/explorer/6605?text=arts&metricType=6605&area=E10000008%2CAllLaInUK&period=latest)
- [LG Inform](https://lginform.local.gov.uk/dataAndReports/explorer) - data here about number of art gallery visits.

**From Fiona**
- [Libraries and makerspaces 2019](https://www.gov.uk/government/publications/libraries-and-makerspaces/libraries-and-makerspaces) - a lot of these places might be closed now. Alas nothing on Brighton, but some useful links.
- [A nesta report on makerspaces from 2015](https://www.nesta.org.uk/report/open-dataset-of-uk-makerspaces-a-users-guide/) unfortunately the dataset, no longer seems to be available.
- [Culture in our city map for Brighton](https://cultureinourcity.com/creative-network/venues-spaces/) - this feels like a work in-progress, not many spaces on here and I know there are more.
- [Resources page with some useful links to reports](https://cultureinourcity.com/creative-network/resources/) 
- [A relevant paper from University of Sussex - Cultural, creative and collective recovery: exploring a creative Worker income Guarantee (CWIG)](https://www.tandfonline.com/doi/full/10.1080/17510694.2023.2301120#abstract)
- [Report: Space to Grow - Brighton & Hove: Space for Culture](https://cultureinourcity.com/resources/space-to-grow-brighton-hove-space-for-culture/)
- [*Meanwhile* space this seemed like a good project](https://www.meanwhilespace.com/about) - still active on companies house, but the website is a bit out of date.
- Some useful links from the 'Creative Lives' website:
- [Barriers to Banking](https://www.creative-lives.org/barriers-to-banking) - alas no data yet
- [Report: Spaces for Creative 2024](https://www.creative-lives.org/spaces-for-creativity-2024) - limited data but backs up some of the themes. [Direct link to the PDF](https://www.creative-lives.org/Handlers/Download.ashx?IDMF=0b2f24b3-f2b2-4a5e-b9b6-92c6b4fccdab).
- [Report: Everyday Creativity 2016](https://www.creative-lives.org/everyday-creativity) - a report from 2016 which includes direct feedback from artists.
- [Arts Council response to the report 2020](https://www.artscouncil.org.uk/blog/value-everyday-creativity) 
- [List of Brighton art galleries](https://www.brighton-hove.gov.uk/libraries-leisure-and-arts/arts-and-culture/art-galleries) - however, a few of these are closed. This page hasn't changed much since 2020.
- [Creative Industries Council](https://www.thecreativeindustries.co.uk/)
- [Unleashing Creativity: Fixing the finance gap in the creative industres, Hasan Bakhshi, Josh Siepel, Lara Carmona, Amy Tarr](https://unleash.wearecreative.uk/)
- [Creative industries add almost £25bn to UK trade balance](https://www.thecreativeindustries.co.uk/facts-figures/creative-industries-add-almost-ps25bn-to-uk-trade-balance) - [data source from gov.uk](https://www.gov.uk/government/statistics/dcms-and-digital-sector-economic-estimates-trade-2021/dcms-sectors-economic-estimates-trade-2021-main-report#trade-in-services-1)
- [Don't let complacency jeopardise the creative industries](https://committees.parliament.uk/committee/170/communications-and-digital-committee/news/175423/dont-let-complacency-jeopardise-the-creative-industries/)
- [CITIB International Strategy (2022-2025)](https://www.thecreativeindustries.co.uk/download-hub/citib-international-strategy-2022-2025) 

- [Culture and Place Data Explorer](https://www.artscouncil.org.uk/your-area/culture-and-place-data-explorer) - a brilliant interactive map for exploring multiple factors related to culture and creativity

# Python ETL

## Overview
This is a mini-EL (no transformations at the moment) pipeline that loads data from a basic CSV file into a DuckDB table 
based on a JSON template. A "basic" CSV file is one that has a header row

## Installation

* Requires Python 3.12 (if this is problematic shout and we can downgrade) and pip
* Dependencies and other stuff are defined in the `pyproject.toml`
* From the `brighton_creatives` directory:
  * `python -m venv venv`
  * `source venv/bin/activate` (`.\venv\Scripts\activate.bat` from Windows cmd)
  * `pip install -e .[dev]
    * Drop the `[dev]` if you don't need or want the dev dependencies from the `pyproject.toml` 
` 
## Quick Tour
* Code is in the `src` folder and within the `etl` package
* Tests are in `tests\etl` and use [Pytest](https://docs.pytest.org/en/stable/)
* The `csv.py` file contains a generic `load_from_template` that:

### The Extract and Load method
* Delivered for [Issue 5](https://github.com/oh-data-sci/brighton_creatives/issues/5)
* See `src/etl/csv.py#load_from_template`
  * Takes a `source_filepath` and optional JSON template
  * Loads or defaults the template from the file
* loads the data into a Pandas `DataFrame` based on the instructions in the template
* Stores the data in a DuckDB table as per the template
  * or it gives it an arbitrary name using [coolname](https://pypi.org/project/coolname/)

### More about the EL Template
* This is an example template used in the `tests` and can be found at `tests\fixtures\test-ward-to-lad-template.json`
```json
{
  "name": "ons-ward-to-la",
  "target_table": "ward_to_lad",
  "column_mappings": {
    "WD25CD": "ward_code",
    "WD25NM": "ward_name",
    "WD25NMW": "welsh_ward_name",
    "LAD25CD": "local_authority_code",
    "LAD25NM": "local_authority_name",
    "LAD25NMW": "welsh_local_authority_name",
    "ObjectId": "ons_internal_id"
  },
  "column_type_overrides": {
    "ons_internal_id": "TINYINT"
  }
} 
```
* The target table is the name of the resulting DuckDB table
* The column mappings optionally rename the CSV columns to other names
  * Use `column_mappings: {}` or just omit the key to keep the source names
  * Leave a column out if it's not needed in the target
* The column type overrides allow change of type from `VARCHAR` which is the default

### Running tests
* `pytest` is used for unit testing
* To make the unit testing as deep as possible an in-memory DuckDB is used
  * see its setup in `tests/conftest.py`
  * a test db connection is passed to each test that needs it
* After the installation steps above you can run the tests via `pytest` from the root dir (i.e. `brighton_creatives`)
  * Make sure you have installed into your `venv` with the `[dev]` option
  * This is because `pytest` and other dev dependencies are in the `dev` section in the `TOML`
* There's plenty (probably too much 😂) of logger debug statements that show what's going on under the hood
* To alter the log output level change it in `tests/conftest.py`, e.g. logging.basicConfig(level=logging.DEBUG)
* Then do `pytest -s` to output logs