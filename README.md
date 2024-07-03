# Real Estate Analysis


## Project Overview
The real estate industry is a cornerstone of economic activity, with property transactions being among the most significant financial decisions individuals make. However, navigating this market can be daunting due to its complexity and the multitude of factors influencing property prices. To address this challenge, we propose a machine learning-based real estate analysis project aimed at providing users with valuable insights and predictions.
Our project leverages machine learning algorithms to analyze historical property data, incorporating features such as location, size, amenities, and market trends. The primary objectives of our system are threefold:

***• Price Prediction:*** By inputting various features such as location, size, and amenities, users can obtain an estimated price for a property. This functionality aids individuals in budget planning and decision-making when considering buying or renting a property.

***• Market Insights:*** Through data analysis and visualization, our project offers insights into the real estate market of the city. Users can access trends, patterns, and statistics, empowering them with valuable knowledge for making informed decisions about investments, pricing strategies, or market trends.

***• Recommendation System:*** Our system recommends similar properties based on user-provided inputs. By employing techniques such as collaborative filtering or content-based filtering, users can discover alternative options that match their preferences, thereby expanding their choices and enhancing their search experience.

By harnessing the power of machine learning, our project aims to democratize access to real estate information and facilitate smarter decision-making in property transactions. Whether individuals are buying, selling, or renting properties, our system provides valuable assistance, empowering users with the knowledge and insights needed to navigate the real estate market effectively.

## Features
1. **Price Predictor:** Uses a random forest regressor trained on a dataset with over 40,000 data points, achieving an R2 score of 0.90 and Mean Absolute Error (MAE) of 0.45.


   <img src="https://github.com/yatharth0512-iitj/Real-Estate-Analysis/blob/main/assets/Predictor.png">


2. **Recommender System:** Utilizes cosine similarity to suggest properties similar to selected ones, with weighted importance given to various features.


   <img src="https://github.com/yatharth0512-iitj/Real-Estate-Analysis/blob/main/assets/Recommender.png">


3. **Analytics Module:** Provides insights on existing properties using analytical libraries like Plotly and Seaborn.


   <img src="https://github.com/yatharth0512-iitj/Real-Estate-Analysis/blob/main/assets/Analysis.png">



## Installation
To run the project locally, follow these steps:

1. Clone the repository.
2. Make sure all the dependencies are already installed.
3. Open the terminal at web_app directory and run ***streamlit run home.py***


