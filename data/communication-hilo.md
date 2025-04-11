draft of Hilo comunication history

- technical meeting with Hilo at

outcomes:


Hello Piotr,

Sorry for the late reply. I’ll answer as best I can as Ahmed is gone on vacation.

1.  It is not a field that is being populated anymore, please disregard it.
2.  Tstat_heat_demand represents the % of the demand of a thermostat. It’s the % of capacity that is being used at that point in time.
3.  We have put the weather temperature in the last two columns, if that’s why you want the geolocation. You can assume they’re all in the greater Montreal area.
4.  The goal of the anomaly detection is to correct errors in the data. We can have situations where communication is disconnected between thermostat and hub, and we would like to be able to a) detect it and b) correct the data.
5.  I do not have labels that clearly identify the anomalies. We mostly see two kinds :

1.  the cumulative energy consumption (tstat_daily_consumption) should reset at midnight (5 :00 UTC) and sometimes sets back to zero at other times of the day, or multiple times a day),
2.  sometimes there are gaps in the data if communication was broken. However since communication with thermostats is limited to only when they are working, it’s hard to tell if a lack of data is due to it being off or an anomaly.

7.  Right now we are not looking for predictive, but we would like it to be as near real-time as possible as we evolve and use the data for more actionnable purposes. To start with, correcting in the hour following might be enough.
8.  As of now, since we have a limited understanding of the amount of anomalies really happening (for gaps for example), it’s hard for us to put a metric on the improvement. We would need some help in quantifying the occurrence of anomalies to start with. In terms of accepted errors, again we do not have a set number in mind, but we do have some degree of tolerance, at least at first, since we do not have functions using directly this data yet. We plan on exposing the data to the end customer eventually to help them manage their bill for instance, but it’s not used in billing. I’m not sure how you formulate the recall-precision trade-off, since we’re dealing with gaps a lot more than with false values.
9.  I am not sure I understand what you mean by this question. All our data has not been labeled for anomalies. If it’s necessary for this pilot we could try to sub-measure thermostat consumption somehow but we are not equiped for that at the moment.

I hope this helps, please reach out to me if you need more explanations.

Best regards,

Odile

questions after receiving 1st dataset:
1. Is there a way to share with us more geo information locations? (address / zip code / latlon ) ?
2. if there is no geolocation possible we can try to find this by clustering



Thank you for your answers. It helps a lot.
Regarding geolocation we thought it might be additional to temperature feature that explains anomalies. The intuition behind it is that maybe anomalies are lakely occurring in similar location in time - the same might work for non anomalous data as well.
If there are any problems with getting exact locations maybe rounding to certain decimal point might be solution or we can at least know the area of the city / district ? 


David D points:
-   Define and create the MVP in concept form
-   Based upon the conceptual MVP we prepare a workplan and timetable for the entire process with Hilo
-   Define success for Hilo and how they scale the solution
-   A proposal is packaged with the above information and presented to Hilo for their approval and contract signoff
-   Build the MVP

[[hilo mvp]]


additional question:
- how shall we interpret the situation when we have several deviceids for one location id in the same time range?
- ask for data for 15 locations and 1 year
- phase 1 we focus on NaNs - we classify NaNs trying to figure out which are correct and which are anomalous
- include deviceid matching part of the project
- try to evaluate data hilo in julia -> figure out if we have several deviceids for the same time for longer period of time - if it happens after midnight  reset



- For every unique location_id there is one device_id that has different properties than the others: it is a lower number and readings are not that often. Is there a reason for that behavior? Is it like a specific kind of device?

- Do we have an exact number of devices that work within given location_id?

- If tstat_daily_consumption does not rise, does it mean that the device could be turned off?

- If there are multiple working thermostats (device_ids) under one location_id, should we interpret it as multiple clients in one location (area) or multiple thermostats of one client?

- If a client switches off the thermostat, for how long usually it is turned off compared to an anomaly? Is it possible to distinguish it? (e.g. client switching for a weekend vs anomaly for few hours)

- When device_id changes (when the connection to a gateway was reset) does it mean that it was turned off by the client or the power was down suggesting there could have been an anomaly?



mail to Odile


Hello Odile, 
We think that in your data the seasonal component might be important in modeling so for the next phase of the project ideally we'd need a dataset of at least 1 year of data. Also we'd need a number of clients s statistically significant and irandomly selected  where proportion of anomalous data to correct data is similar as in the whole population.
Additionally I'd like to share with you few unknowns that we still have after initial exploration:
-   For every unique location_id there is one device_id that has different properties than the others: it is a lower number and readings are not that often. Is there a reason for that behavior? Is it like a specific kind of device?  
-   Do we have an exact number of devices that work within given location_id?   
-   If tstat_daily_consumption does not rise, does it mean that the device could be turned off?  
-   If there are multiple working thermostats (device_ids) under one location_id, should we interpret it as multiple clients in one location (area) or multiple thermostats of one client?  
-   If a client switches off the thermostat, for how long usually it is turned off compared to an anomaly? Is it possible to distinguish it? (e.g. client switching for a weekend vs anomaly for few hours)   
-   When device_id changes (when the connection to a gateway was reset) does it mean that it was turned off by the client or the power was down suggesting there could have been an anomaly?

best, piotrs