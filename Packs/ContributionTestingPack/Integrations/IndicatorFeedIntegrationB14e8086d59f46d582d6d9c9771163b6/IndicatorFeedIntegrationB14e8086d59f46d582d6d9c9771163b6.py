import demistomock as demisto
from CommonServerPython import *

''' IMPORTS '''
import json

IPs_list = ['204.29.45.81', '5.76.125.46', '174.158.242.101', '211.174.36.188']

lastRun = demisto.getLastRun()


def fetch_indicators_mock():
    indicators = []

    for i in range(len(IPs_list)):
        value = IPs_list[i]

        if i == 0:
            indicators.append({
                "score": 0,
                "value": value,
                "type": "IP",
                "rawJSON": {
                    "value": value,
                    "myShortText": "111",
                    "myMultiSelect": "aaa"
                }
            }
            )
        else:
            indicators.append({
                "score": 0,
                "value": value,
                "type": "IP",
                "rawJSON": {
                    "value": value,
                    "myShortText": "333",
                    "myMultiSelect": "ccc"
                }
            }
            )

    return indicators


if demisto.command() == 'fetch-indicators':
    indicators = fetch_indicators_mock()

    demisto.createIndicators(indicators)

    # important (!) this is an ack to let the server know that we finished the fetch
    demisto.results("done")
    sys.exit(0)
