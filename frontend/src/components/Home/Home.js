import React from "react";
import { Button } from "react-bootstrap"; // Using React-Bootstrap button component

const Home = () => {
  return (
    <div className="container my-5">
      <h2 className="text-center text-primary">Welcome to Discount Shops!</h2>
      <p className="lead text-center">
        Browse amazing discounts from various stores!
      </p>

      <div className="text-center mt-4">
        <p>
          Looking for the best deals? Browse now and enjoy exclusive offers.
        </p>
        <Button variant="primary" size="lg" href="/shops">
          Browse Shops
        </Button>
      </div>

      <div className="text-center mt-5">
        <h3>Shopkeepers, Join Us!</h3>
        <p>
          As a shopkeeper, you can upload your offers and share photos with customers.
        </p>
        <Button variant="success" size="lg" href="/register-business">
          Add Your Offer
        </Button>
      </div>
    </div>
  );
};

export default Home;
