## Description

This repository contains a Python implementation of a contact management system built using object-oriented programming principles.
The project demonstrates how to model contacts and phone numbers using custom classes, organize records in an address book, validate user data, and handle errors with custom exceptions.

## Technologies

* Python
* Object-Oriented Programming (OOP)
* Classes and inheritance
* Custom exceptions
* `collections.UserDict`
* Lists and dictionaries
* Data validation
* Encapsulation and class methods

## Functionality

### Contact and Phone Management

The application provides a structured system for managing contact records.
It allows users to:
* create contact records with names and phone numbers;
* add multiple phone numbers to a contact;
* find a specific phone number;
* edit an existing phone number;
* remove a phone number from a contact;
* delete contacts from the address book;
* display stored contact information.

### Data Validation

The `Phone` class validates phone numbers before adding them to a contact.
The implementation ensures that a phone number:
* contains exactly 10 digits;
* consists only of numeric characters.

### Address Book

The `AddressBook` class extends `UserDict` and provides methods for:
* adding new contact records;
* finding contacts by name;
* deleting contacts;
* displaying all stored records.

### Error Handling

The project includes custom exception classes for handling invalid contact operations and demonstrates validation through exceptions when working with phone numbers and records.

## Links

GitHub: https://github.com/Bartmanskiy/goit-algo-hw-06
