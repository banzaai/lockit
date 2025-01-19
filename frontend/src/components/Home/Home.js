import React from "react";
import { Link } from "react-router-dom";

const Home = () => {
  return (
    <div>
      <h2>Welcome to Discount Shops</h2>
      <p>Browse amazing discounts from various stores!</p>
      <Link to="/shops">Browse Shops</Link>
    </div>
  );
};

export default Home;
