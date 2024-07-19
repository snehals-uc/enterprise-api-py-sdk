# ServiceStatusDownDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object | [default to 'ServiceStatusDownDetails']
**reason** | **str** | This field determines the reason behind status being down. Following are the possible reason for the service to be down:   issueAtTheCourtSource: It means that the court source is either under Scheduled Maintenance or Unplanned Maintenance or Intermittently not responding.   notIntegrated: When an court with specific case type is not integrated in UniCourt.   brokenIntegration: Due to some updates made to the court site our existing Integration has broken and will require a fix to be made to support this court again for a spcific case type category. | 
**details** | **str** | Details of the reason. | 
**eta** | **str** | Estimated Time this Service could be Up again for the use. | 

## Example

```python
from unicourt.models.service_status_down_details import ServiceStatusDownDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceStatusDownDetails from a JSON string
service_status_down_details_instance = ServiceStatusDownDetails.from_json(json)
# print the JSON string representation of the object
print(ServiceStatusDownDetails.to_json())

# convert the object into a dict
service_status_down_details_dict = service_status_down_details_instance.to_dict()
# create an instance of ServiceStatusDownDetails from a dict
service_status_down_details_from_dict = ServiceStatusDownDetails.from_dict(service_status_down_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


