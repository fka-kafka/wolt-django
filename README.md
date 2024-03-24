# Wolt Summer 2024 Engineering Internships Pre-Assignment source code

See [original repository](https://github.com/woltapp/engineering-internship-2024) for details.

Technologies used:

- React + TypeScript + Python

## Delivery Fee Calculator

The goal of the assignment was to showcase my coding skills and ability to develop features. Reviewers should put weight on three main aspects: code quality, maintainability, and testing. The task was to write a delivery fee calculator. This code is needed when a customer is ready with their shopping cart and we’d like to show them how much the delivery will cost. The delivery price depends on the cart value, the number of items in the cart, the time of the order, and the delivery distance.

### Input fields

| Field             | Type        | Description                                                                                             | Example value                            |
| :---------------- | :---------- | :------------------------------------------------------------------------------------------------------ | :--------------------------------------- |
| Cart value        | Float       | Value of the shopping cart in euros.                                                                    | **20**                                   |
| Delivery distance | Integer     | The distance between the store and customer’s location **in meters**.                                   | **2235** (2235 meters = 2.235 km)        |
| Cart items        | Integer     | The **number of items** in the customer's shopping cart.                                                | **4** (customer has 4 items in the cart) |
| Order time        | Date + Time | The date/time when the order is being made (see rules-section how rush hours affect the delivery price) | ISO format                               |

#### Backend Specification

Implementation of a HTTP API (single POST endpoint) which calculates the delivery fee based on the information in the request payload (JSON) and includes the calculated delivery fee in the response payload (JSON).

#### Request

Example:

```json
{
  "cart_value": 790,
  "delivery_distance": 2235,
  "number_of_items": 4,
  "time": "2024-01-15T13:00:00Z"
}
```

##### Field details

| Field             | Type    | Description                                                                | Example value                            |
| :---------------- | :------ | :------------------------------------------------------------------------- | :--------------------------------------- |
| cart_value        | Integer | Value of the shopping cart **in cents**.                                   | **790** (790 cents = 7.90€)              |
| delivery_distance | Integer | The distance between the store and customer’s location **in meters**.      | **2235** (2235 meters = 2.235 km)        |
| number_of_items   | Integer | The **number of items** in the customer's shopping cart.                   | **4** (customer has 4 items in the cart) |
| time              | String  | Order time in UTC in [ISO format](https://en.wikipedia.org/wiki/ISO_8601). | **2024-01-15T13:00:00Z**                 |

#### Response

Example:

```json
{ "delivery_fee": 710 }
```

| Field        | Type    | Description                           | Example value               |
| :----------- | :------ | :------------------------------------ | :-------------------------- |
| delivery_fee | Integer | Calculated delivery fee **in cents**. | **710** (710 cents = 7.10€) |

## How to run

1. ### dev environment

- #### client setup

  ```bash
  cd client/app/
  npm install
  npm run dev
  ```

- #### server setup

  - create a virtual environment and activate it

  1. **Windows :**

  ```bash
  python -m venv .venv
  source .venv\Scripts\activate
  ```

  2. **MacOS and Linux :**

  ```bash
  python -m venv .venv
  source .venv/bin/activate
  ```

  - In "settings.py", toggle "DEBUG = False" to "True" if set

  - Install the dependencies

  ```bash
  pip install -r requirements.txt
  ```

  - Start the server

  ```bash
  ./manage.py runserver
  ```

2. ### prod environment

- create a virtual environment and activate it

  1. **Windows :**

  ````bash
    python -m venv .venv
    source .venv\Scripts\activate
  ````

  2. **MacOS and Linux :**

  ```bash
  python -m venv .venv
  source .venv/bin/activate
  ```

- Install the dependencies

  ```bash
  pip install -r requirements.txt
  cd server/
  ```

- In "settings.py", toggle "DEBUG = True" to "False" if set.
  Navigate back to the root directory and run

  ```bash
  ./manage.py runserver
  ```
