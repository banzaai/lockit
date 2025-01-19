import React from "react";
import { useParams } from "react-router-dom";

const ShopDetails = () => {
  const { id } = useParams();

  return (
    <div>
      <h2>Shop Details - ID: {id}</h2>
      <p>Discount details, shop info, and images go here.</p>
    </div>
  );
};

export default ShopDetails;
