# CaseExportCallback


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object. | [default to 'CaseExportCallback']
**case_export_callback_id** | **str** | Unique Id for the Case Export Callback. | 
**case_id** | **str** | Unique Id for a Case in UniCourt. | 
**callback_generated_date** | **datetime** | Date when the job is run. | 
**status** | **str** | Status of the request. | 
**case_export_callback_api** | **str** |  | 
**file** | [**ExportFile**](ExportFile.md) |  | 
**exception** | [**Exception**](Exception.md) |  | 

## Example

```python
from unicourt.models.case_export_callback import CaseExportCallback

# TODO update the JSON string below
json = "{}"
# create an instance of CaseExportCallback from a JSON string
case_export_callback_instance = CaseExportCallback.from_json(json)
# print the JSON string representation of the object
print(CaseExportCallback.to_json())

# convert the object into a dict
case_export_callback_dict = case_export_callback_instance.to_dict()
# create an instance of CaseExportCallback from a dict
case_export_callback_from_dict = CaseExportCallback.from_dict(case_export_callback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


