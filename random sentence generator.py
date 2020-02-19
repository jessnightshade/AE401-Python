import random
namelist=['Sally','Bob','I']
verblist=['went to','ran from','hid in']
nounlist=['the market.','a bear.','a box.']
name=random.choice(namelist) #choose random word from namelist
verb=random.choice(verblist) #choose random word from verblist
noun=random.choice(nounlist) #choose random word from nounlist
print(name,verb,noun)