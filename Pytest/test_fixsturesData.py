import pytest
from Practice.Logging.base_class import BaseClass


@pytest.mark.usefixtures('dataLoad')
class TestExample2(BaseClass):
    def test_edit_profile(self, dataLoad):
        log = self.get_logger()
        log.info(dataLoad[0])
        log.info(dataLoad[1])
        log.info(dataLoad[2])

