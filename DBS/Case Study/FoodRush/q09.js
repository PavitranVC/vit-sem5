db = db.getSiblingDB("foodrush");

// Q9. Which cuisines get the best average rating (cuisines with at least 5 reviews)?
db.reviews.aggregate([
  { $lookup: { from: "restaurants", localField: "restaurant_id", foreignField: "_id", as: "restaurant" } },
  { $unwind: "$restaurant" },
  { $unwind: "$restaurant.cuisine" },
  { $group: { _id: "$restaurant.cuisine", reviews: { $sum: 1 }, avg_rating: { $avg: "$rating" } } },
  { $match: { reviews: { $gte: 5 } } },
  { $project: { _id: 0, cuisine: "$_id", reviews: 1, avg_rating: { $round: ["$avg_rating", 2] } } },
  { $sort: { avg_rating: -1, reviews: -1, cuisine: 1 } }
]);
