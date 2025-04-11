Infinity Forecasting solution is delivered in 3 modules: 

- predictive model deployed to ACE platform 

maybe here we can put few ACE screenshots? 

- predictive API 

- forecasting dashboard 

data sources: 

- depth data from sanitation districts  

- rainfall data 

- gis layer  

=> weather forecast data - we need the weather forecast data to get predictied flow from the model for future rainfall 

- predictive model 

- predictive model needs to be fitted based on flow data from sanitation districts and rainfall data  

- based on modeled relationship it produces forecasted flow based on forecasted rainfall data 

- predictive API 

- model output is translated to JSON API 

- forecasting dashboard is loaded by predictive API: 

- we need to be able to join flow data with GIS layer features in order to present predicted flow on the map 

- configurable : 

- the feature that we want to show on the map with colour and geometry 

- layer popup contents 

- forecasting step (depends on what makes sense ( 2 hours vs 1 week) and what rainfall forecast is available 

- colours and geometries to presentI 

Assumptions: 

- Depth time series are strongly correlated with rainfall data 
    
- We have a good quality rainfall forecast which is also strongly correlated with rainfall data 
    
- We have a gis layer with features related to depth data (reference id)