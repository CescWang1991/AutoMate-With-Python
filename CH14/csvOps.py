import csv

EdgeListFile = open('edgelist_Okt-Des_2016.csv')
EdgeListReader = csv.reader(EdgeListFile)
EdgeListData = list(EdgeListReader)
print(EdgeListData[0])
print(len(EdgeListData))

outputCsvFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputCsvFile)
for lineNum in range(10):
    outputWriter.writerow(EdgeListData[lineNum])

outputTsvFile = open('output.tsv', 'w', newline='')
outputWriter = csv.writer(outputTsvFile, delimiter='\t', lineterminator='\n\n')
for lineNum in range(10):
    outputWriter.writerow(EdgeListData[lineNum])

outputTsvFile.close()
outputCsvFile.close()
EdgeListFile.close()
