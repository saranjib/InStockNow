import React, { useState } from "react";
import API from "../services/api";

function Search() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);

  const searchProduct = () => {
    API.get(`/products/search/${query}`)
      .then(res => setResults(res.data));
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>Search Product Availability</h2>

      <input
        type="text"
        placeholder="Search product..."
        onChange={(e) => setQuery(e.target.value)}
      />

      <button onClick={searchProduct}>
        Search
      </button>

      <div>
        {results.map((item, index) => (
          <div key={index} style={{ marginTop: "20px" }}>
            <h3>{item.product}</h3>

            {item.stock.map((s, i) => (
              <p key={i}>
                Store ID {s.store_id} → {s.quantity} in stock
              </p>
            ))}
          </div>
        ))}
      </div>
    </div>
  );
}

export default Search;