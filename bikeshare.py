import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():chicago

print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
print('Would you like to se data for Chicago,New York City or Washington?')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # Get input.
citya = input('Give me your city:  ')
city =  citya.lower()

    # TO DO: get user input for month (all, january, february, ... , june)
print('Would you like to filter the data by month, day, both or not at all? Type "all" for no time filter.')
print('Which month? January, February, March, April, May or June?')
montha = input('Give me a month: ');
month = montha.lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
print('Which day? all, monday, tuesday, ... sunday')
daya = input('Give me name of day: ');
day = daya.lower()

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
    df = pd.read_csv(CITY_DATA[city])

    # The main code block is below; do not edit this

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df
df = load_data(city, month, day)

#Show table by five row at the time.
# ilock hints from https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/
n = 0
l = 5
show_more = 'y'
while show_more == 'y':
     #show_more = 'y'

   print (df.iloc[n:l]) #print from n row to l row in table
   n = n + 5 #adding upp from n
   l= l + 5  #adding up from l
   show_more = input("\nWould you like to show more? (y or n) ")



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""


    # TO DO: display the most common month
common_month = df['month'].mode()[0]
print('Most Comon Month:', common_month)

    # TO DO: display the most common day of week
common_day = df['day_of_week'].mode()[0]
print('Most Comon Day Of Week:', common_day)
    # TO DO: display the most common start hour
common_start_hour = df['Start Time'].mode()[0]
print('Most Comon Start Hour: ', common_start_hour)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

   # print('\nCalculating The Most Popular Stations and Trip...\n')
    # TO DO: display most commonly used start station
common_start_station = df['Start Station'].describe()
print('Most Comon Start Station:', common_start_station)
# TO DO: display most commonly used end stat     common_end_station = df['End Station'].describe()
common_end_station = df['End Station'].describe()
print('Most Comon End Station:', common_end_station)
# TO DO: display most frequent combination of start station and end station trip


freq_start_end_station = df.groupby(['Start Station','End Station']).size().nlargest(2)
print('Most Comon Start-End Stations:', freq_start_end_station)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

   # print('\nCalculating Trip Duration...\n')


total_travel_time = df['Trip Duration'].sum()
print('Total travel time:', total_travel_time)

    # TO DO: display mean travel time
mean_travel_time = df['Trip Duration'].mean()
print('Mean travel time:', mean_travel_time)


def user_stats(df):
    """Displays statistics on bikeshare users."""


       # TO DO: Display counts of user types
count_user_types = df['User Type'].nunique()
print('Numbers of User Types:', count_user_types)
# Copy from answer at student hub

if 'Gender' in df:
#Display counts of gender
        female = df['Gender'].str.count('Female').sum()
        male = df['Gender'].str.count('Male').sum()
        unknown = len(df) - female - male
        print('There are {} females, {} males, and {} unknown Customers.'.format(int(female), int(male), int(unknown)))
        #Display earliest, most recent, and most common year of birth
else:
         #do nothing
        print('Table has no Gender.')

if 'Birth Year' in df:
    oldest = min(df['Birth Year'])
    youngest = max(df['Birth Year'])
    avg_age = df['Birth Year'].mean()
    print('Oldest DOB is:', int(oldest))
    print('The youngest DOB is:', int(youngest))
    print('Avg DOB is:', avg_age.round(2))
else:
         #do nothing
        print('Table has no Birth Year.')


def main():
    while True:
        #city, month, day = get_filters()
        #df = load_data(city, month, day)
        #show_table(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
