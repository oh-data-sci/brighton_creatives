import logging
import json

import coolname
import pandas as pd
from pathlib import Path
from duckdb.duckdb import DuckDBPyConnection

logger = logging.getLogger(__name__)


def load_from_template(
    db_connection: DuckDBPyConnection,
    source_filepath: str,
    template_filepath: str = None,
):
    """
    Loads CSV data from the source filepath according to a template that includes:
    * data subdirectory (defaults to .)
    * destination duckdb (defaults to creatives.duckdb)
    * destination table (mandatory)
    * number of header lines
    * source to target column mappings (e.g. WD25CD:ward_code)
      * if no mappings are present then the source columns headers are used
    """
    logger.debug(
        f"Loading {source_filepath} to {db_connection.description} using template {template_filepath}"
    )
    _validate_load(db_connection, source_filepath, template_filepath)
    # pull the extract + load directives out of the template
    template = _load_template(template_filepath)

    header_line = template.get("header_line", 0)
    logger.debug(f"Col headings on line {header_line}")

    skip_rows = template.get("skip_rows", 0)
    logger.debug(f"Will skip {skip_rows} lines")

    encoding = template.get("encoding", "utf-8")
    logger.debug(f"File encoding is {encoding}")

    column_mappings = template.get("column_mappings", {})
    logger.debug(f"Will rename columns as per {column_mappings}")

    column_type_overrides = template.get("column_type_overrides", {})
    logger.debug(f"Will override VARCHAR types as per {column_type_overrides}")

    target_table = template.get(
        "target_table", coolname.generate_slug(2).replace("-", "_")
    )
    logger.debug(f"Loading into table {target_table}")

    # read the source data as csv
    df = pd.read_csv(
        source_filepath, header=header_line, encoding=encoding, skiprows=skip_rows
    )

    _load_df_to_duck(
        db_connection, df, target_table, column_mappings, column_type_overrides
    )

    return target_table


def _validate_load(
    db_connection: DuckDBPyConnection,
    source_filename: str,
    template_filepath: str = None,
):
    if not db_connection:
        raise ValueError("You need to pass a valid DuckDB connection")

    if not source_filename:
        raise ValueError("You need to supply a source filename, e.g. foo.csv")

    if not Path(source_filename).exists():
        raise FileNotFoundError(f"File not found: {source_filename}")

    if template_filepath and not Path(template_filepath).exists():
        raise FileNotFoundError(f"File not found: {template_filepath}")


def _load_template(json_path: str) -> dict:
    logger.debug(f"Loading from template file {json_path}")
    if not json_path:
        return {}
    path = Path(json_path)
    with path.open("r", encoding="utf-8") as f:
        template = json.load(f)
    return template


def _load_df_to_duck(conn, df, target_table, column_mappings, column_type_overrides):
    default_type = "VARCHAR"
    logger.debug(f"df columns {df.columns}")
    source_col_names = (
        [col for col in column_mappings if col in df.columns]
        if column_mappings
        else df.columns
    )

    logger.debug(f"Source columns: {source_col_names}")
    df_clean = df[source_col_names].rename(columns=column_mappings)

    # create the DDL ... note type defaults to VARCHAR unless overridden in template
    col_defs = [
        f"{col} {column_type_overrides.get(col, default_type)}"
        for col in df_clean.columns
    ]
    logger.debug(f"Column defs are: {col_defs}")

    # create target table in duck
    create_table_sql = f"""
    CREATE TABLE IF NOT EXISTS {target_table} (
        {", ".join(col_defs)}
    )
    """
    conn.execute(create_table_sql)

    # register temp table with the cleaned df
    conn.register("temp_table", df_clean)
    # insert from temp table into target table
    conn.execute(f"INSERT INTO {target_table} SELECT * FROM temp_table")
    # clean up
    conn.unregister("temp_table")
