Toronto project phase 3
Goal: 
predict the pipe level for selected Toronto sites based on historical channels data and future rain prediction.
hypothesis: we are able to predict the pipe level based on past pipe level, rain and any other available historical data with accuracy 60% or better.


Step A: simple model
	1. EDA of current FW data
	2. match forecast api
	3. evaluate base models (used in previous projects)
[1.5 sprint]

	outcome: 
	- forecasting model 
	- directions for improvement of he model or for client what data we need to start collecting
	- large project scope ( with data that we don'e know yet /  accuracy we want to agree on / predictions frequency / granuality

Step B: final model
	1. EDA for new dataset and forecast data [1 sprint]
	3. modelling phase -  features engeneering / model tunning until reaching  forecasting accuracy from hypothesis in phase 1 
		developement: [2 sprints ]
		evaluation (feedback loop): [2 sprints]

	outcome:
	- selected forecasting model with expected accuracy

Step C: Run selected model  in Tesler [1 sprint]
	1. Tesler deployment
	
	outcome:
	- models sheduled in Tesler 
	- tests and bugfixing

overall cost:  
7.5 sprints for all
1.5 sprint for small project