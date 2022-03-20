AWS_REGION = "us-west-2"

DYNAMODB_TABLE_NAME = "moto_mock_table"
DYNAMODB_DEFAULT_VALIDATION = {"pk": "pk_test", "sk": "sk_test"}

S3_BUCKET_NAME = "moto_mock_bucket"

DYNAMODB_SCHEMA = {
        "AttributeDefinitions": [
            {"AttributeName": "pk", "AttributeType": "S"},
            {"AttributeName": "sk", "AttributeType": "S"},
        ],
        "TableName": DYNAMODB_TABLE_NAME,
        "KeySchema": [
            {"AttributeName": "pk", "KeyType": "HASH"},
            {"AttributeName": "sk", "KeyType": "RANGE"},
        ],
        "TableStatus": "ACTIVE",
}

DYNAMODB_DEFAULT_ITEMS = [
        {
            "pk": "pk_test",
            "sk": "sk_test"
        },
        {
            "pk": "pk_test_2",
            "sk": "sk_test_2"
        },
]
