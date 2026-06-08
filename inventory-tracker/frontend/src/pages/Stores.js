import React, { useEffect, useState } from "react";
import API from "../services/api";

function Stores() {
  const [stores, setStores] = useState([]);

  useEffect(() => {
    API.get("/stores/")
      .then(res => setStores(res.data));
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h2>Stores</h2>

      {stores.map(s => (
        <div key={s.id} style={{ marginBottom: "10px" }}>
          <h3>{s.store_name}</h3>
          <p>{s.location}</p>
        </div>
      ))}
    </div>
  );
}

export default Stores;