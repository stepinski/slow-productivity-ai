lime and shap are the way to explain ml models
its related to explainability
SHAP is a way to explain locally indifidual predictions
it says how each feature contributes to this particular predictions ( not the same as feature importance which is global)
for instance if we predict bonus for employee using age, title, years of experience from SHAP we can see something like:
E[X] - expected value of bonus ( mean bonus) 150 is contributed by title +30, experience +130, age -10

lime - is another way for local explainability - means local interpretable model agnostic explanations
for instance we may predict negative or positibve emotions from text - we identify which words in sentence mostly contributed to sentiment prediction
if we have non linear classification model - diabets / nondiabets -> we focus on particular prediction - looking for nearest neighbourhood and than we build simple model ( logistic regression) in this neighbourhood - we have n variables for regression and we fit their weights - thats where we get importance of each variable for this individual prediction

****