#! python3
# removeCsvHeader.py - Removes the header from all CSV files in the current
# working directory.
import csv, os

for csvFilename in os.listdir('./BeforeRemove'):
    if not csvFilename.endswith('.csv'):
        continue
    print('Removing header from ' + csvFilename + '...')

    # Read the CSV file in (skipping first row).
    csvRows = []
    csvFileReader = open(os.path.join('./BeforeRemove', csvFilename))
    readerObj = csv.reader(csvFileReader)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue  # skip first row
        csvRows.append(row)
    csvFileReader.close()

    # Write out the CSV file.
    csvFileWriter = open(os.path.join('./AfterRemove', csvFilename), 'w', newline='')
    csvWriter = csv.writer(csvFileWriter)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileWriter.close()
