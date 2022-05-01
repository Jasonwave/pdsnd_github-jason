#Got help from geeksforgeeks.org for research of functions
#Got extra resources working with pandas from udemy course Understand data science in 10hours
#Got extra help from colleagues to fix some bugs


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    #set an empty variable to store the selected city from the user
    city=''

    #putting the selection of the user in a while loop to handle invalid inputs

    while city not in CITY_DATA.keys():
        city=input("\n\nKindly selected your city either Chicago,New York or Washington: \n").lower()
        if city not in CITY_DATA.keys():
            print("\nWrong input, kindly select from Chicago,New york or Washington")
            
    print("\nYou have selected {} City\n".format(city.capitalize()))   

    # TO DO: get user input for month (all, january, february, ... , june)
    #Information about the months will be stored in a dictionary to be selected from, 'all' option also included

    month_dict = {'January': 1, 'February': 2, 'March': 3,
                  'April': 4, 'May': 5, 'June': 6, 'All': 7}
    month=''
    
    while month not in month_dict.keys():
        month=input("Please Enter a given month from either January to June or input all to view all : \n").lower().capitalize()
        if month not in month_dict.keys():
            print("Wrong input, Kindly select either January, February, March...June or all to display a month")
   
    print("\nYou have selected the month of {}.\n".format(month.capitalize()))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    #Information about the day of week will also be stored in a tuple to be selected from, all also included
    day_selected=''
    day_list=['All','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    day=input("Kindly enter your day of interest: \n").lower().capitalize()
    if day_selected not in day_list:
        print("Wrong input, Kindly choose from Monday to Sunday or select all")
    
    print("\n You have selected {} as your day of week".format(day.capitalize()))

    print("\nYou have selected {} as your city, {} as your month, and {} as your day.\n".format(city.capitalize(), month.capitalize(), day.capitalize()))
    

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    #Now we want to read the file and access the contents of the selected city
    df = pd.read_csv(CITY_DATA[city])

    #Now we convert the Start time of the City to datetime format for processing
    df['Start Time']=pd.to_datetime(df['Start Time'])

    #Now we extract both day of week and month from the properly formatted Start Time column
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['month'] = df['Start Time'].dt.month


    #Now filtering by month if all is not selected
    if month != 'All':
        months_list=['January', 'February', 'March', 'April', 'May', 'June']
        month=months_list.index(month) + 1

	#Create the new month dataframe
    df = df[df['month']== month]
	
 
    #Now filter by day of week if all is not selected
    if day != 'All':
        
        df = df[df['day_of_week'] == day]
	
	#create the day dataframe
    df = df[df['day_of_week']==day]

    #Return the dataframe selected

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    #The Start Time column is not properly formated so it is coverted to datetime format and reupdated
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #initialize a variable to store the most frequent(mode) month data to be displayed
    frequent_month = df['month'].mode()[0]
    print("\n The Most common month is: {}".format(frequent_month).capitalize())
   
    # TO DO: display the most common day of week
    #initialize a variable to store the most frequent(mode) day of week data to be displayed
    frequent_day = df['day_of_week'].mode()[0]
    print("\n\nThe Most Common Day of the week is: {}\n".format(frequent_day).capitalize())



    # TO DO: display the most common start hour
    #initialize a variable to store the most frequent(mode) day of week data to be displayed
    df['hour_frame'] = df['Start Time'].dt.hour
    frequent_hour = df['hour_frame'].mode()[0]
    print("\nThe Most common Start Hour is: {}".format(frequent_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    #initialize a variable to store the most frequent(mode) day of week data to be displayed
    frequent_start_station = df['Start Station'].mode()[0]
    print("\nThe most commonly used start station is: {}".format(frequent_start_station).capitalize())


    # TO DO: display most commonly used end station
    frequent_end_station = df['End Station'].mode()[0]
    print("\nThe most commonly used end stationis: {}".format(frequent_end_station).capitalize())

    # TO DO: display most frequent combination of start station and end station trip
    
    #select the start and end station column and concatenate them to get their combination
    df['First_To_last'] = df['Start Station'].str.cat(df['End Station'], sep=' - ')
    frequent_start_and_stop = df['First_To_last'].mode()[0]
    print("\nThe most frequent combination of start and end station trips are {}.".format(frequent_start_and_stop).capitalize())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time_sum = df['Trip Duration'].sum()
    
    #To get the time in hour minute and seconds we use the divmod() function to divide the sum of trip duration column and this will be used for consequently.
    minute_time, seconds_time = divmod(travel_time_sum, 60)
    hour_time, minute_time = divmod(minute_time, 60)

    print("\n\nThe total travel time is {} hour(s), {} minute(s) and {} second(s)\n.".format(hour_time,minute_time,seconds_time))

    # TO DO: display mean travel time
    mean_travel_time = round(df['Trip Duration'].mean())
    minute_time, seconds_time = divmod(mean_travel_time, 60)

    if minute_time > 60:
        hours_time, minute_time = divmod(minute_log, 60)
        print("\nThe mean travel time is {} hour(s), {} minute(s) and {} second(s).".format(hours_time,minute_time,seconds_time))
    else:
        print("\n\nThe mean travel time is {} minute(s) and {} second(s).\n".format(minute_time,seconds_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    users_num = df['User Type'].value_counts()
    print("\n\nThe counts of users types are: {}\n".format(users_num))

    # TO DO: Display counts of gender
    #Used a try and except statement to check if the data queried is available.
    #Will do this for a couple of TODOs, so that unavailable data wont break the program
    try:
        gender_num = df['Gender'].value_counts()
        print("\n\nThe users gender are : {}".format(gender_num))
    except:
        print("\n\nThe city selected has no 'Gender' data.\n")

    # TO DO: Display earliest, most recent, and most common year of birth
    print("Displaying the earliest, most recent and most common year of birth...")
    try:
        min_year = int(df['Birth Year'].min())
        latest_year = int(df['Birth Year'].max())
        frequent_year = int(df['Birth Year'].mode()[0])
        print("\nThe earliest year of birth is: {}".format(min_year))
        print("The most recent year of birth is: {}".format(latest_year))
        print("The most common year of birth is: {}".format(frequent_year))
    except:
        print("\n\nThe city has no data about the Year of Birth of Users.\n")

   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    reply_list = ['yes', 'no']
    view_data = ''

    #create an increment variable for 5 more rows of data
    increment = 0
    while view_data not in reply_list:
        view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()
     
        if view_data == "yes":
            print(df.head())
        elif view_data not in reply_list:
            print("\nIncorrect response, Kindly input 'yes' or 'no': ")

    #ask for more rows of data
    while view_data == 'yes':
        increment += 5
        view_data = input("Would you want to see 5 more rows of data?Enter yes or no: ").lower()

        if view_data == "yes":
             print(df[increment:increment+5])
        elif view_data != "yes":
             break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
