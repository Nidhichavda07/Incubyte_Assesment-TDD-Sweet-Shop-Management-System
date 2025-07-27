// ... your imports stay the same
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { FiShoppingCart, FiLogOut } from 'react-icons/fi';
import { Link, useNavigate } from 'react-router-dom';
import { toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';


const Dashboard = () => {
  const [message, setMessage] = useState('');
  const [sweets, setSweets] = useState([]);
  const [search, setSearch] = useState('');
  const [category, setCategory] = useState('All');
  const [showModal, setShowModal] = useState(false);
  const [selectedSweet, setSelectedSweet] = useState(null);
  const [quantity, setQuantity] = useState(1);

  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem('access');

    axios.get('http://127.0.0.1:8000/api/dashboard/', {
      headers: { Authorization: `Bearer ${token}` },
    })
      .then(res => setMessage(res.data.message))
      .catch(() => setMessage('Unauthorized. Please login.'));

    axios.get('http://127.0.0.1:8000/api/sweets/', {
      headers: { Authorization: `Bearer ${token}` },
    })
      .then(res => setSweets(res.data))
      .catch(() => console.log("Failed to fetch sweets"));
  }, []);

  const handleLogout = () => {
    localStorage.removeItem('access');
    window.location.href = '/login';
  };

  const openModal = (sweet) => {
    setSelectedSweet(sweet);
    setQuantity(1);
    setShowModal(true);
  };

  const closeModal = () => {
    setShowModal(false);
    setSelectedSweet(null);
  };

  const handlePurchase = async () => {
    try {
      const token = localStorage.getItem("access");

      await axios.post(
        "http://127.0.0.1:8000/api/purchases/",
        {
          sweet: selectedSweet.id,
          quantity: quantity,
        },
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

     toast.success("Sweet purchased successfully!");
     navigate('/dashboard', { state: { purchaseSuccess: true } });
      closeModal();
    } catch (error) {
      console.error("Error purchasing:", error);
      toast.error("Failed to purchase sweet.");
    }
  };

  const filteredSweets = sweets.filter((sweet) => {
    const q = search.trim().toLowerCase();
    const categoryMatch = category === 'All' || sweet.category.toLowerCase() === category.toLowerCase();

    const priceMatchRegex = q.match(/^([<>]=?|=)?(\d+)$/);
    if (priceMatchRegex) {
      const operator = priceMatchRegex[1] || '=';
      const value = parseFloat(priceMatchRegex[2]);
      const sweetPrice = parseFloat(sweet.price_per_kg);

      let priceMatch = false;
      if (operator === '>') priceMatch = sweetPrice > value;
      else if (operator === '<') priceMatch = sweetPrice < value;
      else if (operator === '>=') priceMatch = sweetPrice >= value;
      else if (operator === '<=') priceMatch = sweetPrice <= value;
      else priceMatch = sweetPrice === value;

      return priceMatch && categoryMatch;
    }

    const nameMatch = sweet.name.toLowerCase().includes(q);
    const tagMatch = sweet.tags?.toLowerCase().includes(q);

    return (nameMatch || tagMatch) && categoryMatch;
  });

  const categories = ['All', ...new Set(sweets.map(s => s.category))];

  return (
    <div className="min-h-screen bg-gradient-to-br from-yellow-100 to-pink-100 p-6">
      {/* Navbar */}
      <nav className="bg-pink-600 text-white py-4 px-6 rounded-xl shadow-md flex flex-wrap items-center justify-between gap-4">
        <h1 className="text-2xl font-bold">🍬 Sweet Shop</h1>

        <input
          type="text"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          placeholder="Search by name, tags or price (e.g. >250)"
          className="flex-grow px-4 py-2 rounded-full focus:outline-none focus:ring-2 focus:ring-pink-400 text-gray-800"
        />

        <select
          value={category}
          onChange={(e) => setCategory(e.target.value)}
          className="px-4 py-2 rounded-full bg-white text-pink-600 shadow-md border border-gray-300 focus:outline-none focus:ring-2 focus:ring-pink-400"
        >
          {categories.map((cat) => (
            <option key={cat} value={cat}>{cat}</option>
          ))}
        </select>

        <div className="flex items-center gap-4">
          <Link to="/purchase">
            <button className="relative p-2 hover:bg-pink-100 rounded-full transition">
              <FiShoppingCart className="text-white text-2xl" />
            </button>
          </Link>
          <button
            onClick={handleLogout}
            className="bg-white text-pink-600 font-semibold px-4 py-2 rounded-full hover:bg-pink-100 transition"
          >
            <FiLogOut className="inline mr-2" /> Logout
          </button>
        </div>
      </nav>

      {/* Welcome Message */}
      <div className="max-w-xl mx-auto bg-white p-8 mt-10 rounded-2xl shadow-md text-center">
        <h2 className="text-2xl font-bold text-pink-600 mb-2">Welcome!</h2>
        <p className="text-gray-700">{message}</p>
      </div>

      {/* Sweets Grid */}
      <div className="mt-10 grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
        {filteredSweets.map((sweet) => (
          <div key={sweet.id} className="bg-white rounded-2xl shadow-md overflow-hidden">
            <img src={sweet.image} alt={sweet.name} className="w-full h-40 object-cover" />
            <div className="p-4">
              <h3 className="text-lg font-bold text-pink-700">{sweet.name}</h3>
              <p className="text-gray-600 text-sm mb-2">{sweet.description}</p>
              <p className="text-pink-600 font-semibold mb-2">₹{sweet.price_per_kg} per kg</p>
              <p className="text-xs italic text-gray-500 mb-1">Tags: {sweet.tags || 'None'}</p>
              <p className="text-xs text-gray-400">Category: {sweet.category}</p>
              <button
                onClick={() => openModal(sweet)}
                className="mt-2 bg-pink-500 text-white px-4 py-2 rounded-full hover:bg-pink-600 transition"
              >
                Purchase
              </button>
            </div>
          </div>
        ))}
      </div>

      {/* MODAL */}
      {showModal && selectedSweet && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
          <div className="bg-white p-6 rounded-xl shadow-lg w-full max-w-md">
            <h2 className="text-xl font-bold text-pink-600 mb-4">
              Purchase {selectedSweet.name}
            </h2>
            <img src={selectedSweet.image} alt={selectedSweet.name} className="w-full h-40 object-cover rounded-lg mb-4" />
            <p className="mb-2">Price per Kg: ₹{selectedSweet.price_per_kg}</p>
            <label className="block mb-2 font-semibold">Quantity (kg):</label>
            <input
              type="number"
              min="1"
              max={selectedSweet.stock}
              value={quantity}
              onChange={(e) => setQuantity(e.target.value)}
              className="w-full border px-4 py-2 rounded-md mb-4"
            />
            <p className="mb-4 text-pink-600 font-semibold">Total: ₹{selectedSweet.price_per_kg * quantity}</p>
            <div className="flex justify-end gap-3">
              <button
                onClick={closeModal}
                className="px-4 py-2 bg-gray-300 rounded-md"
              >
                Cancel
              </button>
              <button
                onClick={handlePurchase}
                className="px-4 py-2 bg-pink-600 text-white rounded-md hover:bg-pink-700"
              >
                Confirm Purchase
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default Dashboard;
