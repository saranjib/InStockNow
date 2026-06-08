import React from "react";
import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav style={styles.nav}>
      <h2>ShelfSync</h2>

      <div>
        <Link to="/">Home</Link>
        <Link to="/products">Products</Link>
        <Link to="/stores">Stores</Link>
        <Link to="/search">Search</Link>
        <Link to="/login">Login</Link>
      </div>
    </nav>
  );
}

const styles = {
  nav: {
    display: "flex",
    justifyContent: "space-between",
    padding: "10px",
    background: "#222",
    color: "white"
  }
};

export default Navbar;