import json
import csv
import pandas as pd

data_dir = "../data"
recipe_dir = data_dir + "/recipes_raw/"

epi_json = recipe_dir + "recipes_raw_nosource_epi.json"
fn_json = recipe_dir + "recipes_raw_nosource_fn.json"


def read_json(file_names):
    """

    :param file_names: a list of json file names to read
    :return:
    """

    with open('../data/recipes.csv', 'w') as out_f:
        writer = csv.writer(out_f)

        writer.writerow(["title", "ingredients", "instructions"])

        for fn in file_names:

            with open(fn, 'r') as f:
                x = json.loads(f.read())

            f.close()

            for k, v in x.items():
                writer.writerow([v["title"],
                                 v["ingredients"],
                                 v["instructions"]])

    out_f.close()


read_json([epi_json, fn_json])

recipes = pd.read_csv("../data/recipes.csv")
print(recipes.head(5))
