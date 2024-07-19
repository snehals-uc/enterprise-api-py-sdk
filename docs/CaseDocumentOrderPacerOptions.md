# CaseDocumentOrderPacerOptions

**Applicable for PACER cases.**

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pacer_user_id** | **str** | Your PACER credentials username. This is mandatory when a PACER Case is being requested in the API. For Non PACER cases this is not mandatory. Suppose your request consists of Non PACER and PACER Cases then this needs to be passed becuase you are requesting a PACER case too. | 
**pacer_client_code** | **str** | This is mandatory if your setting in PACER website is set to Yes for the flag &#x60;Require Client Code?&#x60; under &#x60;Set PACER Billing Preferences&#x60; page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/) | [optional] 

## Example

```python
from unicourt.models.case_document_order_pacer_options import CaseDocumentOrderPacerOptions

# TODO update the JSON string below
json = "{}"
# create an instance of CaseDocumentOrderPacerOptions from a JSON string
case_document_order_pacer_options_instance = CaseDocumentOrderPacerOptions.from_json(json)
# print the JSON string representation of the object
print(CaseDocumentOrderPacerOptions.to_json())

# convert the object into a dict
case_document_order_pacer_options_dict = case_document_order_pacer_options_instance.to_dict()
# create an instance of CaseDocumentOrderPacerOptions from a dict
case_document_order_pacer_options_from_dict = CaseDocumentOrderPacerOptions.from_dict(case_document_order_pacer_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


