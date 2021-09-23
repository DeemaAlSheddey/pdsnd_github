"""Project for the nanodegree"""

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    cities= ['Chicago','New York','Washington']
    months=['All','January','February','March','April','May','June']
    days=['All','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    
    print('Hello! Let\'s explore some US bikeshare data!')
    
    while(True):
        city=input('Choose a city (chicago, new york city, washington). \n')
        if city.title() in cities:
                break

    while(True) :           
        month=input('Name a month to filter by, or "all" to apply no month filter \n ' )
        if month.title()  in months:
            break

    while(True) :    
        day=input('Name a day to filter by, or "all" to apply no day filter  \n' )
        if day.title() in days:
           break



    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month.title()) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    
    # TO DO: display the most common month
    import pandas as pd
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print('Most Common month :', common_month)
    # TO DO: display the most common day    
    df['day'] = df['Start Time'].dt.weekday
    popular_day = df['day'].mode()[0]
    print('Most Common Day:', popular_day)
    # TO DO: display the most common hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Hour:', popular_hour)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_SStaion = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_SStaion)

    # TO DO: display most commonly used end station
    popular_EStaion = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_EStaion)

    # TO DO: display most frequent combination of start station and end station trip 
    popular_StartEnd=df.groupby(['Start Station','End Station']).size().idxmax()
    print('Most frequent combination of start station and end station trip :',popular_StartEnd)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # TO DO: display total travel time
    travel_time = pd.to_numeric(df['Trip Duration']).sum()
    print('Total travel time:', travel_time)
    # TO DO: display mean travel time
    avg_time = pd.to_numeric(df['Trip Duration']).mean()
    print('Average trip duration.:', avg_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""
   
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if (city.title()=='Chicago' or city.title()=='New York'):
        gender = df['Gender'].value_counts()
        print(gender)
        
         ##most common
        common_year = df['Birth Year'].mode()[0]
        print('most common year of birth :', common_year)
       # Display earliest
        recent=df['Birth Year'].max()
        print(recent ,' most recent year of birth ')
        ##most recent
        earliest=df['Birth Year'].min()
        print(earliest ,' earliest year of birth ')

    
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    end_loc=5
    while (view_data.lower()=='yes'):
        print(df.iloc[start_loc:end_loc])
        start_loc += 5
        end_loc+=5
        view_data = input("Do you wish to continue?: ")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
