Hi Piotr,

*For the seasonal component, typically people heat only about half the year or a bit more, and we haven’t seen any clue of having a seasonal aspect to anomalies. They seem to be more happening once in a while during the heating season, from what we know it can be connectivity issues, which are not seasonal.*

Seasonality I was referring to is related to our goal of predicting proper values instead of anomalous
- in timeseries data  we can model different levels of seasonality - for example hourly / daily / weekly / monthly/ yearly 
	-> the shorter period of time we have for training the lower seasonality we can uderstand and as a consequence we have worse prediction
	
*What number of clients would be statistically significant for you?*

It depends on the total number of devices you have and how many of them have anomalous reads. 
For example: 
You have 1000 deviceids and for 500 you observe anomalies.
Ideally we'd like to have data for at least 278 devices.

*The meter data we shared with you comes from our employees with the solution, but other than that they can be considered randomly selected.*

I need randomness in order to have the same proportion of anomalous timeseries in the dataset you give me as you have in the whole population. 
For example: 
You have 1000 deviceids and for 500 you observe anomalies 
You give us a sample dataset from 280 devices

-> deviceid were randomly selected means that in the sample there is around 140 anomalous devices 
If for some reason you cannot randomly select devices ( selecting your employees is not a random trial ) please assure that you keep the same proportion of anomalous devices (140 in 280)

additionally I'd like to clarify:
*anomalies are gaps in the data when communication was broken ...*

By gaps you mean gaps in column tstat_daily_consumption or in the entire row?


Thanks,
piotrs