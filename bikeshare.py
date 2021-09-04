import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Enter the city :").lower()
        if city not in ['chicago', 'new york city', 'washington']:
            print("Not a choice, try again.")
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Enter the month or enter all:").lower()
        if month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            print("Not a choice, try again.")
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Enter the day or enter all:").lower()
        if day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'sunday']:
            print("Not a choice, try again.")
        else:
            break

    print('-' * 40)
    return city, month, day

# function to display data
def display_data(city):
    df = pd.read_csv(CITY_DATA[city])
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()
    start_loc = 0
    view_display = view_data
    while (view_display == 'yes'):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_display = input("Do you wish to continue?: ").lower()

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

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        # filter by day of week to create the new dataframe
        
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    MCM = df['month'].mode()
    print('the most common month: ', MCM)
    # TO DO: display the most common day of week
    MCD = df['day_of_week'].mode()
    print('the most common day of week :', MCD)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    MCSH = df['hour'].mode()[0]
    print('the most common start hour :', MCSH)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    MCUSS = df['Start Station'].mode()
    print('the most commonly used start station: ', MCUSS)
    # TO DO: display most commonly used end station
    MCUES = df['End Station'].mode()
    print('the most commonly used end station: ', MCUES)

    # TO DO: display most frequent combination of start station and end station trip
    MFC = (df['Start Station'] + df['End Station']).mode()[0]
    print('the most frequent combination of start station and end station trip: ', MFC)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    TTT = df['Trip Duration'].sum()
    print('the total travel time', TTT)

    # TO DO: display mean travel time
    MTT = df['Trip Duration'].mean()
    print('the mean travel time', MTT)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    COUT = df['User Type'].value_counts()
    print('the counts of user types: ', COUT)

    # TO DO: Display counts of gender
    try:
        COG = df['Gender'].value_counts()
        print('the counts of gender: ', COG)
        # TO DO: Display earliest, most recent, and most common year of birth
        EYB= df['Birth Year'].min()
        MRYB = df['Birth Year'].max()
        MCYB = df['Birth Year'].mode()
        print('the earliest: ', EYB)
        print('the most recent: ', MRYB)
        print('the most common: ', MCYB)
    except Exception as e:
        print(e)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        display_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()