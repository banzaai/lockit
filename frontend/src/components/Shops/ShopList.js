import React from "react";
import { Link } from "react-router-dom";

const ShopList = () => {
  const shops = [
    { id: 1, name: "ElectroMart", discount: "20% Off", img: "https://via.placeholder.com/150" },
    { id: 2, name: "FashionHub", discount: "50% Off", img: "https://via.placeholder.com/150" },
    { id: 3, name: "GroceryPlus", discount: "30% Off", img: "https://via.placeholder.com/150" },
  ];

  return (
    <div className="container my-5">
      <h2 className="text-center text-primary">Shops with Discounts</h2>
      <div className="row mt-4">
        {shops.map((shop) => (
          <div key={shop.id} className="col-md-4">
            <div className="card shadow-sm">
              <img src={shop.img} className="card-img-top" alt={shop.name} />
              <div className="card-body text-center">
                <h5 className="card-title">{shop.name}</h5>
                <p className="card-text text-success fw-bold">{shop.discount}</p>
                <Link to={`/shop/${shop.id}`} className="btn btn-primary">
                  View Details
                </Link>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ShopList;
