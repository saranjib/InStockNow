import React from "react";

function ProductCard({ product }) {
  return (
    <div style={styles.card}>
      <h3>{product.name}</h3>
      <p>{product.description}</p>
    </div>
  );
}

const styles = {
  card: {
    border: "1px solid #ccc",
    padding: "10px",
    margin: "10px",
    borderRadius: "8px"
  }
};

export default ProductCard;