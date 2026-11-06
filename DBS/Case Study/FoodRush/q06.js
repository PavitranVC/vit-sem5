db = db.getSiblingDB("foodrush");

// Q6. Which 3 restaurants earn the most revenue from delivered orders?
db.orders.aggregate([
  { $match: { status: "Delivered" } },
  { $group: { _id: "$restaurant_id", orders: { $sum: 1 }, revenue: { $sum: "$total" } } },
  { $lookup: { from: "restaurants", localField: "_id", foreignField: "_id", as: "restaurant" } },
  { $unwind: "$restaurant" },
  { $project: { _id: 0, restaurant: "$restaurant.name", city: "$restaurant.city", orders: 1, revenue: 1 } },
  { $sort: { revenue: -1 } },
  { $limit: 3 }
]);
