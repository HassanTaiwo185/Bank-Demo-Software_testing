# INFT 1207 – Software Testing and Automation

## Group Number: 6  
## Project Name: Selenium Automation – Guru99 Banking Application  

### Group Members
1. Payathik Manoranjan  
2. Shiraz Khan  
3. Hassan Ayinde  
4. Navid Ahmad  

Submitted to: Faculty, Durham College  

---

## Project Background

This project was originally completed as a **group assignment in April 2025** for the INFT 1207 – Software Testing and Automation course at Durham College.

Although the implementation was completed in April 2025, the project was later added to this GitHub repository for documentation, version control, and portfolio purposes.

---

# 1. Purpose of the Project

The main goal of this project was to make testing a banking web application easier, faster, and more reliable through automation.

Manually testing features such as adding customers, editing accounts, or deleting records can be time-consing and repetitive. To solve this, we built an automation framework using **Python and Selenium WebDriver**.

Our automation framework simulates real user actions on the banking website to verify that:

- Form submissions work correctly  
- Validation messages appear when expected  
- Records can be created, edited, and deleted properly  
- The system handles invalid inputs correctly  

We focused primarily on the **Manager section** of the application because it contains the core banking functionalities.

The objective was not only to automate test cases but also to create a structure that is clean, organized, reusable, and scalable for future testing needs.

---

# 2. Scope of the Project

The project automated nine major modules of the banking application:

- New Customer  
- Edit Customer  
- Delete Customer  
- New Account  
- Edit Account  
- Delete Account  
- Balance Enquiry  
- Mini Statement  
- Customized Statement  

Each module included both **positive and negative test cases**.

For example:
- Valid customer creation
- Blank input validation
- Invalid characters in text fields
- Incorrect account data handling

In total, more than **120 test cases** were designed and implemented.

The scope focused strictly on **functional automation testing**, not performance or security testing.

---

# 3. Software Used

The following tools were used:

### Python
Used as the primary programming language due to its simplicity and strong Selenium integration.

### Selenium WebDriver
Used to automate browser interactions such as:
- Clicking buttons  
- Filling out forms  
- Navigating pages  
- Validating responses  

### PyCharm
Used as the main IDE for writing and organizing code.

### Microsoft Excel
Used to design and manage over 120 test cases.

These tools reflect industry-standard automation practices.

---

# 4. Naming Convention

We followed consistent naming conventions to ensure:

- Code readability  
- Maintainability  
- Clear test case identification  
- Logical file organization  

Test methods and variables were named based on:
- Module name  
- Scenario type (Valid / Invalid)  
- Functionality being tested  

---

# 5. Distribution of Work

Work was divided by module:

| Module | Team Member | Test Cases |
|--------|------------|------------|
| New Customer | Payathik Manoranjan | 28 |
| Edit Customer | Payathik Manoranjan | 20 |
| Delete Customer | Shiraz Khan | 8 |
| New Account | Shiraz Khan | 16 |
| Edit Account | Navid Ahmad | 8 |
| Delete Account | Navid Ahmad | 8 |
| Balance Enquiry | Hassan Ayinde | 7 |
| Mini Statement | Hassan Ayinde | 8 |
| Customized Statement | Hassan Ayinde | 17 |

---

# 6. Approach Used

We used **Selenium WebDriver** to automate browser interactions.

Each test case followed a structured workflow:

### 1. Setup
- Launch browser  
- Open website  
- Maximize window  
- Log in  

### 2. Navigation
- Navigate to assigned module (e.g., New Customer)

### 3. Action
- Perform required operation  
- Use element locators such as:
  - By.ID  
  - By.NAME  
  - By.XPATH  

We primarily used **ID and NAME locators** because they are more reliable and faster than XPath.

### 4. Validation
- Verify expected result  
- Check confirmation messages  
- Validate error messages  

### 5. Closing
- Close browser using `driver.close()`

---

# Implementation Overview

The framework was structured to ensure reusability and clarity.

Each test case follows:

- Setup phase  
- Execution phase  
- Validation phase  
- Cleanup phase  

This structure ensures the framework can easily be expanded in the future.

---

# Conclusion

This project demonstrates how automation testing can:

- Improve software quality  
- Reduce repetitive manual effort  
- Increase efficiency  
- Detect defects early  

It reflects practical application of automation testing concepts learned in the INFT 1207 course.
