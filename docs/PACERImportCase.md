# PACERImportCase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object | [default to 'PACERImportCase']
**court_fee** | **float** | Court Fee charged for the Find Case request. This is only applicable for Appeal Cases. | 
**pacer_import_case_results_array** | [**List[PACERImportCaseResults]**](PACERImportCaseResults.md) |  | 

## Example

```python
from unicourt.models.pacer_import_case import PACERImportCase

# TODO update the JSON string below
json = "{}"
# create an instance of PACERImportCase from a JSON string
pacer_import_case_instance = PACERImportCase.from_json(json)
# print the JSON string representation of the object
print(PACERImportCase.to_json())

# convert the object into a dict
pacer_import_case_dict = pacer_import_case_instance.to_dict()
# create an instance of PACERImportCase from a dict
pacer_import_case_from_dict = PACERImportCase.from_dict(pacer_import_case_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


