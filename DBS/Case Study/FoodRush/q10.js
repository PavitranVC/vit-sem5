db = db.getSiblingDB("foodrush");

// Q10. Who are the top 5 customers by lifetime spend (customers with 3+ delivered orders)?
db.orders.aggregate([
  { $match: { status: "Delivered" } },
  { $group: { _id: "$customer_id", orders: { $sum: 1 }, total_spent: { $sum: "$total" } } },
  { $match: { orders: { $gte: 3 } } },
  { $sort: { total_spent: -1 } },
  { $limit: 5 },
  { $lookup: { from: "customers", localField: "_id", foreignField: "_id", as: "customer" } },
  { $unwind: "$customer" },
  { $project: { _id: 0, customer: "$customer.name", city: "$customer.city", tier: "$customer.loyalty_tier", orders: 1, total_spent: 1,
                avg_per_order: { $round: [{ $divide: ["$total_spent", "$orders"] }, 2] } } }
]);
