# Recipecialist

This application is the project of _COMS4995 sec.009 **Data-Analytics Pipeline**_.

This product targets users who love foods and like to cook by themselves. Users can use their mobiles to take pictures of ingredients available at hand, and our application would recognize those ingredients. Based on the ingredients, the application would recommend corresponding recipes with such ingredients to users.

Below is the **minimum viable product** diagram of this application.

![Pipeline MVP and Big Picture](https://ws3.sinaimg.cn/large/006tNc79ly1g2sfhnzrc2j31t80ptgoy.jpg)



We provide two services in this MVP: **image recognition service** and **recommender service**.

After a photo has been uploaded to the app,  the **image recognition service** will recognize ingredients through a model trained using an image database. Then, the ingredients will be passed to the **recommender service** , which will use the recipe database to recommend recipes based on the ingredient recognized. 

We developed two versions throughout the project: the **remote** and the **local** version. The differences lie in where the resources are stored and handled. 
   
- **Remote**
   - Uploads and stores images at s3
   - Uses Amazon Rekognition as model
      - Identifies multiple ingredients with confidence
   - Builds recipe database on Google Cloud

- **Local (an earlier version)**
   - Uploads and stores images locally at './uploads/'
   - Uses [TensorFlow for poets 2 as model](https://github.com/googlecodelabs/tensorflow-for-poets-2)
      - Identifies a single ingredient
   - Builds recipe database at MySQL locally

## Running the app (remote)

1. Run

   ```python
   python app.py
   ```
   
2. Open a browser and nevigate to `0.0.0.0:7777`. An index page with instructions to upload the ingredient photo will show. Upload a photo by clicking on the button.

3. Enter `0.0.0.0:7777/recommend` in the address bar. This will trigger the `MainHandler()` to call the model with the given image and return recommended recipes.

## Running the app (local)

1. Run

   ```python
   python app.py
   ```

2. Open a browser and nevigate to `0.0.0.0:7777`. An index page with instructions to upload the ingredient photo will show. Upload a photo by clicking on the button.

   <img src="https://github.com/lullaby1024/Pipeline_Project/blob/master/demo/MVP/index_page.png" width="60%">

   Here we tested a simple photo of tomatoes.

   <img src="https://github.com/lullaby1024/Pipeline_Project/blob/master/demo/MVP/tomatoes.jpg" width="40%">

   The uploading service is handled by `UploadHandler()`. If the file is successfuly uploaded, a message will be sent.

   <img src="https://github.com/lullaby1024/Pipeline_Project/blob/master/demo/MVP/upload.png" width="60%">

3. Enter `0.0.0.0:7777/recommend` in the address bar. This will trigger the `MainHandler()` to call the model with the given image and return recommended recipes.

   <img src="https://github.com/lullaby1024/Pipeline_Project/blob/master/demo/MVP/recommend.png" width="90%">

## Contributors

[Qi Feng](https://github.com/lullaby1024) (Product Manager)    

[Zoha Qamar](https://github.com/zohaqamar)    

[Ze Chen](https://github.com/mandychenze)    

[Weiyang Gu](https://github.com/WeiyangGu)     

[Chunran Yao](https://github.com/YLDAPhoenix11)     

Check Our [JIRA](https://toydemoproject.atlassian.net/secure/Roadmap.jspa?projectKey=REC&rapidView=16)!
