# NormCorporateGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'NormCorporateGroup']
**norm_corporate_group_id** | **str** |  | 
**norm_corporate_group_name** | **str** |  | 

## Example

```python
from unicourt.models.norm_corporate_group import NormCorporateGroup

# TODO update the JSON string below
json = "{}"
# create an instance of NormCorporateGroup from a JSON string
norm_corporate_group_instance = NormCorporateGroup.from_json(json)
# print the JSON string representation of the object
print(NormCorporateGroup.to_json())

# convert the object into a dict
norm_corporate_group_dict = norm_corporate_group_instance.to_dict()
# create an instance of NormCorporateGroup from a dict
norm_corporate_group_from_dict = NormCorporateGroup.from_dict(norm_corporate_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


