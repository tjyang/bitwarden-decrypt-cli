import json
import os
import pytest
from bitwarden_decrypt_simple_cli.services.StorageService import StorageService
from bitwarden_decrypt_simple_cli.tests.fixtures_common import db_test, common_data


def test_storage_service_init_without_db_path():
        storage_service = StorageService()
        assert os.path.isfile(storage_service.database_path)


@pytest.mark.usefixtures("db_test")
def test_storage_service_init_without_db_path(db_test):
        assert os.path.isfile(db_test.database_path)
        assert os.path.basename(db_test.database_path) == common_data('test_database_filename')
        assert db_test.database is not None
        assert db_test.database['userEmail'] == common_data('user_email')
        assert db_test.database['userId'] == common_data('user_id')
        assert 'ciphers_' + common_data('user_id') in db_test.database
        assert 'organizations_' + common_data('user_id') in db_test.database
        assert common_data('organization_id') in db_test.database['organizations_' + common_data('user_id')]