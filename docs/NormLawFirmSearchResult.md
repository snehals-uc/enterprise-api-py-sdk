# NormLawFirmSearchResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'NormLawFirmSearchResult']
**norm_law_firm_id** | **str** |  | 
**name** | **str** |  | 
**first_fetch_date** | **datetime** |  | 
**last_fetch_date** | **datetime** |  | 
**norm_law_firm_details_api** | **str** |  | 
**matched_object_array** | [**List[MatchedObject]**](MatchedObject.md) |  | 

## Example

```python
from unicourt.models.norm_law_firm_search_result import NormLawFirmSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of NormLawFirmSearchResult from a JSON string
norm_law_firm_search_result_instance = NormLawFirmSearchResult.from_json(json)
# print the JSON string representation of the object
print(NormLawFirmSearchResult.to_json())

# convert the object into a dict
norm_law_firm_search_result_dict = norm_law_firm_search_result_instance.to_dict()
# create an instance of NormLawFirmSearchResult from a dict
norm_law_firm_search_result_from_dict = NormLawFirmSearchResult.from_dict(norm_law_firm_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


