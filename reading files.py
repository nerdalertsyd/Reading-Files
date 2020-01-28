#-------------------------
#Reading Files
#Sydney Loerzel
#Jan 24, 2020
#-------------------------

#--------------Dicts--------------
age = {}

def read(file):
    ages = open (file, 'r')
    bts_ages = ages.read().split(',')
    print(bts_ages)
    item = 0
    while item < (len(bts_ages)):
        age[bts_ages[item]] = bts_ages[item + 1]
        item = item + 2
    ages.close()
    return file

def birthday():
    print("It is now Jeongguks birthday")
    age['Jeongguk'] = '23'
    print("Jeongguk is now", age['Jeongguk'])
    
def update(file):
    print("The original file needs to be updated with Jeongguks birthday")
    with open(file, 'w') as f:
        for akey in age.keys():
            f.write(akey + ',')
            f.write(age[akey])
            if akey != 'Jeongguk':
                f.write(',')
    print("Open the file externally to make sure the update worked")
    print("Have a good day")
    
read('bts.txt')
print(age)
birthday()
print(age)
update('bts.txt')