# Individual

* Only applicable if the Party is an Individual. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**first_name** | **str** |  | 
**middle_name** | **str** |  | 
**last_name** | **str** |  | 

## Example

```python
from unicourt.models.individual import Individual

# TODO update the JSON string below
json = "{}"
# create an instance of Individual from a JSON string
individual_instance = Individual.from_json(json)
# print the JSON string representation of the object
print(Individual.to_json())

# convert the object into a dict
individual_dict = individual_instance.to_dict()
# create an instance of Individual from a dict
individual_from_dict = Individual.from_dict(individual_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


