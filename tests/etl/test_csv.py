import logging

import pytest
from pathlib import Path

from etl.csv import load_from_template

logger = logging.getLogger(__name__)


def test_load_from_template_requires_source(testdb_connection):
    """
    Should raise a ValueError if no source filename supplied
    Should raise a FileNotFoundError if no such source file
    """
    with pytest.raises(
        ValueError, match="You need to supply a source filename, e.g. foo.csv"
    ):
        load_from_template(testdb_connection, "", None)

    assert not Path("foo.csv").exists()
    with pytest.raises(FileNotFoundError, match="File not found: foo.csv"):
        load_from_template(testdb_connection, "foo.csv", None)


def test_load_from_template_no_such_template(testdb_connection):
    """
    Should raise a FileNotFoundError if a non-existent template is supplied
    """
    sample_ward_to_lad = "./tests/fixtures/sample-ward-to-lad.csv"
    assert Path(sample_ward_to_lad).exists()
    assert not Path("foo.json").exists()
    with pytest.raises(FileNotFoundError, match="File not found: foo.json"):
        load_from_template(testdb_connection, sample_ward_to_lad, "foo.json")


def test_load_from_template_valid_defaulted_template(testdb_connection):
    """
    Should load the data into a random table name with existing cols if no template
    """
    sample_ward_to_lad = "./tests/fixtures/sample-ward-to-lad.csv"
    table_name = load_from_template(testdb_connection, sample_ward_to_lad, None)
    assert table_name is not None

    # E05013038,Burn Valley,,E06000001,Hartlepool,,1
    result = testdb_connection.execute(
        f"""
        SELECT WD25CD, WD25NM, WD25NMW, LAD25CD, LAD25NM, LAD25NMW, ObjectId
        FROM {table_name}
        WHERE WD25CD = 'E05013038'
        """
    )
    ward_data = result.fetchone()
    # E05013038,Burn Valley,,"E06000001",Hartlepool,,1
    assert ward_data[0] == "E05013038"
    assert ward_data[1] == "Burn Valley"
    assert ward_data[2] is None
    assert ward_data[3] == "E06000001"
    assert ward_data[4] == "Hartlepool"
    assert ward_data[5] is None
    assert ward_data[6] == "1"


def test_load_from_template_valid_template(testdb_connection):
    """
    Should load the data as per the template directives
    """
    sample_ward_to_lad = "./tests/fixtures/sample-ward-to-lad.csv"
    ward_to_lad_template = "./tests/fixtures/test-ward-to-lad-template.json"
    expected_table_name = "ward_to_lad"

    table_name = load_from_template(
        testdb_connection, sample_ward_to_lad, ward_to_lad_template
    )
    assert table_name == expected_table_name

    # E05013038,Burn Valley,,E06000001,Hartlepool,,1
    result = testdb_connection.execute(
        f"""
        SELECT ward_code, ward_name, welsh_ward_name, local_authority_code, local_authority_name, welsh_local_authority_name, ons_internal_id
        FROM {table_name}
        WHERE ward_code = 'E05013038'
        """
    )
    ward_data = result.fetchone()
    # E05013038,Burn Valley,,"E06000001",Hartlepool,,1
    assert ward_data[0] == "E05013038"
    assert ward_data[1] == "Burn Valley"
    assert ward_data[2] is None
    assert ward_data[3] == "E06000001"
    assert ward_data[4] == "Hartlepool"
    assert ward_data[5] is None
    assert ward_data[6] == 1
    assert type(ward_data[6]) == int
