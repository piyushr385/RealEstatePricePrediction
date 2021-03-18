<h1 align="center">Real Estate Price Prediction</h1>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li> <a href="#demo">Demo</a> </li>
    <li> <a href="#about-the-project">About The Project</a> </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#install">Installation</a></li>
        <li><a href="#execution-of-the-project">Execution-of-the-project</a></li>
      </ul>
    </li>
    <li><a href="#minimum-requirements">Minimum Requirements</a></li>
    <li><a href="#prerequisite">Prerequisite</a></li>
    <li><a href="#tools-frameworks">Tools Frameworks</a></li>
    <li><a href="#dataset-used">Dataset Used</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

## Demo
 **Prediction on magicbricks.com data**
 
<img src='/images/magicbricks.gif' width="700">


**Prediction on makaan.com data**

<img src='/images/makaan.gif' width="700">


## About The Project

* House-Price-Prediction is a web application that is made for predicting the 
 Price of houses(only Mumbai) based on BHK, bathrooms , rate per sqft , 
 area in sqft, Construction type, Sale type, Location.
* Dataset is created using webscraping and scraped from makaan.com and stored in a csv file.  
* This project is made with help of Machine learning algorithms, HTML, CSS and Flask framework.


## Getting Started
### Install

This project was originally written and tested with Python 3.6.11.

1. Install Python

If you don't have Python installed you can find it [here](https://www.python.org/downloads/ "here")

2. Install Anaconda

install anaconda you can download from [here](https://docs.anaconda.com/anaconda/install/windows/ "here").

3. Create Environment

You can name the environment whatever you want. Although you could use names such as: `houseprice`, `priceprediction` or `housepriceprediction`, we recommend something simple and intuitive like `house`. This is because this name will be used from now onwards.
```
conda create -n house python=3.6
````

4. Activate the virtual environment (for more details click [here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html "here"))

```
conda activate house
```
Note: At the end, you can deactivate it with: `conda deactivate`

5. Fork the Project

* Via HTTPS: `https://github.com/piyushr385/RealEstatePricePrediction.git`
* via SSH:  `git@github.com:piyushr385/RealEstatePricePrediction.git`
* via GitHub CLI `gh repo clone piyushr385/RealEstatePricePrediction`

Note: Work fast with our official CLI. [Learn more]( https://cli.github.com/ "Learn more")

Navigate into the folder with: `cd House-Price-Prediction/`

6. Install dependencies

To install the required packages and libraries, run this command in the project directory after cloning the repository (run this command in the virtual environment we created)
```
pip install -r requirements.txt
```

### Execution of the project

* Run the following commands on command line : (make sure you are in same working directory and you have activated virtual environment)

```
set FLASK_ENV=development
```

```
set FLASK_APP=app
```

```
flask run
```

OR

```
python app.py
```

```
NOTE : Execute the mumbai_house_model.ipynb to get random_model.pkl before executing the whole app. 
```
## Minimum Requirements

* HDD : 500gb 
* RAM : 4gb
* OS  : Windows/Linux

## prerequisite

* python 3.7
* Anaconda
* VS code

## Tools Frameworks 

* pandas : used for data analysis.
* Numpy  : perform a number of mathematical operations.
* Beautiful Soup : Is a Python library used for pulling data out of HTML.
* scikit-learn : used to build machine learning models.
* Flask : extensible web microframework for building web applications with Python.
* HTML and CSS
* Bootstrap

## Dataset-Used:

Data used is scraped from makaan.com website and uploaded in Repository in Data folder.

## Contributing

**Become a Contributor 🙌 💎**

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to your Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See [LICENSE](https://github.com/piyushr385/RealEstatePricePrediction/blob/master/LICENSE) for more information.

## Project created by :
* [Meghdeep Sapre](https://www.linkedin.com/in/meghdeepsapre97/ "Meghdeep Sapre")
* [Piyush Rane](https://www.linkedin.com/in/piyushrane/ "Piyush Rane")
