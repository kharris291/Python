# Kevin Harris
# C09515259

import math

def getInputData(datafile):
  data = [line.split(',') for line in file(datafile)]
  for i in range(0, len(data)):
    # make sure there is no whitespaces
    for s in range(len(data[i])):
      data[i][s] = data[i][s].replace(' ','')
    # Cast numebrs to a int to be able to calculate the euclidean
    #age
    data[i][1]=int(data[i][1])
    #capital-gain
    data[i][11]=int(data[i][11])
    #capital-loss
    data[i][12]=int(data[i][12])
    #hours-per-week
    data[i][13]= int(data[i][13])
        
    #remove the return from the end of each line
    data[i][15] = data[i][15].rstrip('\n')
    data[i][15] = data[i][15].rstrip('\t')

  return data

#calculate the euclidean
def euclidean(queried_data,known_data):
  num=0.0
  num= math.sqrt((queried_data[1]-(known_data[1]))**2)
  num= num + math.sqrt((queried_data[11]-known_data[11])**2)
  num= num + math.sqrt((queried_data[12]-known_data[12])**2)
  num= num + math.sqrt((queried_data[13]-known_data[13])**2)
  return num


def getDistances(known_data,queried_data):
  sortedSalaryArray=[]
  number = 0
  catagory_variance = 0
  # Loop over every item in the dataset
  for i in range(len(known_data)):
    # Calculate the euclidean, to get the
    # numerical distribution between the fields
    number = euclidean(queried_data,known_data[i])
    # Calculate the catagorical variance between
    # fields in each row for the known and queried data
    # workclass
    if not(known_data[i][2] == queried_data[2]):
      catagory_variance += 1
    #education
    if not(known_data[i][4] == queried_data[4]):
      catagory_variance += 1
    #ocupation
    if not(known_data[i][7] == queried_data[7]):
      catagory_variance += 1
    #country
    if not(known_data[i][14] == queried_data[14]):
      catagory_variance += 1
    # Add the catagorical to the numerical and add
    # the distance and the index to a list
    number = number + catagory_variance
    sortedSalaryArray.append([number,known_data[i][15]])
  
  # Sort by distance
  sortedSalaryArray.sort()
  return sortedSalaryArray

def knnestimate(known_data,queried_data,resultRange=20):
  
    #retrive distance variance
    sortedSalaryArray = getDistances(known_data, queried_data)
    over50 = 0
    underOrEqual = 0

    # for the top most relivant results in range of k
    # count the number of target variables of each type
    # to determine whether to return a <=50K or a >50K
    for i in range(resultRange):
        if sortedSalaryArray[i][1] == '<=50K':
            underOrEqual = underOrEqual + 1
        else:
            over50 = over50 + 1

    # return the salary with the highest number of
    # top records in it
    if over50 <= underOrEqual:     
      return '<=50K'
    else:
      return '>50K'

def MyMain():
  #read in the training data and the looked for data
  print("Retrieving information")
  my_data=getInputData('trainingset.txt')
  test_data = getInputData('queries.txt')
  
  testResults = []

  over = 0
  under = 0
  print("Calculating results")
  for i in range(0,len(test_data)):
    # Retrieve results by testing each query
    # against the complete training dataset
    test_data[i][15]= knnestimate(my_data, test_data[i])
    testResults.append({'result':test_data[i][0]+','+test_data[i][15]})
    # Calculate the number of fields that are greater than
    # and less than 50K
    if test_data[i][15] == '<=50K':
      under = under +1
    else:
      over = over+ 1

  print('Results retrieved')
  print('Salaries less than or equal to 50K : ',under)
  print('Salaries greater to 50K : ',over)
  print('Saving to file')
  #write testResults to a file
  fileOpen = open("C09515259.txt", "w")
  for i in range(0,len(testResults)):
    print >>fileOpen,testResults[i]['result']

  fileOpen.close()
  
MyMain()
