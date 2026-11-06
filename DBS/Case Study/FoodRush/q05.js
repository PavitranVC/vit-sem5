db = db.getSiblingDB("foodrush");

// Q5. What are the total revenue, order count and average order value of delivered orders?
db.orders.aggregate([
  { $match: { status: "Delivered" } },
  { $group: { _id: null, delivered_orders: { $sum: 1 }, total_revenue: { $sum: "$total" }, avg_order_value: { $avg: "$total" } } },
  { $project: { _id: 0, delivered_orders: 1, total_revenue: 1, avg_order_value: { $round: ["$avg_order_value", 2] } } }
]);
