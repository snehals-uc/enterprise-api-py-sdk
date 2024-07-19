# Phone

Phone object data schema.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'Phone']
**phone_number** | **str** | Phone Number | 
**phone_type** | **str** | Resolved phone type (ideally from master data). | 
**is_visible** | **bool** | Boolean indicating if the phone is visible or not. | 
**first_fetch_date** | **datetime** | Date at which this record is created in UniCourt. | 
**last_fetch_date** | **datetime** | Date at which this record was updated in UniCourt. | 

## Example

```python
from unicourt.models.phone import Phone

# TODO update the JSON string below
json = "{}"
# create an instance of Phone from a JSON string
phone_instance = Phone.from_json(json)
# print the JSON string representation of the object
print(Phone.to_json())

# convert the object into a dict
phone_dict = phone_instance.to_dict()
# create an instance of Phone from a dict
phone_from_dict = Phone.from_dict(phone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


