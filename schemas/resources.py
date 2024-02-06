valid_schema_list = {
    "type": "object",
    "properties": {
        "page": {"type": "integer"},
        "per_page": {"type": "integer"},
        "total": {"type": "integer"},
        "total_pages": {"type": "integer"}
    }
}

invalid_schema = {
    "type": "object",
    "properties": {
        "email": {"type": "string"}
    }
}
