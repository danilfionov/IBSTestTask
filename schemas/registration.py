valid_schema = {
    "type": "object",
    "properties": {
        "email": {"type": "string"},
        "password": {"type": "string"}
    }
}

invalid_schema = {
    "type": "object",
    "properties": {
        "email": {"type": "string"}
    }
}
