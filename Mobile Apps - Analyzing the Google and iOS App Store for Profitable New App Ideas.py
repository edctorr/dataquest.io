#!/usr/bin/env python
# coding: utf-8

# ## Mobile Apps: Analyzing the Google and iOS App Store for Profitable New App Ideas
# * Analysis and Name of Company Created by **Eduardo Torres**
# * TyrAppTor, Inc. 
# * Last Updated: 04/04/2020

# In this project, I will analyze publically available sample datasets from the Google and iOS App Store to help enable the application development team to make data-driven decisions on apps with highest potential revenue opportunities for the company. I will take the role of the Data Analyst for a company that builds free Android and iOS mobile apps and targets English Speakers. For purposes of this analysis, the company's name is TyrAppTor Inc., (TAT).
# 
# TAT builds Android and iOS Apps that are available to the public free to download and install, and TAT's main source of revenue consists of in-app ads. Considering how the company generates revenue, I will be analyzing the available data to find the best genres/categories to invest in app development. To better enable the app development decision making, I will determine:
# 
# * Most common apps by genre in the iOS and Google Play App Store
# * Most popular apps determined by number of installs in the iOS and Google Play App Store

# **<font color=Blue>Datasource Documentation:</font>**
# **1.** [Google Play App Store](https://www.kaggle.com/lava18/google-play-store-apps) 
# **2.**  [Apple iOS App Store](https://www.kaggle.com/ramamet4/app-store-apple-data-set-10k-apps)

# ## Summary of Results

# As a result of the analysis, my findings indicate that a profitable app idea is one that takes a popular book and passes it through a gamification process that can create more of an active approach to reading. This idea can be in the form of a 3-D book where the user gets to follow the main character throughout the book and engages the user to be part of that story. This has the potential to explore a new approach to learning which can have a great marketing impact on the game and reputation of TyrAppTor, Inc.

# ## Exploring and Cleaning Publicly Available Data to Avoid Additional Costs

# In[1]:


# The datasource function will help automate the import of other datasets
def datasource(source):
    opened_file = open(source)
    from csv import reader
    read_file = reader(opened_file)
    dataset = list(read_file)
    opened_file.close()
    return dataset
    
# Importing iOS App Store Dataset
ios_apps = datasource('AppleStore.csv')
ios_header = ios_apps[0]
ios_data = ios_apps[1:]

# Importing Google Play Store Dataset
android_apps = datasource('googleplaystore.csv')
android_header = android_apps[0]
android_data = android_apps[1:]


# In[2]:


# The explore_data function helps make the datasource exploration readable (see below example)
def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]
    for row in dataset_slice:
        print(row)
        print('\n')
        
    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))


# **<font color=Grey>Explores the Google Play Store Raw Data:</font>**

# In[3]:


print('Google Play Store Data')
print(android_header)
print('\n')
explore_data(android_data, 0, 3, True)


# **<font color=Grey>Explores the iOS App Store Raw Data:</font>**

# In[4]:


print('iOS Apple Store Data')
print(ios_header)
print('\n')
explore_data(ios_data, 0, 3, True)
print('\n')


# **<font color=Black>Data Exploration:</font>**
# 
# During the data exploration, I found that the Google Play data set contains *13* columns and aproximately *10,841* apps, as for the iOS App Store, I found that the data set contains *16* columns and aproximately *7,197* apps. Furthermore, I determined that the columns that could be useful for the analysis are listed in the below tables: 
# 
# **<font color=Green>Google Play Store:</font>**
# 
# |Column              | Defenition                        |
# |:-------------------| :---------------------------------|
# |App                 | App Name                          |
# |Category            | Category the app belongs to       |
# |Rating              | Overall User Rating               |
# |Reviews             | Number of User Reviews            | 
# |Installs            | Number of User Downloads/installs |
# |Type                | Paid or Free                      |
# |Price               | Price of the App.                 |
# |Content Rating      | Age Group the App. Targets.       |
# |Genres              | Available Genre Types             |
# 
# **<font color=Green>Apple iOS App Store:</font>**
# 
# |Column              | Defenition                      | 
# |:-------------------| :-------------------------------|
# |track_name          | App Name                        |
# |currency            | Currency Type                   |
# |price               | Price Amount                    |
# |ratingcounttot      | User Rating Counts (All v.)     |
# |ratingcountver      | User Rating counts (Current v.) |
# |user_rating         | Average User Rating             |
# |cont_rating         | Content Rating                  |
# |prime_genre         | Primary Genre                   |

