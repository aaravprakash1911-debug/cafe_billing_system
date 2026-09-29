
# Cafe Ordering System

## Overview

This is a command-line restaurant ordering system written in Python. It lets a customer see the menu pick items to order and get a bill. All through text prompts in the terminal. It's a beginner- project that uses basic Python skills like dictionaries, loops, conditionals and handling user input.

## Features

- Shows a message and the full list of menu items with prices.

- Lets the customer type the name of an item they want to order.

- Checks if the entered item exists on the menu before adding it.

- Allows the customer to keep adding items one by one until they are done.

- Keeps a running total of the bill as items are added.

- Execute the program and do not crash even when you enter the item which is not present in the menu.

- Displays the final total amount and a thank-you message at the end.

## Tools Used

- **Language:** Python 3

- **Concepts used:** Dictionaries, if/ statements while loops, f-strings, `input()` function for user interaction

- **Tools:** Any code editor (like VS Code or PyCharm) or just a plain terminal

- No extra libraries are needed. Everything works using Python’s built-in features

## Steps to Install. Run the Project

1. Make sure Python 3 is installed on your computer.

You can check by typing `python --version` or `python3 --version` in the terminal.

If its not installed go to [python.org](https://www.python.org/downloads/). Download it.

2. Save the project code into a file called `restaurant.py`.

3. Open your terminal. Command prompt.

4. Go to the folder where you saved `restaurant.py`. For example:

```

cd path/to/your/folder

```

5. Run the program using:

```

python restaurant.py

```

(On some systems you may need to use `python3` )

6. Follow the instructions on the screen to place your order.

## Instructions for Testing

You can test the program manually by trying these scenarios:

1. ** Item test** – Try entering a real item from the menu like `Pizza` and make sure it gets added and the total updates correctly.

2. **Invalid item test** – Enter something not on the menu like `Sandwich`. Check that the program says "item not available" instead of crashing.

3. **Multiple orders test** – Order one item then answer `Yes` when asked if you want to add another. Then choose a valid item and confirm both prices are added together.

4. **Stop ordering test** – After your order say anything other than `Yes` (, like `No`) when asked to add more items. Make sure the program stops and shows the bill.

5. **Case sensitivity test** – Try entering an item name in lowercase when the menu lists it in uppercase (or vice versa) like `pasta` of `Pasta`. The program should show "item not available" but not crash.

6. ** Total test** – Add up the prices of all the items you ordered and compare them to the total shown at the end. They should match.

## Screenshots

A screenshot of the program output is below:

```

Welcome To Our Restaurant

Pizza: Rs150

Pasta: Rs120

Burger: Rs80

Coffee: Rs60

Tea: Rs50

Enter the name of the item you want to order = Pizza

Your item Pizza has been added to your order

Do you want to add another item? (Yes/No) No

The total amount of items to pay is 150

Thank You For Visiting Our Restaurant

```
