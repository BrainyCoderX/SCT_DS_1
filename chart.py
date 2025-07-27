import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('hotel_bookings.csv')


data['customer_type'].value_counts().plot(kind='bar', color='mediumseagreen')
plt.title('Distribution of Customer Types')
plt.xlabel('Customer Type')
plt.ylabel('Number of Bookings')
plt.grid(True)
plt.tight_layout()
plt.show()