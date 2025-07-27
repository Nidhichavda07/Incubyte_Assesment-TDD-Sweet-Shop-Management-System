import React, { useEffect, useState } from "react";
import axios from "axios";

const Purchase = () => {
  // State to hold purchase data
  const [purchases, setPurchases] = useState([]);

  // Fetch purchases when component mounts
  useEffect(() => {
    const fetchPurchases = async () => {
      try {
        const token = localStorage.getItem("token"); // JWT token from local storage

        // Make API request to get user purchases
        const response = await axios.get("http://localhost:8000/api/purchases/", {
          headers: {
            Authorization: `Bearer ${token}`, // Attach JWT token for authentication
          },
        });

        // Set the response data to state
        setPurchases(response.data);
      } catch (error) {
        console.error("Error fetching purchases:", error);
      }
    };

    fetchPurchases(); // Call the function
  }, []); // Empty dependency array ensures it runs once on mount

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Your Purchases</h1>

      {purchases.length === 0 ? (
        <p>No purchases found.</p>
      ) : (
        <ul>
          {purchases.map((item) => (
            <li key={item.id} className="mb-2 p-4 bg-pink-100 rounded shadow">
              {/* Display sweet name and quantity; fallback if sweet_name isn't directly available */}
              {item.sweet_name || item.sweet?.name} - Quantity: {item.quantity}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default Purchase;
