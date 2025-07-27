import React from 'react';
import { useNavigate } from 'react-router-dom';
import './output.css';

const Home = () => {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen bg-gradient-to-br from-pink-100 to-yellow-100 flex flex-col">
      {/* Navbar */}
      <nav className="bg-pink-600 text-white px-6 py-4 shadow-md flex justify-between items-center">
        <h1 className="text-2xl font-bold tracking-wide">🍬 Sweet Shop Management</h1>
        <div className="space-x-4">
          <button
            onClick={() => navigate('/register')}
            className="bg-white text-pink-600 font-medium px-4 py-2 rounded-lg shadow-md hover:bg-pink-100 transition"
          >
            Register
          </button>
          <button
            onClick={() => navigate('/login')}
            className="bg-white text-pink-600 font-medium px-4 py-2 rounded-lg shadow-md hover:bg-pink-100 transition"
          >
            Login
          </button>
        </div>
      </nav>

      {/* Main Content */}
      <main className="flex-grow flex flex-col items-center justify-center text-center px-4">
        <h2 className="text-4xl md:text-5xl font-extrabold text-pink-700 mb-4">
          Welcome to Sweet Shop!
        </h2>
        <p className="text-gray-700 text-lg max-w-xl">
          🍭 Manage your sweets, track inventory, and handle sales with ease using our
          <span className="text-pink-600 font-semibold"> Sweet Shop Management System.</span>
        </p>
      </main>
    </div>
  );
};

export default Home;
