![image](https://github.com/afandigit/Market-Housing/assets/106676180/d45c0ce4-5a38-4021-a82a-a2879b270023)<h1>Market Housing Project</h1>
<br/>
<hr/>



<h2>Overview</h2>

I am using the Scrapy Framework to scrape datasets from websites offering real estate listings for sales and rentals. The goal is to analyze this data and develop a Machine Learning model that suggests listings to clients based on their preferences and financial capabilities.

This involves extracting relevant features from the listings, such as location, price, property type, and amenities, and using these features to train a recommendation system.

The system will leverage data analysis, data science techniques, and business intelligence to provide personalized and financially feasible real estate options for clients.

This project aims to enhance the user experience and optimize the property search process, ultimately driving better business outcomes for real estate platforms.



<h2>Features</h2>

- Web Scraping : Scrapy Framework. [Done]
- Data Cleaning. [Done]
- Data Analysis - Explore and Visualize data : Python libraries - Microsoft Power BI. [Done]
- MERN Stack. [Current step ...]
- Data Preparation for Machine Learning : Data standardization and preprocessing. [Future step ...]
- Machine Learning. [Future step ...]
- Deploy the trained recommendation model in real time. [Future step ...]



<h2>Dataset</h2>

I have been scrapping this dataset using Scrapy Framework for couples days ( mores than 50 hours in general), on two real estate websites in Morroco (Avito - Mubawab) (each website has its specific Spider), just to start using data cleaning process so that i can automate this process in the future.
my goal is to scale this dataset for the entire world, Scrapping the most common Real Estate Websites in the world.
this dataset contains more than 14000 records (Each record represent the data scrapped from an Ad of a real estate website).

<h3>Dataset description</h3>

<ul>
  <li>
    <b>advertisement_url</b> : Which is the full URL of the page in the website on which i retrieve detailed information on the current real estate announcement.
  </li>
  <li>
    <b>title</b> : The title of the property advertisement.
  </li>
  <li>
    <b>publication_date</b> : The date the advertisement was published by its owner.
  </li>
  <li>
    <b>price</b> : The price of the property (in DH = Moroccan DirHam : the official monetary currency of Morocco).
  </li>
  <li>
    <b>location</b> : The exact location of the property.
  </li>
  <li>
    <b>description</b> : Detail parts of the property.
  </li>
  <li>
    <b>complete_description</b> : Complete description of the property established by its owner.
  </li>
  <li>
    <b>features_list</b> : A liste of The property type (Apartment, House, Villa, farmhouse, ...), property state, number of floors ...
  </li>
  <li>
    <b>insert_date</b> : The Date the current announcement was scrapped.
  </li>
</ul>


<h2>Data Cleaning</h2>


<h4>Cleaning Process .... </h4>
<ol>
  <li>
    First step i commit is that i <strong>remove</strong> duplicates records, so as not to distort our analysis in the future. <i>Because in practice, some people repost their real estate ads multiple times on these websites, causing them to appear multiple times for visitors.</i>
Results : we found 3848 duplicate records.
  </li>
  <li>
    Cleaning <b>advertisement_url</b> column --> Adding "website_name" column based on current column and Visualizing the number of records per website name.
  </li>
  <li>
    Cleaning <b>title</b> column --> Adding three new columns based on the current one and supported by <b>feature_list</b> and <b>price</b> columns; 'ad_type' column, 'property_type' column and 'property_surface' column + Analyzing all titles by counting the most appeared words + analyzing the new 'property_surface' column.
    <ul> 
      <li><b>Ad_type column</b> is gonna indicate the type of advertisment; Sale, Rental or Vocation Rental.</li>
      <li><b>property_type column</b> indicate one of these categories, 'Apartments', 'Villas and Riads', 'Houses', 'Rooms', 'Land and Farms', 'Desks', 'Flatsharing', 'Warehouses' or 'Other Real Estate'.</li>
      <li><b>property_surface column</b> indicate the surface of the property (m²)</li>
    </ul>
  </li>
  <li>
    Cleaning <b>publication_date</b> column --> 
  </li>
  <li>
    <b>price</b> :
  </li>
  <li>
    <b>location</b> :
  </li>
  <li>
    <b>description</b> : 
  </li>
  <li>
    <b>complete_description</b> : 
  </li>
  <li>
    <b>features_list</b> : 
  </li>
  <li>
    <b>insert_date</b> :
  </li>
</ol>






<h2>Data Analysis</h2>

Avito 25.73% higher than Mubawab in terms of records in this dataset. and the most 

![image](https://github.com/afandigit/Market-Housing/assets/106676180/4e6a8771-a4e2-4c3d-a378-90da1ed2cd31)

and in term of property type, appartments is the biggest category sold or rent in the Moroccan market. 

![frequency of each property type ](https://github.com/afandigit/Market-Housing/assets/106676180/55152bfc-1718-4657-98ea-0bce946d3be0)





























