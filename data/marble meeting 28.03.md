
- input for PP presentation - steps we did
	done:
	- matched the production classifier model with the proper source code
	- documented classifier model
	- identified original train and validation dataset
	- built new classifier from source
	- validated new classifier on original dataset
	- prepared docker that matches risk os and Python environment
	in progress:
	- testing for better train / validation set ( accuracy on train and validation )
	- exploration of classification results
	- looking for improvements in the model
- issues / obstacles: 
			- dependencies both Python and os to run the model in isolation
			- hardware scaling
----
data question:
 we assume there is work in progress on production AGP dataset - 
 Where does the category field in AGP dataset come from? - is this and output of our classifier?
 How we can validate the value of this field? At least for a subset of production dataset ...

In order to use new datasources we need to:
- understand new requirements for classifier
- understand what are the 3rd party sources available 
- what was the process behind 3rd party data sources until now and how it's managed

