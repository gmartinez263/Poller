import pytest
from poller import Participant
from poller import Poller
from unittest import mock


def test_participant():
    participant = Participant("Isabelle",5,3,1,1)
    assert str(participant) == "Isabelle,5,3,1,1"

@mock.patch('builtins.open')
def test_dunder(mock_open):
    mock_open.return_value = mock.Mock()
    mock_open.return_value.read.return_value = "Isabelle Watanabe,0,0,0,0"
    with Poller("") as poller:
        poller.attempted()
        assert str(poller) == "Isabelle Watanabe,1,0,1,0"      