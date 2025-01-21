import React, { useState } from "react";
import { Link } from "react-router-dom";

const ShopList = () => {
  const shops = [
    { id: 1, name: "ElectroMart", discount: "20% Off", city: "New York", img: "https://via.placeholder.com/150" },
    { id: 2, name: "FashionHub", discount: "50% Off", city: "Los Angeles", img: "https://via.placeholder.com/150" },
    { id: 3, name: "GroceryPlus", discount: "30% Off", city: "Chicago", img: "https://via.placeholder.com/150" },
    { id: 4, name: "TechStore", discount: "15% Off", city: "New York", img: "https://via.placeholder.com/150" },
    { id: 5, name: "HomeEssentials", discount: "25% Off", city: "Los Angeles", img: "https://via.placeholder.com/150" },
  ];

  const cities = ["All", ...new Set(shops.map((shop) => shop.city))]; // Extract unique cities

  const [selectedCity, setSelectedCity] = useState("All");

  const filteredShops = selectedCity === "All" ? shops : shops.filter(shop => shop.city === selectedCity);

  return (
    <div className="container my-5">
      <h2 className="text-center text-primary">Shops with Discounts</h2>

      {/* City Filter Dropdown */}
      <div className="d-flex justify-content-center my-3">
        <select
          className="form-select w-auto"
          value={selectedCity}
          onChange={(e) => setSelectedCity(e.target.value)}
        >
          {cities.map((city, index) => (
            <option key={index} value={city}>{city}</option>
          ))}
        </select>
      </div>

      {/* Shop Cards */}
      <div className="row mt-4">
        {filteredShops.length > 0 ? (
          filteredShops.map((shop) => (
            <div key={shop.id} className="col-md-4">
              <div className="card shadow-sm">
                <img src={shop.img} className="card-img-top" alt={shop.name} />
                <div className="card-body text-center">
                  <h5 className="card-title">{shop.name}</h5>
                  <p className="card-text text-success fw-bold">{shop.discount}</p>
                  <p className="text-muted"><strong>City:</strong> {shop.city}</p>
                  <Link to={`/shop/${shop.id}`} className="btn btn-primary">
                    View Details
                  </Link>
                </div>
              </div>
            </div>
          ))
        ) : (
          <p className="text-center text-danger fw-bold">No shops found in this city.</p>
        )}
      </div>
    </div>
  );
};

export default ShopList;
