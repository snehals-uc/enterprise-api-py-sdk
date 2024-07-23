# SDK Changes
### 1. Installation Requirement
Old sdk supported from **Python >=3.6** and new sdk supports from **Python >=3.7**. Also few supporting dependencies have been upgraded or changed.
### 2. Import for model
In old sdk the importing model was done from ```unicourt.model``` but in new sdk the model folder is changed to ```unicourt.models```.

***Example:***
*   Old SDK
    ```
    from unicourt.model.case_document_order_request import CaseDocumentOrderRequest
    ```
*   New SDK
    ```
    from unicourt.models.case_document_order_request import CaseDocumentOrderRequest
    ```
### 3. Return Object
In old sdk the return object was a ```json``` but in new sdk it is a ```python``` object.
### 4. Example code
In the example file ```old_sdk_test.py``` code at line *17*, old sdk will support both
```
case, status = CaseDocket.get_case(cases['case_search_result_array'][0]['case_id'])
```
```
case, status = CaseDocket.get_case(cases.case_search_result_array[0].case_id)
```
But, new sdk will only support
```
case, status = CaseDocket.get_case(cases.case_search_result_array[0].case_id)
```
