there is a problem in tesler design:
-  for pstepinsky it takes eternity to reload files when switching assets
- scenario when I create template-bundle example shows how it's counterintuitive to use tesler as after creating template you need to scroll to top to swithc to bundle list and than create it in table - there is no simple way to execute template
- after execution of bundle there is no simple way to see the log and edit the script - it should be possible to edit but with information that it happens at template level
ideas:
- edition of scripts everywhere but with info that it's located at template
- run button in template if there is no way to edit things at bundle level
- simple switch between template-bundle-logs\
- editor tool must be able to show text and other output
- add capability to show visual output https://www.npmjs.com/package/react-viewer
- add capability to visualize jupyter notebooks
- need to check kedro pipeline to kubeflow
	- https://towardsdatascience.com/kedro-a-python-framework-for-reproducible-data-science-project-4d44977d4f04
	- https://github.com/getindata/kedro-kubeflow
	- https://neptune.ai/blog/data-science-pipelines-with-kedro