# ChargeSeverityResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'ChargeSeverityResponse']
**charge_severity_array** | [**List[ChargeSeverity]**](ChargeSeverity.md) |  | 
**next_page_api** | **str** | Link to next page. | 
**previous_page_api** | **str** | Link to previous page. | 
**page_number** | **int** | Page number for which results where obtained. | 
**total_pages** | **int** | Total number of pages to obtain all the objects. | 
**total_count** | **int** | Total number of matches found. | 

## Example

```python
from unicourt.models.charge_severity_response import ChargeSeverityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChargeSeverityResponse from a JSON string
charge_severity_response_instance = ChargeSeverityResponse.from_json(json)
# print the JSON string representation of the object
print(ChargeSeverityResponse.to_json())

# convert the object into a dict
charge_severity_response_dict = charge_severity_response_instance.to_dict()
# create an instance of ChargeSeverityResponse from a dict
charge_severity_response_from_dict = ChargeSeverityResponse.from_dict(charge_severity_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