# **<font color=Black>Data Cleaning and Preparation:</font>**
# 
# To make sure that the analysis is appropriate, the data source will need to go through cleaning and preparation before analysis can be performed. In this section, I will be detecting, correcting, and removing inaccurate and duplicate data.
# 
# To make sure I use my time efficiently, I am using the dicussions from the data source documentations to identify errors within the data sources. As such, my readings from the documentations indicate that the Google Apps data source index 10472 is missing the category, which is shifting data and must be removed. 

# In[5]:


#For purposes of validations, I am comparing the index before and after 10472 to make sure
#the category and shiftment of data is actually happening
print(android_header)
print('\n')
print(android_data[10471])
print('\n')
print(android_data[10472])
print('\n')
print(android_data[10473])


# In[6]:


#The below deletes the 10472 index from the analysis
del android_data[10472]


# **<font color=Black>Data Cleaning and Preparation - Continued:</font>**
# 
# The documentation also indicate that the data set contains multiple duplicate entries. Below I compiled a list to provide the number of duplicate entries, which is 1,181. These duplicates will need to be removed; however, these additional records cannot be removed randomly, instead will be removed strategically.
# 
# After looking through the example duplicates in the code below, I identified that, for example, 'Google Ads', returns three additional records. Besides the number of reviews, everything in those records are identical. The difference in the number of reviews can provide insight into how recent these entries are, as such, the highest number of reviews will be treated as the most recent and the rest of the records will be eliminated. The result I expect to see after removing the duplicates is 9659, which is the difference between the actual number in the data source and the duplicates.

# In[7]:


#The below identifies duplicate and unique apps in list form for the Android App Store
duplicate_apps = []
unique_apps = []

for app in android_data:
    name = app[0]
    if name in unique_apps:
        duplicate_apps.append(name)
    else:
        unique_apps.append(name)
        
print('Number of duplicate apps:', len(duplicate_apps))
print('\n')
print('Examples of duplicate apps:', duplicate_apps[:10])
print('\n')


# In[8]:


#In this section, I look through the example duplicate apps to identify a strategy to remove them
print(android_header)
print('\n')
for app in android_data:
    if app[0] == 'Google Ads':
        print(app)
        print('\n')


# In[9]:


#The below will identify the expect number of records expected once duplicates have been removed
reviews_max = {}

for app in android_data:
    name = app[0]
    n_reviews = float(app[3])
    if name in reviews_max and (reviews_max[name] < n_reviews):
        reviews_max[name] = n_reviews
    elif name not in reviews_max:
        reviews_max[name] = n_reviews
        
print('Expected length:', len(android_data) - 1181) #Knowing that there are 1181 dups, I expect to see 9659 records
print('Actual length:', len(reviews_max))


# In[10]:


#The below will seperate clean data and and remove duplicate values using the reviews_max for the logic
android_clean = []
already_added = []

for app in android_data:
    name = app[0]
    n_reviews = float(app[3])
    
    if (reviews_max[name] == n_reviews) and (name not in already_added):
        android_clean.append(app)
        already_added.append(name) # make sure this is inside the if block


# In[11]:


explore_data(android_clean, 0, 3, True)


# **<font color=Black>Data Cleaning and Preparation - Continued:</font>**
# 
# Once removing the duplicates, I explore the results to make sure that the expected results are correct using the explore_data function, which I see to be correct.
# 
# The next part of the preparation is to focus on the audience. In looking through the data, I see that there are multiple apps directed to Non-English speakers, which is not my focus. The next part of the preparation is to isolate Enlgish apps to continue with the analysis.
# 
# To isolate non-english apps, I will write a function (enlgish) that will utilize the ASCII (American Standard Code for Information Interchange) system, which provides an English Text range from 0 to 127 to help identify if a character belongs to the set of Enlgish characters. The only problem with this approach is that there are certain apps that use emojis and trade mark symbols, which puts them outside the 0-127 Enlgish character range, see test example below). To minimize data loss, I will update the function to only remove apps that have more than three characters outside of the English range, which will allow for apps with either three emojis and/or trademark symbols to be included in the analysis.

