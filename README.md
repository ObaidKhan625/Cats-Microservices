# Cats Microservices

• A tiny little project I made to implement some backend concepts, delve into docker concepts like networking and show my love for cats😺.<br>
• I have created 4 seperate microservices, 3 of whom fetch data from the **Cats API** (https://thecatapi.com) and supply it to the cats_display microservice using 
**DRF**.<br>
• The cats_display microservice has the display page which has the photo of each cat fetched from the microservices.<br>
• Each of these photos update every 3 seconds, I have used **HTMX** to poll images from the backend.<br>
• All of these containers can interact with each other because they are in the same docker network.<br>
• Since Cats API offers a limited API usage, I have used rate limiting here, by caching the user's IP in **Redis**, so that after a certain point the same list of photos is show to the user.<br>

Here's how it looks:

![HEY](https://user-images.githubusercontent.com/72970106/187250060-99587fca-5746-4e54-a2be-c3fcd498e02c.gif)
