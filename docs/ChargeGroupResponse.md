# ChargeGroupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'ChargeGroupResponse']
**charge_group_array** | [**List[ChargeGroup]**](ChargeGroup.md) |  | 
**next_page_api** | **str** | Link to next page. | 
**previous_page_api** | **str** | Link to previous page. | 
**page_number** | **int** | Page number for which results where obtained. | 
**total_pages** | **int** | Total number of pages to obtain all the objects. | 
**total_count** | **int** | Total number of matches found. | 

## Example

```python
from unicourt.models.charge_group_response import ChargeGroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChargeGroupResponse from a JSON string
charge_group_response_instance = ChargeGroupResponse.from_json(json)
# print the JSON string representation of the object
print(ChargeGroupResponse.to_json())

# convert the object into a dict
charge_group_response_dict = charge_group_response_instance.to_dict()
# create an instance of ChargeGroupResponse from a dict
charge_group_response_from_dict = ChargeGroupResponse.from_dict(charge_group_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


