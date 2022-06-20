import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# Arrays containing allowed cities, months and days respectivly
cities=['chicago','new york city','washington']
months=['all','january', 'february', 'march', 'april', 'may', 'june','july','august','september','october','november','december']
days=['monday', 'tuesday', 'wednesday', 'thursday','friday','saterday', 'sunday','all']

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
    while True:
        try:
            city=input("Enter city (Ex: chicago, new york city, washington) please: ").lower()
        except Exception as e:
            print("please stick with allowed input")
        if city in cities:
            break
        else:
            print("please make sure to enter value as per above examples")


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month=input("Enter month (Ex:all, january, february, ... , june) please: ").lower()
        except Exception as e:
            print("please stick with allowed input")
        if month in months:
                break
        else:
            print("please make sure to enter value as per above examples")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day=input("Enter day (Ex: all, monday, tuesday, ... sunday) please: ").lower()
        except Exception as e:
            print("please stick with allowed input")
        if day in days:
                break
        else:
            print("please make sure to enter value as per above examples")

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

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int        
        month = months.index(month)    
        # filter by month to create the new dataframe
        df=df[df["month"]==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        day = days.index(day)
        df=df[df["day_of_week"]==day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month_index=df["month"].value_counts().keys()[0]
    print("The most common month is {}".format(months[common_month_index]))
    

    # TO DO: display the most common day of week
    common_day_index=df["day_of_week"].value_counts().keys()[0]
    print("The most common Day of the week is {}".format(days[common_day_index]))
    

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour=df["hour"].value_counts().keys()[0]
    print("The most common start hour is {}".format(common_hour))
    display_raw_data(df["hour"].value_counts())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station=df["Start Station"].value_counts().keys()[0]
    print("The most common Start Station is {}".format(common_start_station))
    

    # TO DO: display most commonly used end station
    common_end_station=df["End Station"].value_counts().keys()[0]
    print("The most common End Station is {}".format(common_end_station))
    

    # TO DO: display most frequent combination of start station and end station trip
    common_start_end_station=df[["Start Station","End Station"]].value_counts().keys()[0]
    print("The most common start and End Stations are {} and {}".format(common_start_end_station[0],common_start_end_station[1]))
    display_raw_data(df[["Start Station","End Station"]].value_counts())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df["Trip Duration"].sum()
    print("The total travel time for all trips are {} mins".format(total_travel_time/60))

    # TO DO: display mean travel time
    average_travel_time=df["Trip Duration"].mean()
    print("The average travel time is {} mins".format(average_travel_time/60))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types=df["User Type"].value_counts()
    print("We have {} {}s and {} {}s".format(user_types.values[0],user_types.keys()[0],user_types.values[1],user_types.keys()[1]))

    # TO DO: Display counts of gender
    try:
        genders=df["Gender"].value_counts()
        print("We have {} {}s and {} {}s".format(genders.values[0],genders.keys()[0],genders.values[1],genders.keys()[1]))
    except Exception as e:
        print("Can't print gender data, it may be missing in selected dataset")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        youngest_birth_year=int(df["Birth Year"].min())
        oldest_birth_year=int(df["Birth Year"].max())
        common_birth_year=int(df["Birth Year"].value_counts().keys()[0])
        print("The youngest year of birth is {} and the oldest is {} and the most common is {}".format(youngest_birth_year,oldest_birth_year,common_birth_year))
    except Exception as e:
        print("Can't print birth dates, as it may be missing in selected dataset")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
        n=0
        while True:
            try:
                display_raw_data=input("Do you want to see (more) raw data? please answer yes if you wish: ").lower()
            except Exception as e:
                print("please stick with allowed input")
            
            if display_raw_data=='yes':
                print(df.iloc[n:(n+5)])
                n+=5        
            else:
                break
        
        return


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
