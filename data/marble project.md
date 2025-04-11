
- [ ] work on project template similar to my snippet template
GREG goal: 

- the key sheet that summarizes tasks and provides a amount for these tasks is \  “Project  Fixed Costs” in the “Marble Estimation Planning” spreadsheet. 
  This spreadsheet was in response to the RFP by a potential vendor.  
  
  We need to ensure that:
- We are capable of providing the items listed
- Any deficiencies or obstacles we have are highlighted for us to review with the client – and – if necessary request additional resources
- We can provide an estimate of the number of months it would take to perform these tasks
- We have a means (ie Face Pro, Ace) of delivering the model results similar to what the respondents of the RFP have proposed (amazon Sagemaker)
- Upon your review of the RFP and response, we have a list of questions (if applicable) to ask the client prior to entering into an agreement


project plan:

docs:
https://www.inverite.com/documentation/#section/Introduction
Marble has 2 models:
- categorization
- risk 
the goal of the project:
- retrain current models
- create new models
todo
- [ ] decompose it to points and than estimate points based on notebooks 2023-11-13

#### my first comments

introduction: https://infomarblefinancial-my.sharepoint.com/personal/estelle_lheureux_marblefinancial_ca/_layouts/15/stream.aspx?id=%2Fpersonal%2Festelle%5Flheureux%5Fmarblefinancial%5Fca%2FDocuments%2FRecordings%2FMarble%20Demo%2D20231025%5F080720%2DMeeting%20Recording%2Emp4&ga=1&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview

- [ ] put it into project form

model in Cleo : T5 for embeddings 
E5 is free and better https://medium.com/@kelvin.lu.au/hosting-a-text-embedding-model-that-is-better-cheaper-and-faster-than-openais-solution-7675d8e7cab2

cleo presentation
[https://datasciencefestival.com/session/large-language-models-for-understanding-personal-finance/](https://datasciencefestival.com/session/large-language-models-for-understanding-personal-finance/ "https://datasciencefestival.com/session/large-language-models-for-understanding-personal-finance/")

kaggle example:
https://www.kaggle.com/datasets/zekaili/bank-transactions/code




- they have a pickle file which they deploy to production
	- there must be a deployment script somewhere?
- they don't know what is the relationship between notebooks / our sources and prod env. - we need to find out what exists and how to manage it
	- question to Rick - does he know the relationship and help us to make sure we won't destroy something


- we're looking for better validation -training ratio for 1st model - we have hundreds of  thousands of data for train and only 1000 for validation we have 98% validation accuracy and 80% training accuracy
- we need new 3rd party data ( yellow pages etc) 
- we need new transactional data - ask them for this!!!

to consider  as potential dataset ( Greg shared with us)
[Financial Data | Yodlee](https://www.yodlee.com/financial-data "https://www.yodlee.com/financial-data")

our goal: validation - trying to understand the bias and find ides for improvement

- to check - folding dataset again to different train-test sets and measure accuracy differently

my goal - try to setup proppper env with requirements as on their production.



-------------------
agenda for the meeting 20 May ->

- Provide overview of our findings to date regarding external classification sources to provide new "source of truth" in order to improve results from current model.
	- List sources
		- 3rd party "black box" solutions
			- TODO - list services tested by Gustavo
		- LLM's
			- chatgpt 4 - almost 100% fine ( some discrepancies in multi level categories ) 
			- offline LLM's models
				- Mistral - mostly wrong
				- OpenChat - mostly right (properly detects income)
					- only one to identify debt collection INTERNET DEPOSIT FROM TANGERINE SAVINGS ACCOUNT - MONTHLY DEBT REPAYMENT -,transfer,bills_and_utilities,fees_and_charges/collections_agency
				- phi3 - mostly wrong
-- done with short comment Approximate accuracy or general consistency across results
-- no idea about 3rd party services -but don't think it's even worth checking Provide costs for using each (based on a set volume)

TODO - show possible difference between chat4 and gemini or self-hosted openchat if only income is acceptable or using chat4 once for training set and than only elastic self hosted - need additional time to test this approach

- I think that if chat4 is acceptable for now - we need to deploy categorisation differently - need to deploy another kind of lambda service in AWS which is going to keep the context of chatgpt query 
- once chatgpt prediction service is deployed, it's queried the same way as previous categorisation service and it's going to reply with an old list of categories
  Service calls indirectly chatgpt service so it's going to be automatically updated once the version of chat is updated. 
	  - if we want to introduce feedback loop - we need additional service deployed to AWS - client is going to ingest manual category mappings through this service if needed ( feedback )

- Discuss who at Marble will determine categories (as we will need to verify results of new model as well as provide any new categories)

 - What impact does/will introducing new categories have on the current model? 
	 - needs futrther investigation 
- Discuss who at Marble will be responsible for spot checking accuracy of the chosen third party data source
- Once Marble decides which direction to go we may provide date where new model + documentation on how to use will be available
- Request data on loan defaults for building risk score model 
 - Once we have specs for new Risk model we may be able to provide timeline for delivering new risk score model - current risk score will work out of the box with new categorisation service 

