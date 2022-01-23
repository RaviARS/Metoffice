# Metoffice

## UK weather climate information

## Farmsetu

### To run Django Project

- Step 1:  To install all python's library run the below command

        pip install -r requirement.txt

- Step 2: To create a tables (collections)  with sqlite run the below migrations command

        python manage.py makemigrations
        
        python manage.py migrate
        

- Step 3: To run Django server (open new terminal)

        python manage.py runserver

- Step 4: To view Django API GUI type below url to your browser

       http://127.0.0.1:8000/api/v1/climate/
       
  - Note :
    - List of endpoints.
  
          Method allowd : [POST]
    
          URL : http://127.0.0.1:8000/api/v1/climate/
    
          Request Payload :
            {
               "order_by": "string",
               "region": "string",
               "parameter": "string"
            }
    
            Allowed value:
    
            order_by = ("ranked", "date")
    
            region = (
            "UK", "England", "Wales", "Scotland", "Northern_Ireland", "England_and_Wales", "England_N", "England_S",
            "Scotland_N", "Scotland_E", "Scotland_W", "England_E_and_NE", "England_NW_and_N_Wales", "Midlands",
            "East_Anglia", "England_SW_and_S_Wales", "England_SE_and_Central_S")
            
             parameter = ("Tmax", "Tmin", "Tmean", "Sunshine", "Rainfall", "Raindays1mm", "AirFrost")
      
              Sample payload
              {
               "order_by": "date",
               "region": "UK",
               "parameter": "Tmax"
              }
          
              Using the climate api we can get the weather and climate data from metoffice,
              if order_by is "date" it will be genrated the csv file (Path: Metoffice/farmsetu/weather_report) 
              andpapulated the weather data into csv file.
              if order_by is "ranked" only it will generated the csv file but not papulated the data into database 
      
          Weather API:
    
              URL : http://127.0.0.1:8000/api/v1/weather/   ,  Methd allowd [GET, POST]
              URL : http://127.0.0.1:8000/api/v1/weather/id ,  Methd allowd [GET, PUT, DELETE]

        - Sample endpoint screen capture attached in the screenshot directory  
      
        - Needs to be Done
              Implement Auth model
              Add Logging to this application
              Add Validation
              Add Weather by ranked Database model
              Improve the ReadMe file 
        
