db = db.getSiblingDB("foodrush");

// Q1. How many orders ended in each status (Delivered vs Cancelled)?
db.orders.aggregate([
  { $group: { _id: "$status", orders: { $sum: 1 } } },
  { $sort: { orders: -1 } }
]);