# In[12]:


#Provided Examples of Non-English Apps
print('Provided Examples of Non-English Apps:')
print(ios_data[813][1])
print(ios_data[6731][1])
print(android_clean[4412][0])
print(android_clean[7940][0])


# In[13]:


#Functions Determines if the String Input is English.
def english(string):
    for char in string:
        if ord(char) > 127:
            return False
    return True


# In[14]:


#Tests example for the English function
print('Is '+'Instagram '+'an English App?:', english('Instagram'))
print('Is '+'爱奇艺PPS -《欢乐颂2》电视剧热播 '+'an English App?:', english('爱奇艺PPS -《欢乐颂2》电视剧热播'))
print('Is '+'Docs To Go™ Free Office Suite '+'an English App?:', english('Docs To Go™ Free Office Suite'))
print('Is '+'Instachat 😜 '+'an English App?:', english('Instachat 😜'))


# In[15]:


#Update to the Enlgish Functions to Include 3 characters outside the Enlgish Range
def new_english(string):
    not_english = 0
    
    for char in string:
        if ord(char) > 127:
            not_english += 1
            
    if not_english > 3:
        return False
    else:
        return True


# In[16]:


#Tests example for the New English function
print('Is '+'Instagram '+'an English App?:', new_english('Instagram'))
print('Is '+'爱奇艺PPS -《欢乐颂2》电视剧热播 '+'an English App?:', new_english('爱奇艺PPS -《欢乐颂2》电视剧热播'))
print('Is '+'Docs To Go™ Free Office Suite '+'an English App?:', new_english('Docs To Go™ Free Office Suite'))
print('Is '+'Instachat 😜 '+'an English App?:', new_english('Instachat 😜'))


# In[17]:


#The below will isolate English apps into its own list
android_english = []
ios_english = []

for app in android_clean:
    name = app[0]
    if new_english(name) == True:
        android_english.append(app)
        
for app in ios_data:
    name = app[1]
    if new_english(name) == True:
        ios_english.append(app)


# **<font color=Grey>Explores Google English App Play Store Data:</font>**

# In[18]:


explore_data(android_english, 0, 3, True)


# **<font color=Grey>Explores iOS English App Store Data:</font>**

# In[19]:


explore_data(ios_english, 0, 3, True)


# **<font color=Black>Data Cleaning and Preparation - Continued:</font>**
# 
# The last part of the data cleaning and preparation is to look at the price aspect. As mentioned in the introduction, TAT generates revenue through in-app ads from free apps to the public. The data set contains paid and free apps, which will require free apps to be isolated. 
# 
# The below process isolates free apps to address the last step in the cleaning process. The final app count for the Android data is *8,864*. 

# In[20]:


#The below seperates apps with a price of 0 and classifies them as part of a new list called Android
android = []
ios = []

for app in android_english:
    price = app[7]
    if price == '0':
        android.append(app)
        
for app in ios_english:
    price = app[4]
    if price == '0.0':
        ios.append(app)


# **<font color=Grey>Explores Google Free English App Play Store Data:</font>**

# In[21]:


print(android_header)
print('\n')
explore_data(android, 0, 3, True)


# **<font color=Grey>Explores iOS Free English App Store Data:</font>**

# In[22]:


print(ios_header)
print('\n')
explore_data(ios, 0, 3, True)


# ## Identifying Apps with the Highest Revenue Potential

# TAT's revenue is directly impacted by the number of users interacting with its applications, which makes the process of data-driven decision making extremly important for the company. The main portion of this analysis is to identify applications already in use with the highest potential number of users.
# 
# Additionally, TAT's is a cost conscious company, which means that potential application ideas have to go through a validation process made up of three parts:
#  * Minimal software development and market testing
#  * Assuming good responses during the initial development, further development is made
#  * Once profitable after six months, iOS and Android apps are built

# In[23]:


print('Google Play Store')
print(android_header)
print('\n')
print('iOS App Store')
print(ios_header)


