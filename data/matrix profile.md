
```json
[

{
"velocity_raw": "23222",
"rain": "23232",
"level_raw": "23210",
"level_qaqc_flag": "55419",
"velocity_qaqc_flag": "55420",
"site": "8887",
"site_name": "NE003CAL_17",
"job": "18d3f4e7-1bac-48bf-b98a-48f00755bed9",
"pdepth": "23204"
},

{

"velocity_raw": "24130",

"rain": "23885",

"level_raw": "23483",

"level_qaqc_flag": "55425",

"velocity_qaqc_flag": "55426",

"site": "8935",

"site_name": "NE001CALa_17",

"job": "657e61b3-eb9e-4987-b9eb-7fa2fb858ff6",

"pdepth": "23480"

},

{

"velocity_raw": "8899",

"rain": "21765",

"level_raw": "6280",

"level_qaqc_flag": "55405",

"velocity_qaqc_flag": "55406",

"site": "6220",

"site_name": "NE015",

"job": "ad9b92f4-7613-4c5c-abd2-206661fb83a5",

"pdepth": "6274"

}

]
```



wget https://fw-data2-service-prod.carlsolutions.com/data/channel/8887-23222/data -O 8887_vel_raw.csv


wget https://fw-data2-service-prod.carlsolutions.com/data/channel/8887-23232/data -O 8887_rain.csv

wget https://fw-data2-service-prod.carlsolutions.com/data/channel/8887-23210/data -O 8887_level_raw.csv

wget https://fw-data2-service-prod.carlsolutions.com/data/channel/8887-55419/data -O 8887_level_qaqccsv


wget https://fw-data2-service-prod.carlsolutions.com/data/channel/8887-55420/data -O 8887_velocity_qaqc.csv


wget https://fw-data2-service-prod.carlsolutions.com/data/channel/8887-23204/data -O 8887_pdepth.csv