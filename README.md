# Python-Assessment

## Implement backend code for the following problem statements :
### Problem 1 :
- Write a method that reads phone book records from a CSV or JSON file.
- Each record consists of the following parameters Name, email, Phone 1, Phone 2.

### Problem 2 :
- Implement a SQL-like parser for phone book records in Problem 1 to implement CRUD operations and print SQL like output on console.:
   1. SELECT * FROM phone_records; This statement reads the first 10 records and displays them on the console.
   2. SELECT * FROM phone_records WHERE name=’doe’; 
   3. INSERT INTO phone_records(name, email,phone 1, phone 2) VALUES(‘Test’,’test@test.xtyz’,’1234456’,’1233233’)
   4. DELETE FROM phone_records WHERE name='John'.

**Dataset as CSV And Json :** [CSV](https://raw.githubusercontent.com/Vengatesan-K/Python-Assessment/main/Dataset/phone_book.csv) & [JSON](https://raw.githubusercontent.com/Vengatesan-K/Python-Assessment/main/Dataset/phone_book.json)


### Approach :
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://python-assessment-jw6edtphrryda4fj5grwby.streamlit.app/)

> - Open the Application using above Streamlit Icon/Button or using [Application](https://python-assessment-jw6edtphrryda4fj5grwby.streamlit.app/) link.
> 
> - Then You can preview the Uploader in Task1 Page, Upload Any Csv File/Json File to read.
> 
> - And Switch to Task2 Tab for Uploading Files Of CSV/Json to Execute Query (CRUD Operations)
> 
> - After Upload file a file, Select query to apply on Dataset
> 
> - There are 4 queries to parsing dataset 
