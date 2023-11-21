from unittest import mock
from lib.time import * 
from unittest.mock import Mock 

def test_error_call():
    mock_requester = Mock(name = 'requester')
    mock_response = Mock(name = 'response')
    timelib = Mock(name = 'timelib')
    timelib.time.return_value = 1
    mock_requester.get.return_value = mock_response 
    mock_response.json.return_value = {"abbreviation":"GMT","client_ip":"94.195.204.132","datetime":"2023-11-21T14:33:07.651310+00:00","day_of_week":2,"day_of_year":325,"dst":False,"dst_from":None,"dst_offset":0,"dst_until":None,"raw_offset":0,"timezone":"Europe/London","unixtime":1700577187,"utc_datetime":"2023-11-21T14:33:07.651310+00:00","utc_offset":"+00:00","week_number":47}

    te = TimeError(mock_requester, timelib)
    assert te.error() == 1700577186