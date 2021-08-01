pip install nsetools

# importing nse from nse tools
from nsetools import Nse

# creating a Nse object
nse = Nse()

# printing Nse object
print(nse)


# importing nse from nse tools
from nsetools import Nse

# creating a Nse object
nse = Nse()

# getting quote of the sbin
quote = nse.get_quote('sbin')

# printing comapny name
print(quote['companyName'])

# printing buy price
print("Buy Price : " + str(quote['buyPrice1']))


# importing nse from nse tools
from nsetools import Nse

# creating a Nse object
nse = Nse()

# getting quote of the sbin
quote = nse.get_quote('sbin')

# printing comapny name
print(quote['companyName'])

# printing average price
print("Average Price : " + str(quote['averagePrice']))


