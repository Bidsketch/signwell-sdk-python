# AdditionalFieldsInnerInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x** | **float** | Horizontal value in the coordinates of the field (in pixels). Coordinates are specific to the page where fields are located. | 
**y** | **float** | Vertical value in the coordinates of the field (in pixels). Coordinates are specific to the page where fields are located. | 
**page** | **int** | The page number within the file. If the page does not exist within the file then the field won&#39;t be created. | 
**recipient_id** | **str** | Unique identifier of the recipient assigned to the field. Recipients assigned to fields will be the only ones that will see and be able to complete those fields. | 
**type** | [**FieldType**](FieldType.md) |  | 
**required** | **bool** | Whether the field must be completed by the recipient. Defaults to &#x60;true&#x60; except for checkbox type fields. | [optional] [default to True]
**label** | **str** | Text and Date fields only: label that is displayed when the field is empty. | [optional] 
**value** | [**AdditionalFieldsInnerInnerValue**](AdditionalFieldsInnerInnerValue.md) |  | [optional] 
**api_id** | **str** | Unique identifier of the field. Useful when needing to reference specific field values or update a document and its fields. | [optional] 
**name** | **str** | Checkbox fields only. At least 2 checkbox fields in an array of fields must be assigned to the same recipient and grouped with selection requirements. | [optional] 
**validation** | [**TextValidation**](TextValidation.md) |  | [optional] 
**fixed_width** | **bool** | Text fields only: whether the field width will stay fixed and text will display in multiple lines, rather than one long line. If set to &#x60;false&#x60; the field width will automatically grow horizontally to fit text on one line. Defaults to &#x60;false&#x60;. | [optional] [default to False]
**lock_sign_date** | **bool** | Date fields only: makes fields readonly and automatically populates with the date the recipient signed. Defaults to &#x60;false&#x60;. | [optional] [default to False]
**date_format** | [**DateFormat**](DateFormat.md) |  | [optional] 
**formula** | **str** | Date fields only (text field formulas coming soon): formulas are a way to prefill fields with calculated future or past dates. Addition, subtraction, and parentheses are allowed. Valid event dates are &#x60;created_date&#x60;, &#x60;sent_date&#x60;, and &#x60;signed_date&#x60;. Valid time periods are &#x60;day&#x60;, &#x60;days&#x60;, &#x60;week&#x60;, &#x60;weeks&#x60;, &#x60;month&#x60;, and &#x60;months&#x60;. Example: &#x60;formula: &#39;sent_date + 10 days&#39;&#x60;. Use with &#x60;lock_sign_date&#x60; if you&#39;d like to make the field readonly and prevent signers from choosing a different date. | [optional] 
**height** | **float** | Height of the field (in pixels). Maximum height varies by field type: Signature/Initials (200px), others (74px). When using text tags if the height is greater than the maximum height, the height will be set to the maximum height. | [optional] 
**width** | **float** | Width of the field (in pixels). For text fields, width will auto-grow unless &#x60;fixed_width&#x60; is true. | [optional] 
**options** | [**List[DropdownOption]**](DropdownOption.md) | Array of dropdown options (for dropdown/select fields only) | [optional] 
**default_option** | **str** | Default selected option (for dropdown/select fields only) | [optional] 
**allow_other** | **bool** | Whether to allow \&quot;Other\&quot; option with text input (for dropdown/select fields only) | [optional] [default to False]

## Example

```python
from signwell_sdk.models.additional_fields_inner_inner import AdditionalFieldsInnerInner

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalFieldsInnerInner from a JSON string
additional_fields_inner_inner_instance = AdditionalFieldsInnerInner.from_json(json)
# print the JSON string representation of the object
print(AdditionalFieldsInnerInner.to_json())

# convert the object into a dict
additional_fields_inner_inner_dict = additional_fields_inner_inner_instance.to_dict()
# create an instance of AdditionalFieldsInnerInner from a dict
additional_fields_inner_inner_from_dict = AdditionalFieldsInnerInner.from_dict(additional_fields_inner_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


