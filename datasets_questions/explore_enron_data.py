#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# counting no of people in dataset
print 'No. of people in enron dataset : {0}'.format(len(enron_data))

# counting no of features in dataset
print 'No. of features in enron dataset for each person :{0}'.format(len(enron_data.values()[0]))

# Finding POIs in the Enron Data
pois = [x for x, y in enron_data.items() if y['poi']]
print 'No of POIs in enron datset : {0}'.format(len(pois))

# Total value of the stock belonging to James Prentice
print 'Total value of the stock belonging to James Prentice is : {0}'.format(enron_data["PRENTICE JAMES"]["total_stock_value"])

# Total messages from WESLEY COLWELL to POIs
print 'Total messages from WESLEY COLWELL to POIs are : {0}'.format(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])

# value of stock options exercised by Jeffrey K Skilling
print 'Total value  of stock options exercised by Jeffrey K Skilling is : {0}'.format(enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]
                                                                                      )

# who took home most of the money
people = ("SKILLING JEFFREY K", "LAY KENNETH L", "FASTOW ANDREW S")
person = ""
money = 0

for i in people:
    if money < enron_data[i]['total_payments']:
        money = enron_data[i]['total_payments']
        person = i

print "Of these three individuals (Lay, Skilling and Fastow), who took home the most money: {0},{1}".format(person, money)

# folks with quantified salary and known email addresses
no_salary, no_email_add = 0, 0
for i in enron_data:
    if enron_data[i]['salary'] != "NaN":
        no_salary += 1
    if enron_data[i]['email_address'] != "NaN":
        no_email_add += 1

print "folks with quantified salary: {0} and with known email addresses:{1}".format(no_salary, no_email_add)

# people with  total payments as NaN
no_total_pay = 0
for i in enron_data:
    if enron_data[i]['total_payments'] == "NaN":
        no_total_pay += 1

print 'Percentage of people with NaN payments : {0}'.format(no_total_pay / float(len(enron_data)))

# people with  poi having total payments as NaN
no_total_pay_poi, no_poi = 0, 0
for i in enron_data:
    if enron_data[i]['poi']:
        no_poi += 1
        if enron_data[i]['total_payments'] == "NaN":
            no_total_pay_poi += 1

print 'Percentage of people(with person of interest) having total payments as NaN  : {0}'.format(no_total_pay_poi / float(no_poi))

# after adding 10 more points
print len([enron_data[person]['total_payments'] for person in enron_data if (enron_data[person]['total_payments'] == 'NaN')])
