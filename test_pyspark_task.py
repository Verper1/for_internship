from pyspark_task import get_product_category_pairs

def test_get_product_category_pairs(spark):
    products_df = spark.createDataFrame([
        {"id": 1, "name": "Laptop"},
        {"id": 2, "name": "Phone"},
        {"id": 3, "name": "Mouse"},
    ])

    categories_df = spark.createDataFrame([
        {"id": 10, "name": "Electronics"},
        {"id": 20, "name": "Accessories"},
    ])

    product_category_df = spark.createDataFrame([
        {"product_id": 1, "category_id": 10},
        {"product_id": 3, "category_id": 20},
    ])

    result_df = get_product_category_pairs(
        products_df, categories_df, product_category_df
    )

    result = {(row["product_name"], row["category_name"]) for row in result_df.collect()}

    expected = {
        ("Laptop", "Electronics"),
        ("Phone", None),
        ("Mouse", "Accessories"),
    }

    assert result == expected

# Для теста в терминале ввести: pytest test_pyspark_task.py
