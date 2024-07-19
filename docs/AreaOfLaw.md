# AreaOfLaw


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'AreaOfLaw']
**area_of_law_id** | **str** |  | 
**case_class_id** | **str** |  | 
**case_class** | **str** |  | 
**name** | **str** |  | 
**created_date** | **datetime** | The date and time when it was first created. This date and time is in UTC. Formatted as YYYY-MM-DD HH:MM:SS. | 

## Example

```python
from unicourt.models.area_of_law import AreaOfLaw

# TODO update the JSON string below
json = "{}"
# create an instance of AreaOfLaw from a JSON string
area_of_law_instance = AreaOfLaw.from_json(json)
# print the JSON string representation of the object
print(AreaOfLaw.to_json())

# convert the object into a dict
area_of_law_dict = area_of_law_instance.to_dict()
# create an instance of AreaOfLaw from a dict
area_of_law_from_dict = AreaOfLaw.from_dict(area_of_law_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


