import csv

def add_base_url(input, output, base_url):
    with open(input, "w") as new:
        writer = csv.writer(new)
        writer.writerow(["url", "categorie", "titre", "date", "radio"])
        with open(output, "r") as f:
            reader = csv.DictReader(f)
            for line in reader:
                writer.writerow([base_url + line["url"], line["categorie"], line["titre"], line["date"], line["url"].split("/", 2)[1]])