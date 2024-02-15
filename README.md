# API-PILPRES-2024
 Unofficial API untuk Mengambil Data Pilpres 2024, made in like 10 minutes

 ![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Falunit3%2FAPI-PILPRES-2024&label=Visitors&countColor=%23263759&style=flat-square&labelStyle=upper)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/alunit3/API-PILPRES-2024.git
   ```
2. Install the requirements
   ```sh
   pip install -r requirements.txt
   ```
3. Run the api server
   ```sh
   uvicorn main:app
   ```
4. url endpoint
   ```sh
   http://127.0.0.1:8000/all
   ```


### Data returned structure

```json
{
  "last_updated": "2024-02-15 18:00:23 WIB",
  "paslon_1": 123,
  "paslon_2": 123,
  "paslon_3": 123,
  "percentage": 99.99,
  "wilayah_data": [
    {
      "wilayah": "nama wilayah",
      "paslon_1": 123,
      "paslon_2": 123,
      "paslon_3": 123,
      "percentage": 99.99,
      "status_progress": true
    }
  ]
}
```
