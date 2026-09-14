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
import re


HACKERONE_REPORT_ID_PATTERN = re.compile(r"[1-9][0-9]*\Z")


def validate_report_id(value: object) -> str:
    """Return a positive decimal HackerOne report identifier."""
    if isinstance(value, bool):
        raise ValueError("Report ID must be a positive decimal integer")
    report_id = str(value)
    if not HACKERONE_REPORT_ID_PATTERN.fullmatch(report_id):
        raise ValueError("Report ID must be a positive decimal integer")
    return report_id
