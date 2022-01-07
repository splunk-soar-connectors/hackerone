[comment]: # "Auto-generated SOAR connector documentation"
# HackerOne

Publisher: Splunk Community  
Connector Version: 2\.0\.2  
Product Vendor: HackerOne  
Product Name: HackerOne  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 4\.9\.39220  

This app integrates with HackerOne to support various generic and investigative actions

### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a HackerOne asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**api\_identifier** |  required  | string | HackerOne Identifier
**api\_token** |  required  | password | HackerOne API Token
**program\_name** |  required  | string | HackerOne Program Name
**state\_filter** |  optional  | string | Filter for report state \(to be used when polling\)
**assignment\_filter** |  optional  | string | Filter for report assignment \(to be used when polling\)
**full\_comments** |  optional  | boolean | Collect comments for reports \(to be used when polling, much slower\)
**phantom\_api\_token** |  required  | password | Phantom API token for updating existing containers

### Supported Actions  
[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using supplied credentials  
[get report](#action-get-report) - Get a report by ID  
[get reports](#action-get-reports) - Get HackerOne reports  
[get updated reports](#action-get-updated-reports) - Get updated HackerOne reports  
[update tracking id](#action-update-tracking-id) - Update HackerOne report with tracking ID  
[unassign report](#action-unassign-report) - Unassign HackerOne report with tracking ID  
[on poll](#action-on-poll) - Consume HackerOne reports and generate containers for them  

## action: 'test connectivity'
Validate the asset configuration for connectivity using supplied credentials

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'get report'
Get a report by ID

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**report\_id** |  required  | ID of report to get | string |  `hackerone report id` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.report\_id | string |  `hackerone report id` 
action\_result\.data\.\*\.id | string | 
action\_result\.data\.\*\.reporter\_id | string | 
action\_result\.data\.\*\.reporter\_name | string | 
action\_result\.data\.\*\.reporter\_username | string | 
action\_result\.data\.\*\.reporter\_reputation | string | 
action\_result\.data\.\*\.assignee\_id | string | 
action\_result\.data\.\*\.assignee\_name | string | 
action\_result\.data\.\*\.assignee\_type | string | 
action\_result\.data\.\*\.program\_id | string | 
action\_result\.data\.\*\.program\_name | string | 
action\_result\.data\.\*\.severity\_rating | string | 
action\_result\.data\.\*\.severity\_author\_type | string | 
action\_result\.data\.\*\.severity\_user\_id | string | 
action\_result\.data\.\*\.severity\_score | string | 
action\_result\.data\.\*\.severity\_attack\_complexity | string | 
action\_result\.data\.\*\.severity\_attack\_vector | string | 
action\_result\.data\.\*\.severity\_availability | string | 
action\_result\.data\.\*\.severity\_confidentiality | string | 
action\_result\.data\.\*\.severity\_integrity | string | 
action\_result\.data\.\*\.severity\_privileges\_required | string | 
action\_result\.data\.\*\.severity\_user\_interaction | string | 
action\_result\.data\.\*\.severity\_scope | string | 
action\_result\.data\.\*\.severity\_cvf | string | 
action\_result\.data\.\*\.weakness\_id | string | 
action\_result\.data\.\*\.weakness\_name | string | 
action\_result\.data\.\*\.weakness\_external\_id | string | 
action\_result\.data\.\*\.attachments | string | 
action\_result\.data\.\*\.comments | string | 
action\_result\.data\.\*\.title | string | 
action\_result\.data\.\*\.state | string | 
action\_result\.data\.\*\.created\_at | string | 
action\_result\.data\.\*\.closed\_at | string | 
action\_result\.data\.\*\.last\_reporter\_activity\_at | string | 
action\_result\.data\.\*\.first\_program\_activity\_at | string | 
action\_result\.data\.\*\.last\_program\_activity\_at | string | 
action\_result\.data\.\*\.bounty\_awarded\_at | string | 
action\_result\.data\.\*\.swag\_awarded\_at | string | 
action\_result\.data\.\*\.disclosed\_at | string | 
action\_result\.data\.\*\.reporter\_agreed\_on\_going\_public\_at | string | 
action\_result\.data\.\*\.issue\_tracker\_reference\_id | string | 
action\_result\.data\.\*\.issue\_tracker\_reference\_url | string | 
action\_result\.data\.\*\.last\_public\_activity\_at | string | 
action\_result\.data\.\*\.last\_activity\_at | string | 
action\_result\.data\.\*\.cve\_ids | string | 
action\_result\.data\.\*\.source | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get reports'
Get HackerOne reports

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**state\_filter** |  optional  | Report State Filter | string | 
**assignment\_filter** |  optional  | Report Assignment Filter | string | 
**full\_comments** |  optional  | Collect comments for reports \(much slower\) | boolean | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.state\_filter | string | 
action\_result\.parameter\.assignment\_filter | string | 
action\_result\.parameter\.full\_comments | boolean | 
action\_result\.data\.\*\.reports | string | 
action\_result\.data\.\*\.count | numeric | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get updated reports'
Get updated HackerOne reports

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**state\_filter** |  optional  | Report State Filter | string | 
**assignment\_filter** |  optional  | Report Assignment Filter | string | 
**full\_comments** |  optional  | Collect comments for reports \(much slower\) | boolean | 
**range** |  optional  | How many minutes back to get changed reports from | numeric | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.state\_filter | string | 
action\_result\.parameter\.assignment\_filter | string | 
action\_result\.parameter\.full\_comments | boolean | 
action\_result\.parameter\.range | numeric | 
action\_result\.data\.\*\.reports | string | 
action\_result\.data\.\*\.count | numeric | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'update tracking id'
Update HackerOne report with tracking ID

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**report\_id** |  required  | ID of report to update | string |  `hackerone report id` 
**tracking\_id** |  required  | ID of tracking ticket | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.report\_id | string |  `hackerone report id` 
action\_result\.parameter\.tracking\_id | string | 
action\_result\.data | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'unassign report'
Unassign HackerOne report with tracking ID

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**report\_id** |  required  | ID of report to unassign | string |  `hackerone report id` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.report\_id | string |  `hackerone report id` 
action\_result\.data | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'on poll'
Consume HackerOne reports and generate containers for them

Type: **ingest**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output