# **<font color=Black>Most Common Genres/Categories in each App Store:</font>**
# 
# In this section, I am investigating apps with the most common Genres and Categories in both the Google and iOS App Store. I will start by looking at common generes in both app markets. I will be using the (Category and Genres) columns for the Google Play Store and (prime_genre) column for the iOS App Store. Using these columns, I created multiple frequency tables to organize values as percentages of total in descending order. These frequency tables provide insight into which genres/categories are most common in the app market place. 

# In[24]:


#The nested fuction below organizes column information in a frequency table as a percentage of total in dec order
def freq_table(dataset, index):
    table = {}
    total = 0
    
    for row in dataset:
        total += 1
        column = row[index]
        
        if column in table:
            table[column] += 1
        else:
            table[column] = 1
            
    percentage_table = {}
    for key in table:
        percentage = (table[key] / total) * 100
        percentage_table[key] = percentage
            
    return percentage_table

def display_table(dataset, index):
    table = freq_table(dataset, index)
    table_display = []
    for key in table:
        key_val_as_tuple = (table[key], key)
        table_display.append(key_val_as_tuple)
        
    table_sorted = sorted(table_display, reverse = True)
    for entry in table_sorted:
        print(entry[1], ':', entry[0])


# **<font color=Grey>Google App Play Store Analysis:</font>**
# 
# Looking through the Google Play Store genre frequency table, I see that there is no significant distinction between genres. Tools rank as the most common, followed by Entertainment, Education and Business (8.4%, 6.1%, 5.3%, 4.6%, respectively). This indicates that the Google Play Store shows a more balanced landscpae for fun and practical applications. However, in looking through the Category frequency table, I see a different story. The Category table indicates that the Family category is the most common, followed by Games and Tools (18.9%, 9.7&, and 8.5%, respectively). 
# 
# The interesting part of the data is that Family contains a significat portion of children games, which indicate that the Google App Store is heavily dominated by game related apps, which are the most common. Since I am looking for the most common apps, the genere column is not very helpful for my analysis. I believe the Category Colum provides a better breakdown and representation of the most common, and for this reason, will move forward only using the Category Column for the Google Play Store.

# In[25]:


# Most common 'Genre' in the Google Play Store
display_table(android, -4)


# In[26]:


# Most common 'Category' in the Google Play Store
display_table(android, 1)


# **<font color=Grey>iOS App Store Analysis:</font>**
# 
# As for the free English iOS App Store anlysis, the Games genre stands out with a 58.16%, which is significantly higher than any of the other genres. The Entertainment, Photo & Video, Education, and Social Networking generes are next in line and are more balanced out (7.9%, 5.0%, 3.7%, 2.3%, respectively).
# 
# While it is clear that the free English iOS Apps data demonstrates a market heavily dominated by Games, Entertainment, Photo & Video, Education and Social Networking, I will continue to investigate to determine if commonality also indicates popularity, in terms of number of installs (user counts).

# In[27]:


# Most common 'Prime Genre' in the Google Play Store
display_table(ios, -5)


# **<font color=Black>Identifying App Popularaty by the Number of Users:</font>**
# 
# In this section of the analysis, I will focus on identifying app popularity driven by the number of users. As such, I will be using the Installs column from the Google Play Store to identify popularity. Considering that the iOS App Store does not contain an installs column, I will default to the rating_count_tot to indicate popularity for apps.

# **<font color=Grey>Google App Play Store Analysis:</font>**
# 
# Using the display_table function that I previously created, I am able to quickly see what genre popularity looks like in a freequency table form. Now, while the frequency table provides insight, its difficult to read into popularity considering how open-ended these numbers look. This will require cleaning and standardization, meeaning, I will be removing (,'s and +'s) and converting the string values into floats in order to properly calculate average of installs within the genres.

# In[28]:


display_table(android, 5) # the Installs columns


# In[29]:


import string

def clean_string(input):
    clean = input
    for char in clean:
        if char in string.punctuation:
            clean = clean.replace(char,"")
    return clean


# In[30]:


def genre_installs(string, n_one, n_two):    
    categories_dic = freq_table(string, n_one)
    for category in categories_dic:
        total = 0 #sum of installs specific to each genre
        len_category = 0 #store the number of apps specific to each genre
        for row in android:
            category_app = row[n_one]
            installs = row[n_two]
            if category_app in category:
                installs = clean_string(installs)
                installs = int(installs)
                total += installs
                len_category += 1

        average_num = total / len_category
        print(category, ':', average_num)


