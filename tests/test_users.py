"""Exercise 2: integration tests and fixtures with teardown."""

import pytest

from orderflow.users import Database, UserRepository


class TestUserRepositoryIntegration:
    """Integration tests for UserRepository against a real Database."""

    @pytest.fixture
    def database(self):
        """Provide a connected database, and close it again afterwards."""
        # TODO: Create a Database instance
        # TODO: Call connect() on the database
        # TODO: Use yield to hand the database to the test
        # TODO: After the yield, call disconnect() on the database

        database = Database()
        database.connect()
        yield database
        database.disconnect()

    @pytest.fixture
    def user_repo(self, database):
        """Provide a UserRepository backed by the connected database."""
        return UserRepository(database)
    
    def test_create_and_retrieve_user(self, user_repo):
        """Test creating and then reading back a user."""
        user = user_repo.create_user("123", "John Doe", "john@example.com")
        assert user['id'] == "123"
        assert user['name'] == "John Doe"
        assert user['email'] == "john@example.com"
        assert user['created_at'] != None

    def test_create_user_with_invalid_email(self, user_repo):
        with pytest.raises(ValueError, match="Invalid email"):
            user_repo.create_user("1", "andres", email="invalid-email")

    def test_get_nonexistent_user(self, user_repo):
        id = user_repo.get_user("999")
        assert id == None

    def test_database_not_connected_raises_error(self):
        """Test that operations fail when the database is not connected."""
        # TODO: Create a Database instance and do NOT connect it
        # TODO: Create a UserRepository with this database
        # TODO: Use pytest.raises(ConnectionError, match="not connected")
        # TODO: Try to create a user
        assert False, "TODO: Implement this test"

    def test_get_on_disconnected_database_raises_error(self):
        """Test that reads fail too, not only writes."""
        # TODO: Create a UserRepository over an unconnected Database
        # TODO: Use pytest.raises(ConnectionError, match="not connected")
        # TODO: Try to read a user
        assert False, "TODO: Implement this test"
