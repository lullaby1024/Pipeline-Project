# Recipecialist

## Demo Implementation
-----------------------  
First, run
```
python app.py
```

Next, open a browser and nevigate to `0.0.0.0:7777`. An index page with instructions to upload the ingredient photo will show. Upload a photo by clicking on the button.

<img src="https://github.com/lullaby1024/Pipeline_Project/blob/master/demo/MVP/index_page.png" width="60%">

Here we tested a simple photo of tomatoes. 

<img src="https://github.com/lullaby1024/Pipeline_Project/blob/master/demo/MVP/tomatoes.jpg" width="40%">

The uploading service is handled by `UploadHandler()`. If the file is successfuly uploaded, a message will be sent. 

<img src="https://github.com/lullaby1024/Pipeline_Project/blob/master/demo/MVP/upload.png" width="60%">

Enter `0.0.0.0:7777/recommend` in the address bar. This will trigger the `MainHandler()` to call the model with the given image and return recommended recipes.

<img src="https://github.com/lullaby1024/Pipeline_Project/blob/master/demo/MVP/recommend.png" width="90%">

## Related Links
[JIRA Roadmap](https://toydemoproject.atlassian.net/secure/Roadmap.jspa?projectKey=REC&rapidView=16)
