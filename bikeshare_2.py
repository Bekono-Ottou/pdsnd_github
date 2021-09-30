import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ["all","january", "february", "march", "april", "may", "june"]

DAYS = ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\n Hello! Let\'s explore some US bikeshare data!\n \n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Enter the city name (chicago, new york city, washington): \n").lower()
    while city not in CITY_DATA:
        print("Please, enter a valid city name (chicago, new york city, washington): \n")
        city = input("Enter the city name: \n").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Enter the month you want to filter by (all, january, february, ... , june): \n").lower()
    while month not in MONTHS:
        print("Please, enter a valid month (all, january, february, ... , june): \n")
        month = input("Enter the month you want to filter by: \n").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter the day you want to filter by (all, monday, tuesday, ... sunday): \n").lower()
    while day not in DAYS:
        print("Please, enter a valid day (all, monday, tuesday, ... sunday): \n")
        day = input("Enter the day you want to filter by: \n").lower()

    #print('-'*40)
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city.lower()])


    # convert the Start Time column to datetime
    # Make sure the dataframe contains the require column
    if 'Start Time' in df:
        df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
        df['month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
        if month.lower() != 'all':
        # use the index of the months list to get the corresponding int
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            month = months.index(month.lower()) + 1

        # filter by month to create the new dataframe
            df = df[df['month'] == month]

    # filter by day of week if applicable
        if day != 'all':
        # filter by day of week to create the new dataframe
            df = df[df['day_of_week'] == day.title()]
    else:
        print("The data cannot be displayed as expected due to missing start time data")

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # convert the Start Time column to datetime
    # Make sure the dataframe contains the require column
    if 'Start Time' in df:
        df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month from the Start Time column to create a month column
        df['month'] = df['Start Time'].dt.month

    # find the most common month
        popular_month = df['month'].mode()[0]
        print("The most common month people travel is:\n {} \n".format(popular_month))

    # TO DO: display the most common day of week
    # extract the day of the week from the Start Time column to create a day_of_week column
        df['day_of_week'] = df['Start Time'].dt.day_name()

    # find the most common day
        popular_day_of_week = df['day_of_week'].mode()[0]
        print("The most common day of the week people travel is:\n {} \n".format(popular_day_of_week))

    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
        df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
        popular_hour = df['hour'].mode()[0]
        print("The most common hour people travel is:\n {} \n".format(popular_hour))
    else:
        print("There is no start time data for the parameters you entered")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    # Make sure the dataframe contains the require column
    if 'Start Station'in df:
        most_common_start_sta = df['Start Station'].mode()[0]
        print("The most commonly used start station is:\n {} \n".format(most_common_start_sta))
    else:
        print("There is no start station data for the parameters you entered")

    # TO DO: display most commonly used end station
    # Make sure the dataframe contains the require column
    if 'End Station' in df:
        most_common_end_sta = df['End Station'].mode()[0]
        print("The most commonly used end station is:\n {} \n".format(most_common_end_sta))
    else:
        print("There is no end station data for the parameters you entered")

    # TO DO: display most frequent combination of start station and end station trip
    # Make sure the dataframe contains the require column
    if 'End Station' in df and 'Start Station'in df:
        combin_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
        print("The most frequent combination of start station and end station trip is:\n {} \n".format(combin_start_end_station))
    else:
        print("The most frequent combination of start station and end station trip cannot be displayed due to missing data")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    # Make sure the dataframe contains the require column
    if 'Trip Duration' in df:
        total_travel_time = df['Trip Duration'].sum()
        print("The total travel time is:\n {} \n".format(total_travel_time))

    # TO DO: display mean travel time
    # Make sure the dataframe contains the require column
        mean_travel_time = df['Trip Duration'].mean()
        print("The mean travel time is:\n {} \n".format(mean_travel_time))
    else:
        print("There is no trip duration data for the parameters you entered")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    # Make sure the dataframe contains the require column
    if 'User Type'in df:
        user_types = df['User Type'].value_counts()
        print("These are the counts of user types:\n {} \n".format(user_types))
    else:
        print("There is no user type data for the parameters you entered")

    # TO DO: Display counts of gender
    # Make sure the dataframe contains the require column
    if 'Gender' in df:
        gender_count = df['Gender'].value_counts()
        print("These are the counts of gender:\n {} \n".format(gender_count))
    else:
        print("There is no gender data for the parameters you entered")

    # TO DO: Display earliest, most recent, and most common year of birth
    # Make sure the dataframe contains the require column
    if 'Birth Year' in df:
        earliest_yob = int(df['Birth Year'].min())
        print("The earliest year of birth is:\n {} \n".format(earliest_yob))

        most_recent_yob = int(df['Birth Year'].max())
        print("The most recent year of birth is:\n {} \n".format(most_recent_yob))

        most_common_yob = int(df['Birth Year'].mode()[0])
        print("The most common year of birth is:\n {} \n".format(most_recent_yob))

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    else:
        print("There is no birth year data for the parameters you entered")

def load_analysis_selected(df):
    """Allows the Data Analyst to choose the analysis to run and then run his selection"""

    # Prompt the analyst which analysis they want to run
    print("\n Which analysis would you like to run?")
    print("(none, all, time_stats, station_stats, trip_duration_stats, user_stats) \n")
    analysis_choice = input().lower()

    # The chosen analysis is run if the analyst didn't type 'none' and the analyst is asked
    # whether or not he would like to run another analysis. While the analyst don't type
    # 'none', the chosen analysis will be run and if they type 'all', all the available
    # analysis will be run.
    while analysis_choice != "none":
        if analysis_choice == "time_stats":
            time_stats(df)
            print("\n Which other analysis would you like to run?")
            print("(none, all, time_stats, station_stats, trip_duration_stats, user_stats) \n")
            analysis_choice = input().lower()
        if analysis_choice == "station_stats":
            station_stats(df)
            print("\n Which other analysis would you like to run?")
            print("(none, all, time_stats, station_stats, trip_duration_stats, user_stats) \n")
            analysis_choice = input().lower()
        if analysis_choice == "trip_duration_stats":
            trip_duration_stats(df)
            print("\n Which other analysis would you like to run?")
            print("(none, all, time_stats, station_stats, trip_duration_stats, user_stats) \n")
            analysis_choice = input().lower()
        if analysis_choice == "user_stats":
            user_stats(df)
            print("\n Which other analysis would you like to run?")
            print("(none, all, time_stats, station_stats, trip_duration_stats, user_stats) \n")
            analysis_choice = input().lower()
        if analysis_choice == "all":
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            print("\n Which other analysis would you like to run?")
            print("(none, all, time_stats, station_stats, trip_duration_stats, user_stats) \n")
            analysis_choice = input().lower()
        else :
            print("\n Please, enter your choice again.\n Make sure you correctly type the analysis name.\n")
            print("\n Which other analysis would you like to run?")
            print("(none, all, time_stats, station_stats, trip_duration_stats, user_stats) \n")
            analysis_choice = input().lower()

def raw_data(city):
    """Prompt the data analyst if they want to see 5 lines of raw data"""

    # Loading the raw data file chosen by the analyst
    raw_file = pd.read_csv(CITY_DATA[city.lower()])

    # Ask the analyst whether or not they want to see 5 lines of raw data
    # Displays the data while the analyst do not say 'no'
    count = 0
    print("\n Make sure you correctly type no if you don't want to see the raw data \n")
    raw_data = input("Do you want to see the fisrt 5 lines of raw data? (yes or no) \n").lower()
    while raw_data != "no" and (count + 4) < raw_file.shape[0]:
        print(raw_file.loc[count : count + 4])
        count += 5
        print("\n Make sure you correctly type no if you don't want to see the raw data \n")
        raw_data = input("Do you want to see the next 5 lines of raw data? (yes or no) \n").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        raw_data(city)

        load_analysis_selected(df)

        restart = input('\n Would you like to restart? Enter yes or no.\n').lower()
        if restart != 'yes':
            break


if __name__ == "__main__":
	main()
