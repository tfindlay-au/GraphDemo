# Graph Demo
Purpose: This repository captures some sample ideas shared for the Melbourne Data Eningeering meetup.

##### Generator.py
Generates a CSV file on disk. This is slow due to the use of names()

##### Inserter.py
This uses the PyArango package to programmatically insert a single document at a time.
This is extremely slow and should be for demonstration purposes only.

##### BulkLoaderWrapper.sh
This shows the use of supplied ArangoDB client tools arangoimp as a high performance data loading tool