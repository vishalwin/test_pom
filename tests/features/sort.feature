Feature: Product Sorting Functionality

Scenario: Sort product name A to Z
Given user open login page
When user enters valid credetials
And user selects "Name (A to Z)" from dropdown
Then products should sort successfully by name in ascending order

@smoke
Scenario: Sort product name Z to A
Given user open login page
When user enters valid credetials
And user selects "Name (Z to A)" from dropdown
Then products should sort successfully by name in descending order

Scenario: Sort product price low to high
Given user open login page
When user enters valid credetials
And user selects "Price (low to high)" from dropdown
Then products should sort successfully by price in ascending order

Scenario: Sort product price high to low
Given user open login page
When user enters valid credetials
And user selects "Price (high to low)" from dropdown
Then products should sort successfully by price in descending order
