db = db.getSiblingDB("foodrush");

// Q8. What are the 5 best-selling dishes by units sold (delivered orders only)?
db.orders.aggregate([
  { $match: { status: "Delivered" } },
  { $unwind: "$items" },
  { $group: {
      _id: "$items.name",
      units_sold: { $sum: "$items.qty" },
      revenue: { $sum: { $multiply: ["$items.qty", "$items.price"] } }
  } },
  { $sort: { units_sold: -1, _id: 1 } },
  { $limit: 5 },
  { $project: { _id: 0, dish: "$_id", units_sold: 1, revenue: 1 } }
]);
