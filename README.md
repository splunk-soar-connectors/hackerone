# HackerOne

Publisher: Splunk Community <br>
Connector Version: 3.0.0 <br>
Product Vendor: HackerOne <br>
Product Name: HackerOne <br>
Minimum Product Version: 4.9.39220

This app integrates with HackerOne to support various generic and investigative actions

### Configuration variables

This table lists the configuration variables required to operate HackerOne. These variables are specified when configuring a HackerOne asset in Splunk SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**api_identifier** | required | string | HackerOne Identifier |
**api_token** | required | password | HackerOne API Token |
**program_name** | required | string | HackerOne Program Name |
**state_filter** | optional | string | Filter for report state (to be used when polling) |
**assignment_filter** | optional | string | Filter for report assignment (to be used when polling) |
**full_comments** | optional | boolean | Collect comments for reports (to be used when polling, much slower) |
**phantom_api_token** | required | password | Phantom API token for updating existing containers |
**verify_server_cert** | optional | boolean | Verify TLS certificates for HackerOne and Splunk SOAR requests |

### Supported Actions

[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using supplied credentials <br>
[get report](#action-get-report) - Get a report by ID <br>
[get reports](#action-get-reports) - Get HackerOne reports <br>
[get updated reports](#action-get-updated-reports) - Get updated HackerOne reports <br>
[update tracking id](#action-update-tracking-id) - Update HackerOne report with tracking ID <br>
[unassign report](#action-unassign-report) - Unassign HackerOne report with tracking ID <br>
[on poll](#action-on-poll) - Consume HackerOne reports and generate containers for them

## action: 'test connectivity'

Validate the asset configuration for connectivity using supplied credentials

Type: **test** <br>
Read only: **True**

#### Action Parameters

No parameters are required for this action

#### Action Output

No Output

## action: 'get report'

Get a report by ID

Type: **investigate** <br>
Read only: **True**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**report_id** | required | ID of report to get | string | `hackerone report id` |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.report_id | string | `hackerone report id` | |
action_result.data.\*.id | string | | |
action_result.data.\*.reporter_id | string | | |
action_result.data.\*.reporter_name | string | | |
action_result.data.\*.reporter_username | string | | |
action_result.data.\*.reporter_reputation | string | | |
action_result.data.\*.assignee_id | string | | |
action_result.data.\*.assignee_name | string | | |
action_result.data.\*.assignee_type | string | | |
action_result.data.\*.program_id | string | | |
action_result.data.\*.program_name | string | | |
action_result.data.\*.severity_rating | string | | |
action_result.data.\*.severity_author_type | string | | |
action_result.data.\*.severity_user_id | string | | |
action_result.data.\*.severity_score | string | | |
action_result.data.\*.severity_attack_complexity | string | | |
action_result.data.\*.severity_attack_vector | string | | |
action_result.data.\*.severity_availability | string | | |
action_result.data.\*.severity_confidentiality | string | | |
action_result.data.\*.severity_integrity | string | | |
action_result.data.\*.severity_privileges_required | string | | |
action_result.data.\*.severity_user_interaction | string | | |
action_result.data.\*.severity_scope | string | | |
action_result.data.\*.severity_cvf | string | | |
action_result.data.\*.weakness_id | string | | |
action_result.data.\*.weakness_name | string | | |
action_result.data.\*.weakness_external_id | string | | |
action_result.data.\*.attachments | string | | |
action_result.data.\*.comments | string | | |
action_result.data.\*.title | string | | |
action_result.data.\*.state | string | | |
action_result.data.\*.created_at | string | | |
action_result.data.\*.closed_at | string | | |
action_result.data.\*.last_reporter_activity_at | string | | |
action_result.data.\*.first_program_activity_at | string | | |
action_result.data.\*.last_program_activity_at | string | | |
action_result.data.\*.bounty_awarded_at | string | | |
action_result.data.\*.swag_awarded_at | string | | |
action_result.data.\*.disclosed_at | string | | |
action_result.data.\*.reporter_agreed_on_going_public_at | string | | |
action_result.data.\*.issue_tracker_reference_id | string | | |
action_result.data.\*.issue_tracker_reference_url | string | | |
action_result.data.\*.last_public_activity_at | string | | |
action_result.data.\*.last_activity_at | string | | |
action_result.data.\*.cve_ids | string | | |
action_result.data.\*.source | string | | |
action_result.status | string | | success failed |
action_result.message | string | | |
action_result.summary | string | | |
summary.total_objects | numeric | | 1 |
summary.total_objects_successful | numeric | | 1 |

## action: 'get reports'

Get HackerOne reports

Type: **investigate** <br>
Read only: **True**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**state_filter** | optional | Report State Filter | string | |
**assignment_filter** | optional | Report Assignment Filter | string | |
**full_comments** | optional | Collect comments for reports (much slower) | boolean | |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.state_filter | string | | |
action_result.parameter.assignment_filter | string | | |
action_result.parameter.full_comments | boolean | | True False |
action_result.data.\*.reports | string | | |
action_result.data.\*.count | numeric | | |
action_result.status | string | | success failed |
action_result.message | string | | |
action_result.summary | string | | |
summary.total_objects | numeric | | 1 |
summary.total_objects_successful | numeric | | 1 |

## action: 'get updated reports'

Get updated HackerOne reports

Type: **investigate** <br>
Read only: **True**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**state_filter** | optional | Report State Filter | string | |
**assignment_filter** | optional | Report Assignment Filter | string | |
**full_comments** | optional | Collect comments for reports (much slower) | boolean | |
**range** | optional | How many minutes back to get changed reports from | numeric | |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.state_filter | string | | |
action_result.parameter.assignment_filter | string | | |
action_result.parameter.full_comments | boolean | | True False |
action_result.parameter.range | numeric | | |
action_result.data.\*.reports | string | | |
action_result.data.\*.count | numeric | | |
action_result.status | string | | success failed |
action_result.message | string | | |
action_result.summary | string | | |
summary.total_objects | numeric | | 1 |
summary.total_objects_successful | numeric | | 1 |

## action: 'update tracking id'

Update HackerOne report with tracking ID

Type: **generic** <br>
Read only: **False**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**report_id** | required | ID of report to update | string | `hackerone report id` |
**tracking_id** | required | ID of tracking ticket | string | |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.report_id | string | `hackerone report id` | |
action_result.parameter.tracking_id | string | | |
action_result.data | string | | |
action_result.status | string | | success failed |
action_result.message | string | | |
action_result.summary | string | | |
summary.total_objects | numeric | | 1 |
summary.total_objects_successful | numeric | | 1 |

## action: 'unassign report'

Unassign HackerOne report with tracking ID

Type: **generic** <br>
Read only: **False**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**report_id** | required | ID of report to unassign | string | `hackerone report id` |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.report_id | string | `hackerone report id` | |
action_result.data | string | | |
action_result.status | string | | success failed |
action_result.message | string | | |
action_result.summary | string | | |
summary.total_objects | numeric | | 1 |
summary.total_objects_successful | numeric | | 1 |

## action: 'on poll'

Consume HackerOne reports and generate containers for them

Type: **ingest** <br>
Read only: **True**

#### Action Parameters

No parameters are required for this action

#### Action Output

No Output

______________________________________________________________________

Auto-generated Splunk SOAR Connector documentation.

Copyright 2026 Splunk Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
