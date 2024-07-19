# CourtServiceStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object | [default to 'CourtServiceStatus']
**court_service_status_id** | **str** | Court Service Status Object ID | 
**court_id_array** | **List[Optional[str]]** | All the court ids associated to the service status | 
**court_location_id_array** | **List[Optional[str]]** | All the court location ids associated to the service status | 
**case_class_id_array** | **List[Optional[str]]** | All the Case class ids associated to the service status | 
**service_status_as_on** | **str** | Date when the service status was last fetched. | 
**case_update_service_status** | [**ServiceStatus**](ServiceStatus.md) |  | 
**case_track_service_status** | [**ServiceStatus**](ServiceStatus.md) |  | 
**case_document_order_service_status** | [**ServiceStatus**](ServiceStatus.md) |  | 

## Example

```python
from unicourt.models.court_service_status import CourtServiceStatus

# TODO update the JSON string below
json = "{}"
# create an instance of CourtServiceStatus from a JSON string
court_service_status_instance = CourtServiceStatus.from_json(json)
# print the JSON string representation of the object
print(CourtServiceStatus.to_json())

# convert the object into a dict
court_service_status_dict = court_service_status_instance.to_dict()
# create an instance of CourtServiceStatus from a dict
court_service_status_from_dict = CourtServiceStatus.from_dict(court_service_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


