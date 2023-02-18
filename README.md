# SyriaTel-Customer-Churn-A-Machine-Learning-Classification-Approach

![Cover image](https://github.com/nkevin90/Classifying-Customer-Churn-in-the-Telecom-Industry-A-Machine-Learning-Approach/blob/main/CoverImage.jpg)
A classifier to predict whether a customer will soon stop doing business(churn) with SyriaTel, a telecommunications company.

## 1. Business Understanding
> **Problem statement:**
 >* SyriaTel, a company in the telecommunication industry, has approached us with a pressing challenge: high customer churn rates are leading to financial losses and decreased customer satisfaction. To combat this issue, SyriaTel aims to accurately predict which customers are likely to leave, allowing them to take proactive measures to retain them. However, traditional methods for predicting customer churn have proven to be unreliable, with high rates of false positives and false negatives.

  > In light of this, SyriaTel has tasked us with developing a machine learning classification model that can accurately predict customer churn based on historical usage patterns and demographic information. Our goal is to create a model that will help SyriaTel minimize financial losses and improve customer satisfaction.

> **Objectives**:
 >* The primary objective of this project is to reduce customer churn, which is the loss of customers to competitors. By predicting which customers are at risk of leaving
 >* Identify which features/predictor variables affect the attrition of customers 
 >* Build 3 Classification models and evaluate the best one for classifying and predicting the churn rate

> **Metric of Success**
The project wil be considered a success if the classification model accurately identifies a high proportion of actual churners(High Recall) with a low number of false positive predictions(Low False Positive Rate) and demonstrates good generalization performance(Accuracy of 80% on unseen dataset).


## 2. Data Understanding

The dataset used was obtained from [Kaggle (Churn in Telecom's dataset)](https://www.kaggle.com/datasets/becksddf/churn-in-telecoms-dataset) and comprises of **3333 rows and 21 columns**. All the features except the phone number and state have numerical values, with the rest being categorical or binary (international plan, voice mail plan, and churn). The churn column will be used as our target variable 

This is a binary classification problem where the goal is to predict the likelihood of a customer churning and the **churn column** will be represented by **1 - True** and **0 - False**

|Dataset Coumns|about|
|:------|------|
|State|Represents the states in the USA|
|Account length|represents the length of time (in seconds or minutes) that a customer's account has been active.|
|Area code|Geographic area code of a customer's telephone number.|
|Phone number|represents the telephone number of a customer.|
|International plan|represents whether a customer has subscribed to an international call plan or not. It can have either "Yes" or "No" values.|
|voice mail plan|represents whether a customer has subscribed to a voice mail plan or not. It can have either "Yes" or "No" values.|
|Number vmail messages|represents the number of voice mail messages left by a customer.|
|Total day minutes|represents the total amount of time (in minutes) that a customer has spent on daytime calls.|
|Total day calls|represents the total number of calls that a customer has made during the day.|
|Total day charge|represents the total charge for daytime calls made by a customer.|
|total eve minutes|represents the total amount of time (in minutes) that a customer has spent on evening calls.|
|total eve calls|represents the total number of calls that a customer has made in the evening.|
|total eve charge|represents the total charge for evening calls made by a customer.|
|total night minutes|represents the total amount of time (in minutes) that a customer has spent on night calls.|
|total night calls|represents the total number of calls that a customer has made at night.|
|total night charge|represents the total charge for night calls made by a customer.|
|total intl minutes|represents the total amount of time (in minutes) that a customer has spent on international calls.|
|total intl calls|represents the total number of international calls made by a customer.|
|total intl charge| represents the total charge for international calls made by a customer.|
|customer service calls|represents the number of customer service calls made by a customer.|
|churn|represents whether a customer has cancelled their service or not. It can have either "True" or "False" values.|

## 3. External Dataset Validation
The Telecommunication industry continues to face a major and costly challenge in the form of customer churn. A recent research study conducted in 2018 by [Analysis Mason](https://www.analysysmason.com/globalassets/x_migrated-media/media/analysys_mason_ssa_mobile_satisfaction_sample_jun2018_rdmm03.pdf), a consulting and research company, highlights this issue. The study, titled **"Connected Consumer 2017: Mobile Customer Satisfaction and Churn in Sub-Saharan Africa**," was led by senior analyst Karim Yaici and research director Stephen Sale.

According to the study, the intention to churn among telecommunication subscribers in the sub-Saharan African region ranged from **9% to 16% across all operators surveyed**. This figure is in line with churn rates in other regions, but lower compared to the neighboring Middle East and Africa (MENA) region, where the intention to churn within 6 months was recorded at an average of 22%.

The study also found that customer service had a significant impact on churn for subscribers in South Africa, where the average churn rate was 17%. This effect was much greater compared to the other countries covered, which may reflect the differences in market maturity in the region. The findings from this study serve as external validation for the importance of customer service in reducing churn in the telecommunication industry.

## 4. Modeling
The Churn classification problem is tackled with approximately 6 algorithms and tuning the best two models. some of the used models are:
 * Logistic Regression Classifier model which is our vanila/baseline model - works by finding the best line that separates the two classes in a high-dimensional space.
 * Adaboost model -  idea is to give more weight to difficult-to-classify points and improve the overall performance of the model.
 * Gradient Boosting model -known for its high accuracy and performance
 * Random Forest model - tends to reduce overfitting, which is a common issue with decision trees.
 * Decision Tree model
 * K-Nearest Neighbor model
 * Hyperparameter tuning of the Decision Tree model
 * Hyperparameter tuning of the Random Forest model

## 5. Evaluation and Conclusion
In conclusion, the results of the mean random forest cross-validation score (k=5) on predicting the churn rate showed an accuracy of 0.95, with a weighted average of 0.95. The precision, recall, and f1-score for class 0 (not churned) were 0.97, 0.97, and 0.97, respectively. For class 1 (churned), the precision, recall, and f1-score were 0.82, 0.82, and 0.82, respectively. The macro average and weighted average for precision, recall, and f1-score were 0.89 and 0.95, respectively.

These results indicate that the random forest model performed well in terms of accuracy, with a high weighted average for precision, recall, and f1-score. The model's performance in predicting class 0 (not churned) was slightly better compared to class 1 (churned), with a higher precision, recall, and f1-score. Overall, the random forest model was considered the best model for predicting the churn rate.
