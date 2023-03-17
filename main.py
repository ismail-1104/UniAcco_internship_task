import csv
import pandas as pd
# import argparse
# parser = argparse.ArgumentParser()

# with open('new.txt', 'r') as txt_file:
#     stripped = (line.strip() for line in txt_file)
#     lines = (line.split(",") for line in stripped if line)

#     with open('new.csv', 'w') as csv_file:
#         write = csv.writer(csv_file)
#         write.writerow(('NAME', 'AGE', 'INCOME'))
#         write.writerows(lines)

df = pd.read_csv("Income.csv")

while (1):
    print("\n\n\nEnter your operation.")
    print("1 -  No. of Rows and columns.")
    print("2 - Calculate mean.")
    print("3 - filter data")
    print("4 - Sort data")
    print("0 - exit")

    ch = int(input("Enter your choice : "))

    if (ch == 1):
        no_of_rows = len(df.axes[0])
        no_of_cols = len(df.axes[1])

        print("No. of rows : ", no_of_rows)
        print("No. of columns : ", no_of_cols)

    elif (ch == 2):
        val = df.mean(numeric_only=True)
        print(val)

    elif (ch == 3):
        print(df[(df['age'] <= 30) & (df['income'] > 50000)
              & (df['name'] == 'Ismail')])

    elif (ch == 4):
        print("\nInput CSV file = \n", df)

        # sorting according to multiple columns
        df.sort_values(["age"], axis=0, ascending=True,
                       inplace=True, na_position='first')

        print("\nSorted CSV file = \n", df)

    elif (ch == 0):
        exit()
