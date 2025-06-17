import duckdb
import logging
import pytest


def pytest_configure():
    # change me to alter the logging level across tests
    logging.basicConfig(level=logging.DEBUG)


class TestDBConnection:
    """
    Create this wrapper class solely to add a handy description for logging / debug
    """

    def __init__(self, conn):
        self.conn = conn
        self.description = "Test DuckDB (in-memory)"

    def __getattr__(self, item):
        return getattr(self.conn, item)


@pytest.fixture
def testdb_connection():
    """Use this fixture in tests to validate writing to the db"""
    raw_conn = duckdb.connect(database=":memory:")
    conn = TestDBConnection(raw_conn)
    yield conn
    raw_conn.close()