# In[31]:


genre_installs(android,1,5)


# In[32]:


for row in android:
    app = row[1]
    name = row[0]
    rating = row[5]
    if app == 'COMMUNICATION'and (rating == '1,000,000,000+'or rating == '500,000,000+'or rating == '100,000,000+'):
        print(name, ":", rating)


# **<font color=Grey>Google App Play Store Analysis Continued:</font>**
# 
# Once I cleaned and looped over the Google Play App store data, I was able to determine that the communication genere had the the most installs with an approximate number of  38,456,119 installs. The only problem with this number is that looking deeper into the data, I see that outliers are skewing my results. This indicates that if these outliers were to be removed, the data could indicate that the original average is much smaller than origionally anticipated.
# 
# While the communications genere is interesting, there are large players that have a lot of power and control this space, like WhatsApp. This can also be said about games and video apps, like Youtube. The market is over saturated, which means that the chances of generating revenue in these genres will not be as optimistic and would not recommend building apps into these spaces.
# 
# One genere that is interesting and has the potential to generate revenue is the BOOKS_AND_REFERENCE, which has a estemiated avereage of 8,767,812 installs. While this genere may also have a few outliers, there are a few apps that make up that outlier group that is not significant enough to ignore this genere. From the information in the frequency tables, I see that a great idea would be to take an app that is popular and make it into an app that can be more engaging (a game version of a book or a simply 3-D audio book) than just a normal raw book.

# In[33]:


for app in android:
    if app[1] == 'BOOKS_AND_REFERENCE':
        print(app[0], ':', app[5])


# In[34]:


# This demonstrates outliers within the genre
for app in android:
    if app[1] == 'BOOKS_AND_REFERENCE' and (app[5] == '1,000,000,000+'
                                            or app[5] == '500,000,000+'
                                            or app[5] == '100,000,000+'):
        print(app[0], ':', app[5])


# In[35]:


#This section convers a section that is still worth exploring
for app in android:
    if app[1] == 'BOOKS_AND_REFERENCE' and (app[5] == '1,000,000+'
                                            or app[5] == '5,000,000+'
                                            or app[5] == '10,000,000+'
                                            or app[5] == '50,000,000+'):
        print(app[0], ':', app[5])


# **<font color=Grey>iOS App Store Analysis:</font>**
# 
# As for the iOS App Store, the navigation genre leads the charts; howerver, outliers (i.e. Waze and Google Maps) make up a significant number of those installs. Unfortunately, most of the popular genres are heavily influeced by a few popular apps which makes the genre appear more popular that it really is.
# 
# The purpose of this analysis was to find an app idea that can be applied to both the Google Play Store and iOS App Store. Since the Google Play Store has a great opportunity within the Books and Reference genre, exploring this genre in the iOS App Store considering that it has a good average of installs in the iOS App Store is a good idea.
# 
# Looking through the frequency table, I see that this genre is domincated by the Bible and Dictionary Apps; however, looking closer to the data, I see that there might also be an opportunity to enter this genre and provide an app that takes a popular book and creates a version that is more engaging to the user.

# In[36]:


genres_ios = freq_table(ios, -5)

for genre in genres_ios:
    total = 0
    len_genre = 0
    for app in ios:
        genre_app = app[-5]
        if genre_app == genre:            
            n_ratings = float(app[5])
            total += n_ratings
            len_genre += 1
    avg_n_ratings = total / len_genre
    print(genre, ':', avg_n_ratings)


# In[37]:


for app in ios:
    if app[-5] == 'Reference':
        print(app[1], ':', app[5])


# ## Conclusion

# In this project, I took the role of the analyst to analyze the Google and iOS app store data for potential profitable new app ideas. 
# 
# In my analysis, I concluded that a profitable app idea is one that takes a popular book and passes it through a gamification process that can create more of an active approach to reading. This idea can be in the form of a 3-D book where the user gets to follow the main character throughout the book and engages the user to be part of that story. This has the potential to explore a new approach to learning which can have a great marketing impact on the game and reputation of TyrAppTor, Inc.
