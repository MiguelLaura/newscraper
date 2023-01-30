# Newscraper

Some yaml files to use with `minet scrape`

## For radiofrance:
`minet fetch url input_urls.csv | minet scrape radiofrance.yml > scraped.csv`  
where input_urls contains urls of the type https://www.radiofrance.fr/personnes/name-of-the-person?p=page-number.  
To add the radio name, use the add_radio python function.

## For liberation:
`minet fetch https://www.liberation.fr/auteur/name-of-the-person/ | minet scrape liberation.yml > scraped.csv`
