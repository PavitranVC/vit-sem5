db = db.getSiblingDB("foodrush");

// Q7. How do orders, revenue and cancellation rate change month by month?
db.orders.aggregate([
  { $group: {
      _id: { $dateToString: { format: "%Y-%m", date: "$order_date" } },
      total_orders: { $sum: 1 },
      cancelled: { $sum: { $cond: [{ $eq: ["$status", "Cancelled"] }, 1, 0] } },
      revenue: { $sum: { $cond: [{ $eq: ["$status", "Delivered"] }, "$total", 0] } }
  } },
  { $project: {
      _id: 0, month: "$_id", total_orders: 1, cancelled: 1, revenue: 1,
      cancellation_rate_pct: { $round: [{ $multiply: [{ $divide: ["$cancelled", "$total_orders"] }, 100] }, 1] }
  } },
  { $sort: { month: 1 } }
]);
