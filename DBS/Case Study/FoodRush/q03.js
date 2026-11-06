db = db.getSiblingDB("foodrush");

// Q3. Which vegetarian menu items cost less than Rs. 100, cheapest first?
db.menu_items.find(
  { is_veg: true, price: { $lt: 100 } },
  { _id: 0, name: 1, category: 1, price: 1, restaurant_id: 1 }
).sort({ price: 1, name: 1 });
