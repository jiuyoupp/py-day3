from jospehring.usecase.ring import Ring
from jospehring.domain.person import Person
from jospehring.adapter.reader import read_data
from unittest import mock
from jospehring.adapter.interface import Interface
import unittest


class TestRingFromReader(unittest.TestCase):
    @mock.patch('jospehring.adapter.reader.read_data')
    def test_txtreader(self, mock_txtreader):
        mock_txtreader.return_value = [Person('冯巧', 1), Person('昌瑶灵', 2), Person('袁春绿', 3)]
        interface = Interface()
        interface.create_jospehring1()

        assert interface.jospeh._ring[0].name == '冯巧'

