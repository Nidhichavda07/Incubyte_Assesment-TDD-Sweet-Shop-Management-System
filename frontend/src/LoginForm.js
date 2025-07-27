import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const LoginForm = () => {
  const [formData, setFormData] = useState({ username: '', password: '' });
  const navigate = useNavigate();

  const handleChange = (e) =>
    setFormData({ ...formData, [e.target.name]: e.target.value });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post('http://127.0.0.1:8000/api/login/', formData);
      localStorage.setItem('access', res.data.access);
      localStorage.setItem('username', formData.username);

      const isAdmin = formData.username.toLowerCase() === 'admin';
      navigate(isAdmin ? '/admin-dashboard' : '/dashboard');
    } catch (err) {
      alert('Login failed. Please check your credentials.');
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-yellow-100 to-pink-100">
      {/* Navbar */}
      <nav className="bg-pink-600 text-white px-6 py-4 shadow-md flex justify-between items-center">
        <h1 className="text-2xl font-bold">🍬 Sweet Shop Management</h1>
        <div className="space-x-4">
          <button
            onClick={() => navigate('/register')}
            className="bg-white text-pink-600 px-4 py-2 rounded-lg shadow hover:bg-pink-100 transition"
          >
            Register
          </button>
          <button
            onClick={() => navigate('/login')}
            className="bg-white text-pink-600 px-4 py-2 rounded-lg shadow hover:bg-pink-100 transition"
          >
            Login
          </button>
        </div>
      </nav>

      {/* Login Form */}
      <div className="flex items-center justify-center py-12 px-4">
        <form
          onSubmit={handleSubmit}
          className="bg-white shadow-lg rounded-xl px-10 pt-8 pb-10 w-full max-w-md"
        >
          <h2 className="text-3xl font-bold mb-6 text-center text-pink-600">
            🍬 Sweet Shop Login
          </h2>

          {/* Username */}
          <div className="mb-5">
            <label htmlFor="username" className="block text-gray-700 font-medium mb-2">
              Username
            </label>
            <input
              name="username"
              id="username"
              placeholder="Enter username"
              className="w-full px-4 py-2 border border-pink-300 rounded focus:outline-none focus:ring-2 focus:ring-pink-400"
              value={formData.username}
              onChange={handleChange}
              required
            />
          </div>

          {/* Password */}
          <div className="mb-6">
            <label htmlFor="password" className="block text-gray-700 font-medium mb-2">
              Password
            </label>
            <input
              name="password"
              id="password"
              type="password"
              placeholder="Enter password"
              className="w-full px-4 py-2 border border-pink-300 rounded focus:outline-none focus:ring-2 focus:ring-pink-400"
              value={formData.password}
              onChange={handleChange}
              required
            />
          </div>

          {/* Submit Button */}
          <button
            type="submit"
            className="w-full bg-pink-600 hover:bg-pink-100 text-white hover:text-pink-600 font-semibold py-2 px-4 rounded-lg transition duration-200"
          >
            Login
          </button>
        </form>
      </div>
    </div>
  );
};

export default LoginForm;
