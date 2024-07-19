# CaseUpdatePacerOptionsResponse

Applicable for PACER cases.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object. | [default to 'CaseUpdatePacerOptionsResponse']
**pacer_user_id** | **str** | **Your PACER credentials username. This is mandatory when a PACER Case is being requested in the API. For Non PACER cases this is not mandatory. Suppose your request consists of Non PACER and PACER Cases then this needs to be passed becuase you are requesting a PACER case too.** | 
**pacer_client_code** | **str** | This is mandatory if your setting in PACER website is set to Yes for the flag &#x60;Require Client Code?&#x60; under &#x60;Set PACER Billing Preferences&#x60; page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/) | 
**fetch_participants_if_older_than_days** | **int** | **Currently this option is only applicable for Federal PACER cases. You can limit how often parties and attorneys for a PACER case are fetched to reduce your PACER fees. If you are tracking cases daily or hourly you could easily end up with a large PACER bill.**  **Use Case: Cases are typically updated to check for new docket entry filings. However every update to PACER case costs money. Participants for a case change less often than docket entry filings. So fetching participants for every update might result in unnecessary PACER costs; especially on cases which have a lot of parties and attorneys. So instead of getting charged the minimum cost of $0.10 for an update which might have had few docket entries, you could end up spending $3 for every update because there were a lot of parties for that case that were also fetched.**  **With this option you can choose when to fetch parties for case based on when was it last fetched.** You can limit how often this participants are fetched in a PACER case to keep your PACER costs under control.  Min days is 0 and Max days is 100.  Example: 1.  Specifying a value of 0 ensures that participants are fetched from PACER for this case update irrespective of when the participants were last fetched. 2.  Specifying a value of 30 ensures that participants are fetched from PACER for this case update only if the last fetch was older than 30 days.  | [default to 0]
**refresh_type** | **str** | This flag determines whether to pull only new or pull all the docket entries for a PACER case being requested.  Only one of the two values is allowed: -   fetchNewDocketEntries:     &gt;   Updates the PACER case with only new docket entries that have been added after the previous update of the case being requested. -   fetchAllDocketEntries:     &gt;   Updates the PACER case by re-parsing all dockets from #1 till latest docket entry available.  | [default to 'fetchNewDocketEntries']
**additional_page_array** | [**List[CaseUpdatePacerOptionsAdditionalPageArrayInner]**](CaseUpdatePacerOptionsAdditionalPageArrayInner.md) | Currently this option is only applicable for Federal PACER cases. The default behavior of the Case Update is to fetch the Docket Report from PACER which includes the parties and attorneys too.  However if you need to fetch information for other pages in PACER you will need to specify it here. - associatedCases: &gt; This will fetch the Associated Cases page in PACER if available. This page consists of related cases especially applicable for Multi-District Litigation cases and Member Cases. Including this option will internally link all related cases in our system. Data from this page will be available via the Related Cases API. - caseSummary: &gt; This will fetch the Case Summary page in PACER if available. This page consists of additional case info which is not present in the Docket Report page. Data from this page will be structured and available as response in the Case API’s &#x60;&#x60;&#x60;additional_info&#x60;&#x60;&#x60; field. - listOfCreditors: &gt; This page will fetch the “List Of Creditors” page for PACER Bankruptcy cases of case type \&quot;bk\&quot;. Note that this page cannot be extracted for Bankruptcy cases of case type \&quot;ap\&quot; (Adversary Proceedings). This page consists of the Creditor information like the name and address of the Creditors. Data from this page will be structured and available as response in the Case API.  | 

## Example

```python
from unicourt.models.case_update_pacer_options_response import CaseUpdatePacerOptionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CaseUpdatePacerOptionsResponse from a JSON string
case_update_pacer_options_response_instance = CaseUpdatePacerOptionsResponse.from_json(json)
# print the JSON string representation of the object
print(CaseUpdatePacerOptionsResponse.to_json())

# convert the object into a dict
case_update_pacer_options_response_dict = case_update_pacer_options_response_instance.to_dict()
# create an instance of CaseUpdatePacerOptionsResponse from a dict
case_update_pacer_options_response_from_dict = CaseUpdatePacerOptionsResponse.from_dict(case_update_pacer_options_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


