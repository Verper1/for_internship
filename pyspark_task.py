from pyspark.sql import DataFrame

def get_product_category_pairs(products_df: DataFrame,
                               categories_df: DataFrame,
                               product_category_df: DataFrame) -> DataFrame:
    product_with_links_df = products_df.join(
        product_category_df,
        on=products_df["id"] == product_category_df["product_id"],
        how="left"
    )

    result_df = product_with_links_df.join(
        categories_df,
        on=product_with_links_df["category_id"] == categories_df["id"],
        how="left"
    )

    return result_df.select(
        products_df.name.alias("product_name"),
        categories_df.name.alias("category_name")
    )
