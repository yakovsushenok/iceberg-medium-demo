from example_code.models import DynamoDB, NewImage
from example_code.utils import add_quote

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

    rows = []
    # person_name and sort_key are the same for every row
    person_name = new_image.person_name
    sort_key = new_image.sort_key

    # iterate over each car
    for car in new_image.cars:
        make = car.make
        model = car.model
        oil_changes = car.maintenance.oil_changes

        for oil_change in oil_changes:
            row_to_append = [
                person_name,
                sort_key,
                make,
                model,
                oil_change,
            ]
            rows.append([add_quote(field) for field in row_to_append])
    # each element of the rows list is a list itself. By joining each element with a comma
    # separator and creating a string, we create a row to be inserted into the SQL query.
    query_rows = [", ".join(row) for row in rows]
    # now we just format it, so that we can plug it into the query.
    return "(" + "), (".join(query_rows) + ")"
