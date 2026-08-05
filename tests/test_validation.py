# Copyright (c) 2026 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import unittest
from unittest.mock import Mock

import phantom.app as phantom
from hackerone_connector import HackerOneConnector
from hackerone_validation import validate_report_id


class ValidateReportIdTest(unittest.TestCase):
    def test_accepts_positive_decimal_ids(self):
        for value, expected in ((1, "1"), ("42", "42"), (987654321, "987654321")):
            with self.subTest(value=value):
                self.assertEqual(validate_report_id(value), expected)

    def test_rejects_non_decimal_values(self):
        invalid_values = (
            None,
            True,
            False,
            0,
            -1,
            ".",
            "..",
            "../1",
            "1/2",
            "1?x",
            "01",
            "1.0",
            " 1",
        )
        for value in invalid_values:
            with self.subTest(value=value), self.assertRaises(ValueError):
                validate_report_id(value)


class ReportActionValidationTest(unittest.TestCase):
    def setUp(self):
        self.connector = HackerOneConnector()
        self.connector.save_progress = Mock()

    def test_update_tracking_id_returns_action_error_for_invalid_report_id(self):
        action_result = Mock()
        action_result.set_status.return_value = phantom.APP_ERROR
        self.connector._post_rest_data = Mock()

        status = self.connector._update_tracking_id(
            {"report_id": "../1", "tracking_id": "CASE-1"}, action_result
        )

        self.assertEqual(status, phantom.APP_ERROR)
        action_result.set_status.assert_called_once_with(
            phantom.APP_ERROR, "Exception occurred while updating tracking id"
        )
        self.connector._post_rest_data.assert_not_called()

    def test_unassign_report_returns_action_error_for_invalid_report_id(self):
        action_result = Mock()
        action_result.set_status.return_value = phantom.APP_ERROR
        self.connector._put_rest_data = Mock()

        status = self.connector._unassign_report({"report_id": "1/2"}, action_result)

        self.assertEqual(status, phantom.APP_ERROR)
        action_result.set_status.assert_called_once_with(
            phantom.APP_ERROR, "Exception occurred while updating tracking id"
        )
        self.connector._put_rest_data.assert_not_called()
