import os
import join
import plot

def main():
    join.create_csv()
    plot.plot()
    os.remove('total.csv')

if __name__ == '__main__':
    main()