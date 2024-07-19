# PacerCredentialRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pacer_user_id** | **str** | Pacer User Id. | 
**default_pacer_client_code** | **str** | This is mandatory if your setting in PACER website is set to Yes for the flag &#x60;Require Client Code?&#x60; under &#x60;Set PACER Billing Preferences&#x60; page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/) | [optional] 
**password** | **str** | Password. | 

## Example

```python
from unicourt.models.pacer_credential_request import PacerCredentialRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PacerCredentialRequest from a JSON string
pacer_credential_request_instance = PacerCredentialRequest.from_json(json)
# print the JSON string representation of the object
print(PacerCredentialRequest.to_json())

# convert the object into a dict
pacer_credential_request_dict = pacer_credential_request_instance.to_dict()
# create an instance of PacerCredentialRequest from a dict
pacer_credential_request_from_dict = PacerCredentialRequest.from_dict(pacer_credential_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


