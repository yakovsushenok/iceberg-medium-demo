from example_code.models import DynamoDB, NewImage

example_table_columns = ["person_name", "sort_key", "make", "model", "oil_change"]


def create_insert_query(dynamodb: DynamoDB):
    return " ".join(
        [
            "INSERT INTO example_db.example_table",
            "(" + f"{','.join(example_table_columns)}",
            ")",
            "VALUES",
            get_query_values(dynamodb.new_image),
        ]
    )

def get_query_values(new_image: NewImage):
    return "(" + "),(".join(get_query_rows(new_image)) + ")"

def get_query_rows(new_image: NewImage):
    
