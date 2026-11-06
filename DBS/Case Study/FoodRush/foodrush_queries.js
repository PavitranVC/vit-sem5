// FoodRush – the 10 case study queries (+1 bonus) for MongoDB / mongosh
// Run the seed script first. Then run each query on its own and take a screenshot of the output.
// Usage: mongosh "<your connection string>"  -> then paste one query at a time
//        (or: mongosh "<uri>" foodrush_queries.js to run them all in one go)

db = db.getSiblingDB("foodrush");

// ======================= SIMPLE QUESTIONS =======================

// Q1. How many orders ended in each status (Delivered vs Cancelled)?
db.orders.aggregate([
  { $group: { _id: "$status", orders: { $sum: 1 } } },
  { $sort: { orders: -1 } }
]);

// Q2. Which vegetarian-only restaurants operate in Vellore or Coimbatore?
db.restaurants.find(
  { is_veg: true, city: { $in: ["Vellore", "Coimbatore"] } },
  { _id: 0, name: 1, city: 1, cuisine: 1, opened_year: 1 }
);

// Q3. Which vegetarian menu items cost less than Rs. 100, cheapest first?
db.menu_items.find(
  { is_veg: true, price: { $lt: 100 } },
  { _id: 0, name: 1, category: 1, price: 1, restaurant_id: 1 }
).sort({ price: 1, name: 1 });

// Q4. Which Cash-on-Delivery orders are worth more than Rs. 500, highest first?
db.orders.find(
  { payment_method: "COD", total: { $gt: 500 } },
  { _id: 1, customer_id: 1, restaurant_id: 1, total: 1, status: 1 }
).sort({ total: -1 });

// Q5. What are the total revenue, order count and average order value of delivered orders?
db.orders.aggregate([
  { $match: { status: "Delivered" } },
  { $group: { _id: null, delivered_orders: { $sum: 1 }, total_revenue: { $sum: "$total" }, avg_order_value: { $avg: "$total" } } },
  { $project: { _id: 0, delivered_orders: 1, total_revenue: 1, avg_order_value: { $round: ["$avg_order_value", 2] } } }
]);

// ======================= COMPLEX QUESTIONS =======================

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

// ======================= BONUS =======================

// Q11 (bonus). How fast is each delivery agent? (average delivery time and workload)
db.orders.aggregate([
  { $match: { status: "Delivered" } },
  { $group: { _id: "$agent_id", deliveries: { $sum: 1 }, avg_minutes: { $avg: "$delivery_minutes" } } },
  { $lookup: { from: "delivery_agents", localField: "_id", foreignField: "_id", as: "agent" } },
  { $unwind: "$agent" },
  { $project: { _id: 0, agent: "$agent.name", city: "$agent.city", vehicle: "$agent.vehicle", deliveries: 1, avg_minutes: { $round: ["$avg_minutes", 1] } } },
  { $sort: { avg_minutes: 1, agent: 1 } }
]);
