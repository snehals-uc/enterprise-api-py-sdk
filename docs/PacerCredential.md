# PacerCredential


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object. | [default to 'PacerCredential']
**pacer_user_id** | **str** | Pacer User Id. | 
**default_pacer_client_code** | **str** | This is mandatory if your setting in PACER website is set to Yes for the flag &#x60;Require Client Code?&#x60; under &#x60;Set PACER Billing Preferences&#x60; page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/) | 

## Example

```python
from unicourt.models.pacer_credential import PacerCredential

# TODO update the JSON string below
json = "{}"
# create an instance of PacerCredential from a JSON string
pacer_credential_instance = PacerCredential.from_json(json)
# print the JSON string representation of the object
print(PacerCredential.to_json())

# convert the object into a dict
pacer_credential_dict = pacer_credential_instance.to_dict()
# create an instance of PacerCredential from a dict
pacer_credential_from_dict = PacerCredential.from_dict(pacer_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


