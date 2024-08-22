#Edit of code
#----Modules----#
import pandas as pd
import matplotlib.pyplot as plt

#----Global Variables----#
quit = False

#----Setup dataframe and query it here prior to creating visualisation and UI functions----#
original_df = pd.read_csv('data/FINAL_DATASET.csv')


# big_mac_df = pd.read_csv('data/big_mac_aud.csv',2
                            #header=None,
                            #names=['Country', 'Local', 'AUD', 'Date'])

#----Define Functions Below----#
def showOriginalData():
    print(original_df)


def showCharts():
    original_df.plot(
                    kind='bar',
                    x='KD',
                    y='Win Rate',
                    color='blue',
                    alpha=0.3,
                    title='Correlation Between KD and Win Rate')
    plt.show()

try:
    # Some code that might raise an exception
    original_df.plot(
        kind='bar',
        x='KD',
        y='Win Rate',
        color='blue',
        alpha=0.3,
        title='Correlation Between KD and Win Rate')
    plt.show()
except Exception as e:
    print('Error occurred while showing charts')
    print(f'Caught {e=}, {type(e)=}')

    print("""Welcome to the Big Mac Data Extraordinaire!
          
    Please select an option:
    1 - Show the original dataset
    2 - Show data for specific
    3 - Visualise the correlation between KD and Win Rate
    4 - Quit Program
        """)
    
    try:
        choice = int(input('Enter Selection: '))

        if choice == 1:
            showOriginalData()
        #elif choice == 2:
            
        elif choice == 3:
            showCharts()
        elif choice == 4:
            quit = True
        else:
            print('A number between 1 and 4, come on!')

    except:
        print('Enter a number, it is not that hard.')



   

#----Main program----#
#while not quit:
def userOptions():
    options = {
        1: ("Show the original dataset", showOriginalData),
        2: ("Show data for a specific week", showWeekData),
        3: ("Visualise the correlation between KD and Win Rate", showCharts),
        4: ("Quit Program", None)
    }
    
def main():
    global quit
    print("Welcome to the Valorant Stats Analyzer!")
    while not quit:
        userOptions()
    print("Thank you for using the Valorant Stats Analyzer. Goodbye!")

if __name__ == "__main__":
    main()

