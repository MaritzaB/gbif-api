from pygbif import species as species
from pygbif import occurrences as occ
from pygbif import datasets as ds

import pandas as pd

species_name = "Phoebastria immutabilis"

# Get the species key
species_key = species.name_backbone(species_name)["speciesKey"]
print(f"Species key: {species_key}")

# Get the occurrence data
occurrences = occ.search(taxonKey=species_key, hasCoordinate=True, year=2023, limit=1000)
## Convert the occurrences to a pandas DataFrame
occurrences_df = pd.DataFrame(occurrences["results"])

# Clean columns
columnas_a_conservar = [
    'year', 'month', 'day', 'eventDate',
    'dateIdentified', 'decimalLatitude', 'decimalLongitude', 'coordinateUncertaintyInMeters',
    'stateProvince', 'gbifRegion', 'country'
    ]
df = occurrences_df.drop(columns=[col for col in occurrences_df.columns if col not in columnas_a_conservar])

print(df.head())
print(df.shape)

# Save the DataFrame to a CSV file
#df.to_csv("occurrences.csv", index=False)
