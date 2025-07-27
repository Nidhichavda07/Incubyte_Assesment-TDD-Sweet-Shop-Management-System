import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const RegisterForm = () => {
  const [formData, setFormData] = useState({ username: '', email: '', password: '' });
  const navigate = useNavigate();

  // Handle input change
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // Register user
      await axios.post('http://127.0.0.1:8000/api/register/', formData);

      // Auto-login after registration
      const loginRes = await axios.post('http://127.0.0.1:8000/api/login/', {
        username: formData.username,
        password: formData.password,
      });

      // Save token to local storage
      localStorage.setItem('access', loginRes.data.access);
      navigate('/dashboard');
    } catch (err) {
      console.error(err);
      alert('Registration failed. Please try again.');
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-yellow-100 to-pink-100">
      {/* Navbar */}
      <nav className="bg-pink-600 text-white py-4 px-6 shadow-md flex justify-between items-center">
        <h1 className="text-2xl font-bold">🍬 Sweet Shop Management</h1>
        <div className="space-x-4">
          <button
            onClick={() => navigate('/register')}
            className="bg-white text-pink-600 font-medium px-4 py-2 rounded-lg hover:bg-pink-100 transition"
          >
            Register
          </button>
          <button
            onClick={() => navigate('/login')}
            className="bg-white text-pink-600 font-medium px-4 py-2 rounded-lg hover:bg-pink-100 transition"
          >
            Login
          </button>
        </div>
      </nav>

      {/* Registration Form */}
      <div className="flex justify-center items-center h-[calc(100vh-80px)] px-4">
        <form
          onSubmit={handleSubmit}
          className="bg-white shadow-xl rounded-xl px-10 pt-8 pb-10 w-full max-w-md"
        >
          <h2 className="text-3xl font-bold mb-6 text-center text-pink-600">
            🍭 Create an Account
          </h2>

          {/* Username */}
          <label className="block mb-1 text-gray-700 font-medium" htmlFor="username">
            Username
          </label>
          <input
            name="username"
            id="username"
            placeholder="Enter username"
            value={formData.username}
            onChange={handleChange}
            required
            className="w-full px-4 py-2 mb-4 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-pink-400"
          />

          {/* Email */}
          <label className="block mb-1 text-gray-700 font-medium" htmlFor="email">
            Email
          </label>
          <input
            name="email"
            id="email"
            type="email"
            placeholder="Enter email"
            value={formData.email}
            onChange={handleChange}
            required
            className="w-full px-4 py-2 mb-4 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-pink-400"
          />

          {/* Password */}
          <label className="block mb-1 text-gray-700 font-medium" htmlFor="password">
            Password
          </label>
          <input
            name="password"
            id="password"
            type="password"
            placeholder="Enter password"
            value={formData.password}
            onChange={handleChange}
            required
            className="w-full px-4 py-2 mb-6 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-pink-400"
          />

          <button
            type="submit"
            className="w-full bg-pink-600 text-white font-semibold py-2 px-4 rounded-lg hover:bg-pink-700 transition"
          >
            Register
          </button>
        </form>
      </div>
    </div>
  );
};

export default RegisterForm;
