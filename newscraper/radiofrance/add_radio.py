import csv

def add_radio(input, output):
    with open(input, "w") as new:
        writer = csv.writer(new)
        writer.writerow(["url", "categorie", "titre", "date", "radio"])
        with open(output, "r") as f:
            reader = csv.DictReader(f)
            for line in reader:
                writer.writerow([line["url"], line["categorie"], line["titre"], line["date"], line["url"].split("/", 2)[1]])