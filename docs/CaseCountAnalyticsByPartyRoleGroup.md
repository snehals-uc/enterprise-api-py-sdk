# CaseCountAnalyticsByPartyRoleGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CaseCountAnalyticsByPartyRoleGroup']
**case_count** | **int** |  | 
**case_search_api** | **str** | Link to cases for the entity involving the search criteria. TBD. | 
**party_role_group** | [**PartyRoleGroup**](PartyRoleGroup.md) |  | 

## Example

```python
from unicourt.models.case_count_analytics_by_party_role_group import CaseCountAnalyticsByPartyRoleGroup

# TODO update the JSON string below
json = "{}"
# create an instance of CaseCountAnalyticsByPartyRoleGroup from a JSON string
case_count_analytics_by_party_role_group_instance = CaseCountAnalyticsByPartyRoleGroup.from_json(json)
# print the JSON string representation of the object
print(CaseCountAnalyticsByPartyRoleGroup.to_json())

# convert the object into a dict
case_count_analytics_by_party_role_group_dict = case_count_analytics_by_party_role_group_instance.to_dict()
# create an instance of CaseCountAnalyticsByPartyRoleGroup from a dict
case_count_analytics_by_party_role_group_from_dict = CaseCountAnalyticsByPartyRoleGroup.from_dict(case_count_analytics_by_party_role_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


