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
import pytest

from hackerone_validation import validate_report_id


@pytest.mark.parametrize("value, expected", [(1, "1"), ("42", "42"), (987654321, "987654321")])
def test_validate_report_id_accepts_positive_decimal_ids(value, expected):
    assert validate_report_id(value) == expected


@pytest.mark.parametrize("value", [None, True, False, 0, -1, ".", "..", "../1", "1/2", "1?x", "01", "1.0", " 1"])
def test_validate_report_id_rejects_non_decimal_values(value):
    with pytest.raises(ValueError):
        validate_report_id(value)
