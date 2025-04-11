Iam policy - user based
resource based:
	- bucket policies
	- object access control list ACL
	- bucket ACL
	- principal IaM is allowed if its not stated or explicitly denied

bucket policies:
	- define which api calls are allowed to which group

EC2 instance access:
instance roles -> IaM permissions -> bucket

Cross-account access:
s3 bucket policy:
 allows cross-account


Block public access policies - the set of rules if they are ON they're stronger than any wrong set of rules at bucket level


