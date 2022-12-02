# Parsing multiple json files
Parsing 820,000+ json files to find 5000+ missing information (SIC code) in our database

## Removing unwanted files in the submission zip file
After extracting, we need to removed some additional files that we don't need. 
<br>
Example include "CIK0000001750-submissions-001.json"

```bash
mv *submissions*.json /mnt/d/Documents/CIK
```

## Converting desired output into a text file

```bash
python3 parse_json.py >test_output.txt
```


## List of files and its uses
- ### comp_sec_id.csv 
List of companies that we would like to find SIC code

- ### parsed_sic.txt
Result of parsing with the following order of format: 
1. SEC/CIK
2. SIC
3. Industry Category by SIC
4. Name of Company

# Source
- [Edgar Dataset Download](https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip)

- [Edgar Database Documentation](https://www.sec.gov/edgar/sec-api-documentation)
