# Contact

Contact object data schema.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'Contact']
**address_array** | [**List[Address]**](Address.md) | List of available addresses. | 
**phone_number_array** | [**List[Phone]**](Phone.md) | List of available phone numbers. | 
**email_array** | [**List[Email]**](Email.md) | List of available emails. | 

## Example

```python
from unicourt.models.contact import Contact

# TODO update the JSON string below
json = "{}"
# create an instance of Contact from a JSON string
contact_instance = Contact.from_json(json)
# print the JSON string representation of the object
print(Contact.to_json())

# convert the object into a dict
contact_dict = contact_instance.to_dict()
# create an instance of Contact from a dict
contact_from_dict = Contact.from_dict(contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


