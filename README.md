1. Ability to create an account for trading.
2. Ability to "add" cash to account.
3. Ability to go and do some trading.


1. Ability to create an account for trading.
    1. create account database model (add boolean field to check if user is blacklisted) table: account
    2. create a form for user registration/ login
    3. create flask endpoint and add functionality to register new user (Could be some additional requirements: must be 21 years old) + add template
    4. create flask endpoint and add functionality to login existing user + add template
    5. create functionality to reset users password if it is forgotten.
    6. Add ability to log out.
    7. Add functionality to amend user details.
    8. Create a page for viewing users balance.
    9. Show user information
    10. Show trade history
    11. 

2. Ability to manipulate cash to account.
    1. create account_cash_transactions database model table. (should contain only cash). relationship account one : account_cash_transactions many
    (account_id: int, amount: float, creation_date: datetime, status: ["TOP-UP", "BUYING-SHARES", "SELLING-SHARES", "WITHDRAWAL"])
    2. form to add cash
    3. create flask endpoint and add functionality

3. Ability to go and do some trading.
    1. Find api that gives us stock price.
    2. add a page for getting particular stock price
    3. create stocks database model (quantity: int, ticker: str, price: float, transaction_type: ["BUY", "SELL"] , creation_date: datetime, account_id: int) relationship account one : stocks many 


Backend:
1. Create Database models
2. create endpoint "users/":
    1. POST - Creates new user
    2. GET with <id> gets user by id
    3. GET with <email> gets user by email
    4. PUT with id updates user information
    5. DELETE deletes user

3. Ability to manipulate cash to account.
    1. create endpoint "account_cash_transactions/"
        1. POST - creates new cash transaction
        2. GET - with <account_id> return all account account_cash_transactions sort by creation_date: desc
        3. GET - with <account_id> get users cash balance

4. Ability to go and do some trading.
    1. create endpoint "stock/"
        GET <ticker> get ticker current price
        POST "stock/sell/<account_id>/<ticker>"
        POST "stock/buy/<account_id>/<ticker>"