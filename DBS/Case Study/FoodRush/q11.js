db = db.getSiblingDB("foodrush");

// Q11 (bonus). How fast is each delivery agent? (average delivery time and workload)
db.orders.aggregate([
  { $match: { status: "Delivered" } },
  { $group: { _id: "$agent_id", deliveries: { $sum: 1 }, avg_minutes: { $avg: "$delivery_minutes" } } },
  { $lookup: { from: "delivery_agents", localField: "_id", foreignField: "_id", as: "agent" } },
  { $unwind: "$agent" },
  { $project: { _id: 0, agent: "$agent.name", city: "$agent.city", vehicle: "$agent.vehicle", deliveries: 1, avg_minutes: { $round: ["$avg_minutes", 1] } } },
  { $sort: { avg_minutes: 1, agent: 1 } }
]);
