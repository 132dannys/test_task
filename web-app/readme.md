## Web application, which get info about product in marketplace Wildberies by vendor code.

## Setup

- docker-compose build
- docker-compose up

To Run Tests:
- make container-shell
- pytest

Application will be avaible at this URL: 127.0.0.1:8000/api/v1/vendor-codes/
- for input API accept vendor code or .xlsx file with vendor codes in first column(like test.xlsx in main folder).
