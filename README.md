# Recipecialist

This application is the project of _COMS4995 sec.009 **Data-Analytics Pipeline**_.

This product targets users who love foods and like to cook by themselves. Users can use their mobiles to take pictures of ingredients available at hand, and our application would recognize those ingredients. Based on the ingredients, the application would recommend corresponding recipes with such ingredients to users.

Below is the **minimum viable product** diagram of this application.

![Pipeline MVP and Big Picture](https://ws3.sinaimg.cn/large/006tNc79ly1g2sfhnzrc2j31t80ptgoy.jpg)



We provide two services in this MVP: **image recognition service** and **recommender service**.

After a photo has been uploaded to the app,  the **image recognition service** will recognize ingredients through a model trained using an image database. Then, the ingredients will be passed to the **recommender service** , which will use the recipe database to recommend recipes based on the ingredient recognized. 

We developed two versions throughout the project: the **remote** and the **local** version. The major difference lies in where the resources are stored and handled. 
   
- **Remote**
   - Uploads and stores images at s3
   - Uses Amazon Rekognition as model
      - Identifies multiple ingredients with confidence
   - Builds recipe database on Google Cloud
   - Provides direct search by typing in ingredients

- **Local (an earlier version)**
   - Uploads and stores images locally
   - Uses [TensorFlow for poets 2](https://github.com/googlecodelabs/tensorflow-for-poets-2) as model
      - Identifies a single ingredient
   - Builds recipe database at MySQL locally
   
- The following section is a simple demonstration of the remote version.

## Running the app

- Run

   ```python
   python src_remote/app.py
   ```

- Open a browser and nevigate to `0.0.0.0:7777`. An index page with instructions will show. 

### Get recommendation by uploading photo
- Upload a photo and click the button.
<img src="https://github.com/lullaby1024/Pipeline_Project/blob/master/demo/MVP_v2/index_page.png" width="70%">

   - The uploading service is handled by `UploadHandler()`. If the file is successfuly uploaded, a message will be sent.
   <img src="https://github.com/lullaby1024/Pipeline_Project/blob/master/demo/MVP_v2/upload.png" width="60%">

- Enter `0.0.0.0:7777/recommend` in the address bar. This will trigger the `MainHandler()` to call the model with the given image and return recommended recipes.

<img src="https://github.com/lullaby1024/Pipeline_Project/blob/master/demo/MVP_v2/recommend1.png" width="40%">
<img src="https://github.com/lullaby1024/Pipeline_Project/blob/master/demo/MVP_v2/recommend2.png" width="80%">

### Get recommendation by typing ingredients
- Type in the ingredients in the search box (separated by ",") and click the button. 
<img src="https://github.com/lullaby1024/Pipeline_Project/blob/master/demo/MVP_v2/index_text.png" width="40%">

- The `SearchHandler()` will handle the query request and return the results in the same window.
<img src="https://github.com/lullaby1024/Pipeline_Project/blob/master/demo/MVP_v2/search.png" width="80%">

## Contributors

[Qi Feng](https://github.com/lullaby1024) (Product Manager)    

[Zoha Qamar](https://github.com/zohaqamar)    

[Ze Chen](https://github.com/mandychenze)    

[Weiyang Gu](https://github.com/WeiyangGu)     

[Chunran Yao](https://github.com/YLDAPhoenix11)     

Check Our [JIRA](https://toydemoproject.atlassian.net/secure/Roadmap.jspa?projectKey=REC&rapidView=16)!
