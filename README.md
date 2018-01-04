This web application lets you find out highest overall rated hospitals within in 20-mile radius your zip code. It presents you with a verbal summary of your choices. This web application knows zip codes from the USA only. 

![Auto generated text](https://qxf2.com/assets/img/hospitals-near-me/higher_rated_farther_away.png)

# Background

Apparently all US hospitals that accept publicly insured patients (in the US, they call it Medicaid and Medicare) have to submit data about their quality of care to a body known as the [Centers for Medicare & Medicaid Services (CMS)](https://www.cms.gov/). Most hospitals seem to accept publicly insured patients ... so the data that someone compiled and uploaded to [Kaggle](https://www.kaggle.com) is quite comprehensive. 

# Data source
[Hospital General Information dataset on Kaggle](https://www.kaggle.com/cms/hospital-general-information)

# Setup

1. pip install -r REQUIREMENTS.txt
2. To start the server:
> python run.py
3. Go to localhost:6464 in your browser
4. To test the different messages, you can use the following zip codes

> 99557 for no hospitals

> 71923 for exactly one option

> 72055 for multiple options

> 13210 for the case where the highest rated hospital is not the closest

# Disclaimer

This was a internal Qxf2 practice project to learn natural language generation with Python and nothing more. If you are interested in using an application like this, you should use the US Government's official [Hospital Search Application](https://www.medicare.gov/hospitalcompare/search.html) and not this repository. 
