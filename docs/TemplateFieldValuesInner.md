# TemplateFieldValuesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_id** | **str** | The API ID of the field in your template. This field is case sensitive. | 
**value** | [**TemplateFieldValuesInnerValue**](TemplateFieldValuesInnerValue.md) |  | 

## Example

```python
from signwell_sdk.models.template_field_values_inner import TemplateFieldValuesInner

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateFieldValuesInner from a JSON string
template_field_values_inner_instance = TemplateFieldValuesInner.from_json(json)
# print the JSON string representation of the object
print(TemplateFieldValuesInner.to_json())

# convert the object into a dict
template_field_values_inner_dict = template_field_values_inner_instance.to_dict()
# create an instance of TemplateFieldValuesInner from a dict
template_field_values_inner_from_dict = TemplateFieldValuesInner.from_dict(template_field_values_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


