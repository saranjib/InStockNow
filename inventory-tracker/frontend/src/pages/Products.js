import React, { useEffect, useState } from "react";
import API from "../services/api";
import ProductCard from "../components/ProductCard";

function Products() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    API.get("/products/")
      .then(res => setProducts(res.data));
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h2>Products</h2>

      {products.map(p => (
        <ProductCard key={p.id} product={p} />
      ))}
    </div>
  );
}

export default Products;