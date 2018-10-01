# Pizza Ordering App
> Requirement

Users may order one or more pizzas, where each pizza may be either: 
<ul>
  <li>Small</li>
  <li>Medium</li>
  <li>Large</li>
</ul>
Small pizzas cost $5, medium pizzas cost $8 and large pizzas cost $12.
All pizzas come on a tomato base (for our pizza shop, this will be the only option), and will have the topping
cheese by default, at no extra cost. Users may choose up to a maximum of four additional toppings (bringing
the total to five) from the following list, where each topping adds an additional $1 to the price of the pizza:
<ul>
  <li>Bacon</li>
  <li>Olives</li>
  <li>Ham</li>
  <li>Mushrooms</li>
  <li>Pineapple</li>
  <li>Salami
  <li>Anchovies</li>
</ul>
A pizza order consists of an order for one or more pizzas, where each pizza has a size, and may optionally include a list
of up to four additional toppings.
Each pizza order must be marked as either to be collected or to be delivered.
If the pizza is to be collected then the order requires a name and a phone number to be valid.
If the pizza is to be delivered then a name, phone number and address are required to be valid. In addition, if the order
total is less than $30 then an $8 delivery fee is added to the total.
The application must be error tolerant and capable of accepting keyboard input to store a number of pizza orders in
memory (they do not have to be persisted to file), as well as displaying an order summary which include details of all
orders, including:
<ul>
  <li>The details of each pizza in the order</li>
  <li>The total cost of the order</li>
  <li>The name, phone number and (if required) address of the person who made the order</li>
</ul>
