things to tuch during the meeting

* 53% missing values for energy demand and consumption
* 1st step data resampling -> 10 minutes data (from 1/3/4 minutes series): after this step lacking data is 26%
* 2nd step filling data using logic - >  after this step 7% missing data
	* eg.. the previous and next demand value is 0 and consumption is not rising means heater is OFF so actually it's in OFF mode so DEMAND and CONSUMPTION remains the same
* 3rd step -> after this step 0.28% missing : ML model to fill the data
	* 0.28% still missing: usually it's last hour during the day( prediction so we left it for final solution)


output dataset: final.csv

reports:
1_raw - raw data from Hilo  
2_processed - preeliminary cleaning and consolidation to 10 minutes signals
3_filled - filling missings with logic rules
4_final - filling missing with AI


logic filling:
def initial_filling(df):

"""Using logic and industry knowledge to fill missing anomalies

OFF -> previous tstat_daily_consumption, if does not exist then 0 and tstat_heat_demand = 0

turning on/off -> previous tstat_daily_consumption, if does not exist then 0 and tstat_heat_demand = 1

wrong_reset_time -> tstat_heat_demand = 0, if consumption missing then 0

both missing -> previous tstat_daily_consumption, if previous if OFF then demand = 0, anomaly = OFF

If whole day has only NaNs -> switched OFF whole day and demand = 0, consumption = 0

If first value of a day missing -> demand = 0, consumption = 0

If consumption is 0 and demand missing -> demand = 0