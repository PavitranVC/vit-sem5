db = db.getSiblingDB("foodrush");

// Q4. Which Cash-on-Delivery orders are worth more than Rs. 500, highest first?
db.orders.find(
  { payment_method: "COD", total: { $gt: 500 } },
  { _id: 1, customer_id: 1, restaurant_id: 1, total: 1, status: 1 }
).sort({ total: -1 });
