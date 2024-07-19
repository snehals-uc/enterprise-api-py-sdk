# CaseSearchResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CaseSearchResult']
**case_id** | **str** |  | 
**case_name** | **str** |  | 
**case_number** | **str** |  | 
**filed_date** | **datetime** |  | 
**court** | [**Court**](Court.md) |  | 
**court_location** | [**CourtLocation**](CourtLocation.md) |  | 
**case_type** | [**CaseType**](CaseType.md) |  | 
**case_status** | [**CaseStatus**](CaseStatus.md) |  | 
**first_fetch_date** | **datetime** |  | 
**last_fetch_date** | **datetime** |  | 
**last_fetch_date_with_updates** | **datetime** |  | 
**participants_last_fetch_date** | **datetime** |  | 
**case_api** | **str** |  | 
**matched_object_array** | [**List[MatchedObject]**](MatchedObject.md) |  | 

## Example

```python
from unicourt.models.case_search_result import CaseSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of CaseSearchResult from a JSON string
case_search_result_instance = CaseSearchResult.from_json(json)
# print the JSON string representation of the object
print(CaseSearchResult.to_json())

# convert the object into a dict
case_search_result_dict = case_search_result_instance.to_dict()
# create an instance of CaseSearchResult from a dict
case_search_result_from_dict = CaseSearchResult.from_dict(case_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


