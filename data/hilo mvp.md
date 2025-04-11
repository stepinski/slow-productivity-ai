
MVP:
steps to build:
1. testing unsupervised approach for anomaly detection
2. get feedback from client in order to have common understanding of: (~2hrs)
	-  What is the performance of selected model
	- What more we know about the process that we model after this task 1 :
		 - intuition that temperature is an important factor that explains this phenomena
		 - intuition that location is important
	- indentify the way we measure performance of this :
		 - the amount of NaNs discovered by our model
		 -  the amount of NaNs wrongly classified
		 - the amount of non NaNs classified as anomalies - WHY?
		 - identify FN and FP ,TN and TP - understand how we classify them
3. Predicting values for anomalous periods
	 - Test our multivariate models for signal prediction for the data classified as non anomalous - hypo: we can find a model with RRMSE <30%
	 - Select the best model and evaluate RRMSE for known values
	 -  get feedback from HILO 
		 - WHAT is their opinion on selected metric
		 - WHAT are their comments on predicted data
		 - WHAT are their suggestions/comments for improvement

4. Implement the 2 models in Tesler

estimation:
- 2,5 sprints for 1st model
- 1 sprint for feedback adoption
- 1 sprint for predictive model
- 1 sprint for changes after feedback