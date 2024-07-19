# NormPartySearchResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'NormPartySearchResult']
**norm_party_id** | **str** |  | 
**name** | **str** |  | 
**party_classification_type** | **str** |  | 
**first_fetch_date** | **datetime** |  | 
**last_fetch_date** | **datetime** |  | 
**norm_party_details_api** | **str** |  | 
**matched_object_array** | [**List[MatchedObject]**](MatchedObject.md) |  | 

## Example

```python
from unicourt.models.norm_party_search_result import NormPartySearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of NormPartySearchResult from a JSON string
norm_party_search_result_instance = NormPartySearchResult.from_json(json)
# print the JSON string representation of the object
print(NormPartySearchResult.to_json())

# convert the object into a dict
norm_party_search_result_dict = norm_party_search_result_instance.to_dict()
# create an instance of NormPartySearchResult from a dict
norm_party_search_result_from_dict = NormPartySearchResult.from_dict(norm_party_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


