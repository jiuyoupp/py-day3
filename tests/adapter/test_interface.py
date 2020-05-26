from jospehring.usecase.ring import Ring
from jospehring.domain.person import Person

from unittest import mock
from jospehring.adapter.interface import Interface
import unittest


class TestRingFromReader(unittest.TestCase):
    @mock.patch('jospehring.adapter.interface.ReadData')
    def test_txtreader(self, mock_case):
        mock_case.read_data.return_value = [Person('冯巧', 1), Person('昌瑶灵', 2), Person('袁春绿', 3)]
        interface = Interface()
        interface.create_jospehring('')
        assert interface.jospeh.ring[0].name == '冯巧'
        assert interface.jospeh.ring[1].name == '昌瑶灵'
