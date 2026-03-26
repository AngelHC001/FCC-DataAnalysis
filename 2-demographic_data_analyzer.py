import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    
    # How many of each race are represented in this dataset? 
    #This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()
    
    # What is the average age of men?
    male_people = df[df['sex'] == 'Male']
    average_age_men = male_people['age'].mean()
    
    # What is the percentage of people who have a Bachelor's degree?
    totalGrades = df['education'].value_counts().sum()
    bachelors = df['education'].value_counts().iloc[2]
    percentage_bachelors = (bachelors / totalGrades) * 100
    
    # What percentage of people with advanced education 
    #(`Bachelors`, `Masters`, or `Doctorate`) make more than 50K? 
    higher_edu = df.loc[(df['education'] == 'Bachelors') |  
                          (df['education'] == 'Masters') |  
                          (df['education'] == 'Doctorate')] 
    
    # What percentage of people without advanced education make more than 50K?
    lower_edu = df.loc[(df['education'] != 'Bachelors') &
                       (df['education'] != 'Masters') & 
                       (df['education'] != 'Doctorate')]
    
    total_higher = higher_edu['salary'].shape[0]
    total_lower = lower_edu['salary'].shape[0]
    
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = higher_edu['salary'].value_counts().iloc[1]
    lower_education =  lower_edu['salary'].value_counts().iloc[1]
    
    # percentage with salary >50K
    higher_education_rich = (higher_education/total_higher) * 100
    lower_education_rich = (lower_education/total_lower) * 100
    
    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    
    # What percentage of the people who work 
    #the minimum number of hours per week have a salary of >50K?
    mask = df['hours-per-week'] == min_work_hours
    num_min_workers = df.loc[mask].shape[0]
    num_min_rich = df.loc[(mask) & (df['salary'] == '>50K')].shape[0]
    rich_percentage = (num_min_rich / num_min_workers) * 100
    
    
    # What country has the highest percentage of people that earn >50K?
    filter1 = df.loc[(df['salary'] == '>50K'),'native-country']
    highest_earning_country = filter1.value_counts().index[0]
    top_country = filter1.value_counts().iloc[0]
    total_world = filter1.value_counts().sum()
    highest_earning_country_percentage = (top_country/total_world) * 100
    
    
    # Identify the most popular occupation for those who earn >50K in India.
    occupations = df.loc[(df['salary'] == '>50K') & (df['native-country'] == 'India'),'occupation']
    top_IN_occupation = occupations.value_counts().iloc[0]
    
    # DO NOT MODIFY BELOW THIS LINE
    
    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)
    
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
    
calculate_demographic_data()


    