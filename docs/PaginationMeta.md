# PaginationMeta

Pagination metadata for list responses

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_page** | **int** | Current page number | 
**next_page** | **int** | Next page number, null if on last page | [optional] 
**previous_page** | **int** | Previous page number, null if on first page | [optional] 
**total_count** | **int** | Total number of records | 
**total_pages** | **int** | Total number of pages | 

## Example

```python
from signwell_sdk.models.pagination_meta import PaginationMeta

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationMeta from a JSON string
pagination_meta_instance = PaginationMeta.from_json(json)
# print the JSON string representation of the object
print(PaginationMeta.to_json())

# convert the object into a dict
pagination_meta_dict = pagination_meta_instance.to_dict()
# create an instance of PaginationMeta from a dict
pagination_meta_from_dict = PaginationMeta.from_dict(pagination_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


