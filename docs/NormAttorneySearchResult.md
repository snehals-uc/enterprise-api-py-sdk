# NormAttorneySearchResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'NormAttorneySearchResult']
**norm_attorney_id** | **str** |  | 
**name** | **str** |  | 
**first_fetch_date** | **datetime** |  | 
**last_fetch_date** | **datetime** |  | 
**has_associated_public_data** | **bool** |  | 
**norm_attorney_details_api** | **str** |  | 
**matched_object_array** | [**List[MatchedObject]**](MatchedObject.md) |  | 

## Example

```python
from unicourt.models.norm_attorney_search_result import NormAttorneySearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of NormAttorneySearchResult from a JSON string
norm_attorney_search_result_instance = NormAttorneySearchResult.from_json(json)
# print the JSON string representation of the object
print(NormAttorneySearchResult.to_json())

# convert the object into a dict
norm_attorney_search_result_dict = norm_attorney_search_result_instance.to_dict()
# create an instance of NormAttorneySearchResult from a dict
norm_attorney_search_result_from_dict = NormAttorneySearchResult.from_dict(norm_attorney_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


