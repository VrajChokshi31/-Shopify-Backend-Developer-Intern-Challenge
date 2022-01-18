# Shopify BackEnd Developer Intern Challenge - Summer 2022

![alt text](https://github.com/VrajChokshi31/-Shopify-Backend-Developer-Intern-Challenge/blob/main/shopify.jpg?raw=true)

This repo includes the project made by me for the shopify intern challenge. It requires me to build an inventory tracking web application which can implement the basic CRUD functionality.
The main aim of the web application is that one should able to:-

Create inventory items

Edit Them

Delete Them

View a list of them.

Also it requires to implement one of the several features given in the instruction pdf. 
I have implemented the feature " Push a button export product data to a CSV".

I have also included the zip file for anyone who has trouble downloading the project via the normal method. 

## Technologies Used

I have use Python as the primary language and Django as the backend framework.

## Installation 

If you don't have python in your system follow this [link](https://docs.python.org/3/using/windows.html).

Use the following command to install django.

```bash
py -m pip install django
```
Now change the directory to the location where you have downloaded the folder mysite.

```bash
cd mysite
```
Also run the following command.
```bash
py -m pip install django-better-choices
```
Now run the server using the following command.
```bash
py manage.py runserver
```
Go to the web browser and type:- http://localhost:8000/shop/

You can now see that the application is working.

## Usage
By following the above instructions and running on the localhost we get the screen as below.


https://github.com/VrajChokshi31/-Shopify-Backend-Developer-Intern-Challenge/blob/main/Screenshot%20(23).png

We can see various tabs like Add Item, View Item, Modify Item, Delete Item and Export.

![alt text](https://github.com/VrajChokshi31/-Shopify-Backend-Developer-Intern-Challenge/blob/main/Screenshot%20(23).png?raw=true)

The Add Item requires to fill the form which includes which as the serial number as primary key.

![alt text](https://github.com/VrajChokshi31/-Shopify-Backend-Developer-Intern-Challenge/blob/main/Screenshot%20(24).png?raw=true)

The View Item tab opens the all the records that have been added as shown below.


![alt text](https://github.com/VrajChokshi31/-Shopify-Backend-Developer-Intern-Challenge/blob/main/Screenshot%20(25).png?raw=true)

The Modify Item requires the serial number and other columns which we need to modify.


![alt text](https://github.com/VrajChokshi31/-Shopify-Backend-Developer-Intern-Challenge/blob/main/Screenshot%20(26).png?raw=true)

The Delete Item requires the serial number of the data we need to delete.


![alt text](https://github.com/VrajChokshi31/-Shopify-Backend-Developer-Intern-Challenge/blob/main/Screenshot%20(27).png?raw=true)

The Export tab converts our data to a csv file. This the feature I have implemented from all the features given in the instructions.


![alt text](https://github.com/VrajChokshi31/-Shopify-Backend-Developer-Intern-Challenge/blob/main/Screenshot%20(28).png?raw=true)

## Contributor
Vraj Chokshi.

## License
[MIT](https://choosealicense.com/licenses/mit/)
