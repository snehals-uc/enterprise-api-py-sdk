# NormOrganizationTickerArrayInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exchange** | **str** |  | 
**symbols** | **List[str]** |  | 

## Example

```python
from unicourt.models.norm_organization_ticker_array_inner import NormOrganizationTickerArrayInner

# TODO update the JSON string below
json = "{}"
# create an instance of NormOrganizationTickerArrayInner from a JSON string
norm_organization_ticker_array_inner_instance = NormOrganizationTickerArrayInner.from_json(json)
# print the JSON string representation of the object
print(NormOrganizationTickerArrayInner.to_json())

# convert the object into a dict
norm_organization_ticker_array_inner_dict = norm_organization_ticker_array_inner_instance.to_dict()
# create an instance of NormOrganizationTickerArrayInner from a dict
norm_organization_ticker_array_inner_from_dict = NormOrganizationTickerArrayInner.from_dict(norm_organization_ticker_array_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


