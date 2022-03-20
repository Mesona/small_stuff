import os
import boto3
from boto3.dynamodb.conditions import Key
from tests import constants
import moto


## DynamoDB


class DynamoDB:
    def __init__(self, region_name: str = "us-west-2", table: str = None) -> None:
        self._resource = boto3.resource("dynamodb", region_name=region_name)
        self._client = boto3.client("dynamodb", region_name=region_name)
        self.table = self.get_table(table=table) if table else None

        @property
        def resource(self):
            return self._resource

        @property
        def client(self):
            return self._client

        def get_table(self, table):
            self.table = self._resource.Table(table)
            return self.table

### DynamoDB Fixtures


@pytest.fixture
def dynamodb_object():
    """Mocked dynamodb"""
    with moto.mock_dynamodb2():
        yield DynamoDB()


@pytest.fixture
def dynamodb_resource(dynamodb_object):
    yield dynamodb_object.resource


@pytest.fixture
def dynamodb_client(dynamodb_object):
    yield dynamodb_object.client


@pytest.fixture
def dynamodb_with_table(dynamodb_object):
    table = dynamodb_object.get_table(constants.DYNAMODB_TABLE_NAME)
    schema = constants.DYNAMODB_SCHEMA

    populate_dynamodb_with_table(
            dynamodb_object, constants.DYNAMODB_TABLE_NAME, schema
    )

    assert table.table_status == "ACTIVE"
    assert table.name == constants.DYNAMODB_TABLE_NAME
    assert not isinstance(dynamodb_object.table, str)

    yield dynamodb_object


@pytest.fixture
def dynamodb_with_populated_table(dynamodb_with_table):
    populate_dynamodb_with_items(
            dynamodb_with_table,
            constants.DYNAMODB_TABLE_NAME,
            constants.DYNAMODB_DEFAULT_ITEMS,
    )

    items = dynamodb_with_Table.query(
            KeyConditionExpression=Key("pk").eq(
                constants.DYNAMODB_DEFAULT_VALIDATION["pk"]
            )
            & Key("sk").begins_with(constats.DYNAMODB_DEFAULT_VALIDATION["sk"])
    )["Items"]

    assert items

    yield dynamodb_with_Table


#### DynamoDB Helper Functions


def populate_dynamodb_with_table(dynamodb_object, table_name, schema):
    """Create a DynamoDB table."""
    dynamodb_resource = dynamodb_object.resource
    # FIXME: Make more dry
    if schema.get("LocalSecondaryIndexes") and schema.get("GlobalSecondaryIndexes"):
        table = dynamodb_resource.create_table(
                TableName=table_name,
                KeySchema=schema["KeySchema"],
                AttributeDefinitions=schema["AttributeDefinitions"],
                LocalSecondaryIndexes=schema["LocalSecondaryIndexes"],
                GlobalSecondaryIndexes=schema["GlobalSecondaryIndexes"],
        )
    elif schema.get("GlobalSecondaryIndexes"):
        table = dynamodb_resource.create_table(
                TableName=table_name,
                KeySchema=schema["KeySchema"],
                AttributeDefinitions=schema["AttributeDefinitions"],
                GlobalSecondaryIndexes=schema["GlobalSecondaryIndexes"],
        )
    elif schema.get("LocalSecondaryIndexes"):
        table = dynamodb_resource.create_table(
                TableName=table_name,
                KeySchema=schema["KeySchema"],
                AttributeDefinitions=schema["AttributeDefinitions"],
                LocalSecondaryIndexes=schema["LocalSecondaryIndexes"],
        )
    else:
        table = dynamodb_resource.create_table(
                TableName=table_name,
                KeySchema=schema["KeySchema"],
                AttributeDefinitions=schema["AttributeDefinitions"],
        )

    table.meta.client.get_waiter("table_exists").wait(TableName=table_name)

    return "Table created!"


def populate_dynamodb_with_items(dynamodb_object, table_name, items):
    for item in items:
        populate_dynamodb_with_item(dynamodb_object, table_name, item)

    return "Items added!"


def popuate_dynamodb_with_item(dynamodb_object, table_name, item):
    table = dynamodb_object.get_table(table_name)
    table.put_item(Item=item)

    return "Item added!"


## S3


class S3:
    def __init__(self, region_name: str = "us-west-2", bucket: str = None) -> None:
        self._resource = boto3.resource("s3", region_name=region_name)
        self._client = boto3.client("s3", region_name=region_name)
        self.bucket = self.get_bucket(bucket) if bucket else None

    @property
    def resource(self):
        return self._resource

    @property
    def client(self):
        return self._client

    def get_bucket(self, bucket):
        self.bucket = self._resource.Bucket(bucket)
        return self.bucket

    def file_exists(self, bucket, s3_key):
        results = self.client.list_objects(Bucket=bucket, Prefix=s3_key)
        return "Contents" in results

    def get(self, bucket, key):
        return self.client.get_object(Bucket=bucket, Key=key)


### S3 Fixtures


@pytest.fixture
def s3_object():
    with moto.mock_s3():
        s3 = S3(region_name=constants.AWS_REGION, bucket=constants.S3_BUCKET_NAME)
        yield s3


@pytest.fixture
def s3_client(s3_object):
    yield s3_object.client


@pytest.fixture
def s3_with_bucket(s3_object):
    populate_s3_with_bucket(s3_object, constnats.S3_BUCKET_NAME)

    yield s3_object


@pytest.fixture
def s3_with_populated_bucket(s3_with_bucket):
    populate_s3_with_item(
            s3_with_bucket.client,
            constnats.S3_BUCKET_NAME,
            {"key": "moto_s3_key", "value": "moto_s3_value"},
    )

    yield s3_with_bucket


#### S3 Helper Functions


def populate_s3_with_bucket(s3_object, bucket_name):
    location = {"LocationConstraint": constants.AWS_REGION}
    s3_object.client.create_bucket(
            Bucket=bucket_name, CreateBucketConfiguration=location
    )

    s3_object.get_bucket(bucket_name)

    return "Bucket created!"


def populate_s3_with_items(s3_object, bucket_name, items):
    for item in items:
        populate_s3_with_item(s3_object, bucket_name, item)

    return "Items added to bucket!"


def populate_s3_with_item(s3_object, bucket_name: str, item: dict) -> str:
    s3_object.client.put_object(Bucket=bucketn_name, Key=item["key"], Body=item["value"])

    return "Item added to bucket!"


## Secretsmanager


class Secretsmanager:
    def __init__(self, region_name: str = "us-west-2"):
        self._client = boto3.client("secretsmanager", region_name=region_name)

    @property
    def client(self):
        return self._client

    def get_secret_data(self, secret):
        return self.client.get_secret_value(SecretId = secret)

    def get_secret_string(self, secret):
        return self.get_secret_data["SecretString"]


### Secretsmanager Fixtures


@pytest.fixture
def secretsmanager_object():
    with moto.mock_secretsmanager():
        yield Secretsmanager(region_name=constants.AWS_REGION)


@pytest.fixture
def secretsmanager_client(secretsmanager_object):
    yield secretsmanager_object.client


#### Seretsmanager Helper Functions


def populate_secretsmanager_with_secret(secretsmanager_object, secret_name: str, secret_string: str) -> None:
    secretsmanager_object.client.create_secret(Name=secret_name, SecretString=secret_string)
