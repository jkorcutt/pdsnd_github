import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = ['all', 'january', 'february', 'march','april', 'may','june']

DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('\nPlease type one of the following: Chicago, New York City, Washington\n').lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print('Please try again. Be sure to type one of the following: Chicago, New York City, Washington\n')
            continue
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('\nPlease type one of the following: all, January, February, March, April, May, June\n').lower()
        if month not in ('all', 'january', 'february', 'march','april', 'may','june'):
            print('Please try again. Be sure to type one of the following: all, January, February, March, April, May, June\n')
            continue
        else:
            break


    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('\nPlease type one of the following: all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday\n').lower()
        if day not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            print('Please try again.  Be sure to type one of the following: all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday\n')
            continue
        else:
            break


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
    df = pd.read_csv(CITY_DATA[city])

    #convert StartTime column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #extract month & day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week']= df['Start Time'].dt.weekday_name

    #extract hour from Start Time to create new columns
    df['start_hour'] = df['Start Time'].dt.hour

    #filter by month
    if month != 'all':
        #use index of moths list to get corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        #filter by month to creat new DataFrame
        df = df[df['month']== month]

    #filter by day
    if day != 'all':
        #filter by day of week to create new DataFrame
        df = df[df['day_of_week']== day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()[0]
    print('Most Common Month: ', most_common_month)


    # display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('Most Common Day: ',  most_common_day)


    # display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['start_hour'].mode()[0]
    print('Most Common Starting Hour: ', most_common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_used_start_station = df['Start Station'].mode()[0]
    print('Most Used Start Station: ',most_used_start_station)


    # display most commonly used end station
    most_used_end_station = df['End Station'].mode()[0]
    print('Most Used End Station: ',most_used_end_station)


    # display most frequent combination of start station and end station trip
    most_used_combination_of_stations = (df['Start Station']+'||'+ df['End Station']).mode()[0]
    print('Most Frequent Combination of Start and End Stations: ',str(most_used_combination_of_stations.split('||')))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time: ', total_travel_time)


    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Average Travel Time: ', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Count of User Types: ', df['User Type'].value_counts())


    # Display counts of gender
    if 'Gender' in df:
        print('\nCounts Concering Gender:')
        if 'Gender' == 'Male':
            print('Male Travelers Count: ', df['Gender'].value_counts())
        if 'Gender' == 'Female':
            print('Female Travelers Count: ', df['Gender'].vaue_counts())


    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print('Earliest Year of Birth: ', df['Birth Year'].min())
        print('Most Recent Year of Birth: ', df['Birth Year'].max())
        print('Most Common Year of Birth: ', df['Birth Year'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#show raw data, 5 rows at a time, per user request
def raw_data_display(df):
    i=0
    see_raw_data = input('Would you like to view five rows of raw data? \nEnter yes or no.\n')
    while see_raw_data.lower() == 'yes':
        print(df.iloc[i:i +5])
        i += 5
        see_raw_data = input('Would you like to view the next five rows of raw data? \nEnter yes or no.\n')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        raw_data_display(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
