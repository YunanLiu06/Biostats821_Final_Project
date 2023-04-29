# A Flu Vaccinating Provider Data Library
This is the final project for Biostats821.

# Introduction
In the wake of the COVID-19 pandemic, the importance of vaccinations has been highlighted more than ever before. While much of the attention has been focused on the development and distribution of COVID-19 vaccines, it is important not to forget the importance of other vaccinations, such as the flu vaccine. In order to ensure that individuals have access to the flu vaccine, it is important to have a comprehensive list of flu vaccinating providers.

Creating a flu vaccine provider data library is one way to achieve this goal. In this project, we first utilized data from the CDC, including provider locations, websites, phone numbers, and so on, to create a database of flu vaccination providers in North Carolina. We then developed a user-friendly GUI for the data library, allowing people to easily access information on flu vaccination availability and provider information. By compiling this information into one place, individuals would be able to easily find providers near them, and healthcare organizations would have a more streamlined way to communicate information about the flu vaccine to their patients.

#### In the terminal, run `python database/main_GUI.py` to open the GUI.
<p align="center">
  <img width="500" height="200" src="https://user-images.githubusercontent.com/112578003/235311464-5c72362e-fa30-42f9-b937-8c77ac1a4d7b.png"
</p>

#### Choose a *vaccine name* and fill in *optional filters* to get relevent information about flu vaccinating providers.

* **Possible combinations of optional filters:**
1. No input in all filters : 
   
   Get the information of all locations by vaccine name
<p align="center">
  <img width="500" height="400" src="https://user-images.githubusercontent.com/112578003/235312264-bfb039a3-2913-4939-907c-7313789fb098.png"
</p>

2. `City of your location` : 

   Get the information of all locations by city and vaccine name
<p align="center">
  <img width="500" height="500" src="https://user-images.githubusercontent.com/112578003/235312369-4c9cff7f-d2fc-4993-ace1-370e434a092b.png"
</p>

3. `Number of locations needed` : 

   Get limited number(*the input number*) of information by vaccine name
<p align="center">
  <img width="500" height="400" src="https://user-images.githubusercontent.com/112578003/235312434-0809e346-9db8-4c9d-822b-d547040e4f30.png"
</p>   

4. `City of your location` + `Number of locations needed` : 
    
   Get limited number(*the input number*) of information by city and vaccine name
<p align="center">
  <img width="500" height="400" src="https://user-images.githubusercontent.com/112578003/235312469-3160b5d6-f3d4-4897-9c25-7dfae828cab5.png"
</p>   

5. `Latitude of your location`+`Longtitude of your location` : 

   Get the information of the nearest location by position *(the example shows the nearest provider to Duke University)*
<p align="center">
  <img width="500" height="300" src="https://user-images.githubusercontent.com/112578003/235312551-b4aea7fe-12bd-42af-a94e-5ee1ef3c4ba3.png"
</p>  

