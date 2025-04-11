how readily service is 
- dependent on storage class
	- s3 standard not available 53 minutes a year 99.99% availability
		- low latency high throughput
		- frequently accessed data
		- big data gaming etc
	- inrequent access
		- standard IA  99.9 av
			- backups, recov
		- one zone-IA
			- 99.999999999 % durability in single AZ until AZ is desttroyed
			- 99.5% availability
			- second backups
	- glacier - backups/ archiving
		- price for storage + retrieval cost
			- Instant retrieval
				- milsec ret, quarterly access
				- min storage 90 days
			- glacier flexible retrieval
				- expedited ( to 5 minutes) / standard ( 3-5 hours) /  bulk (5-12 hours) - free
				- min storage duration 90 days
			- glacier deep archive
				- standard (12 hours) bulk (48 hours)
				- min storage duration 180 days
s3 intelligent tiering:
auto FA tier - default 
auto IA -> after 30 days
auto archive IA -> after 90 days
(optional) AA -> config 90-700+ days
(optional ) deep AA -> config 180-700+ days

