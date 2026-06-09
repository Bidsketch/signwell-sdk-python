# AccountInfoResponsePreferences


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_format** | **str** |  | [optional] 
**days_until_links_expire** | **int** |  | [optional] 
**disable_apply_everywhere** | **bool** |  | [optional] 
**disable_apply_everywhere_effective** | **bool** |  | [optional] 
**disable_drawn_signatures** | **bool** |  | [optional] 
**disable_typed_signatures** | **bool** |  | [optional] 
**disable_uploaded_signatures** | **bool** |  | [optional] 
**enable_redirect** | **bool** |  | [optional] 
**hide_document_id_in_audit** | **bool** |  | [optional] 
**mute_branding** | **bool** |  | [optional] 
**redirect_url** | **str** |  | [optional] 
**separate_audit_pdf** | **bool** |  | [optional] 
**separate_completed_file** | **bool** |  | [optional] 
**enable_nom151_compliance** | **bool** |  | [optional] 

## Example

```python
from signwell_sdk.models.account_info_response_preferences import AccountInfoResponsePreferences

# TODO update the JSON string below
json = "{}"
# create an instance of AccountInfoResponsePreferences from a JSON string
account_info_response_preferences_instance = AccountInfoResponsePreferences.from_json(json)
# print the JSON string representation of the object
print(AccountInfoResponsePreferences.to_json())

# convert the object into a dict
account_info_response_preferences_dict = account_info_response_preferences_instance.to_dict()
# create an instance of AccountInfoResponsePreferences from a dict
account_info_response_preferences_from_dict = AccountInfoResponsePreferences.from_dict(account_info_response_preferences_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


