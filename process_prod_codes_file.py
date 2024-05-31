import csv
import os.path


def process_google_prod_codes(file_name: str) -> list[tuple]:
    prod_codes = []
    with open(file_name, 'r') as f:
        for prod_line in f:
            # get rid of comments
            if prod_line.startswith("#"):
                continue
            # process only those lines that have 4 fields - take the first field (#id and the last one, the name)
            # log.warning(l)
            code, rest = prod_line.strip().split(" - ")
            fields = rest.split(">")
            if len(fields) == 5:
                prod_codes.append((code, fields[-1].strip()))
    return prod_codes


def generate_csv_list_of_prod_categories(product_categories: list, file_name) -> None:
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(product_categories)


# the code assumes that Google's product taxonomy file is downloaded in data subfolder
if __name__ == '__main__':
    in_filename = os.path.join("data", "taxonomy-with-ids.en-US.txt")
    out_filename = os.path.join("data", "prod_categories.csv")
    categories = process_google_prod_codes(in_filename)
    generate_csv_list_of_prod_categories(categories, out_filename)
