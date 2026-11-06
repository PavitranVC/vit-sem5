db = db.getSiblingDB("foodrush");

// Q2. Which vegetarian-only restaurants operate in Vellore or Coimbatore?
db.restaurants.find(
  { is_veg: true, city: { $in: ["Vellore", "Coimbatore"] } },
  { _id: 0, name: 1, city: 1, cuisine: 1, opened_year: 1 }
);
