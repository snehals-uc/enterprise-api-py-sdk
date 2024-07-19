# CaseCountAnalyticsByPartyRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CaseCountAnalyticsByPartyRole']
**case_count** | **int** |  | 
**case_search_api** | **str** | Link to cases for the entity involving the search criteria. TBD. | 
**party_role** | [**PartyRole**](PartyRole.md) |  | 

## Example

```python
from unicourt.models.case_count_analytics_by_party_role import CaseCountAnalyticsByPartyRole

# TODO update the JSON string below
json = "{}"
# create an instance of CaseCountAnalyticsByPartyRole from a JSON string
case_count_analytics_by_party_role_instance = CaseCountAnalyticsByPartyRole.from_json(json)
# print the JSON string representation of the object
print(CaseCountAnalyticsByPartyRole.to_json())

# convert the object into a dict
case_count_analytics_by_party_role_dict = case_count_analytics_by_party_role_instance.to_dict()
# create an instance of CaseCountAnalyticsByPartyRole from a dict
case_count_analytics_by_party_role_from_dict = CaseCountAnalyticsByPartyRole.from_dict(case_count_analytics_by_party_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


