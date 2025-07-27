import React from 'react';
import { useNavigate } from 'react-router-dom';

const AdminDashboard = () => {
  const navigate = useNavigate();

  const handleLogout = () => {
    // Add JWT token removal logic here if implemented
    localStorage.removeItem('token'); // or whatever key you're using
    navigate('/login');
  };

  const stats = [
    {
      label: '🍬 Total Sweets',
      count: 120,
      path: '/admin/sweets',
    },
    {
      label: '👥 Total Users',
      count: 58,
    },
    {
      label: '📦 Total Orders',
      count: 245,
    },
  ];

  return (
    <div className="min-h-screen bg-yellow-50">
      {/* Navbar */}
      <nav className="bg-pink-600 text-white px-6 py-4 shadow-md flex justify-between items-center">
        <h1 className="text-2xl font-bold tracking-wide">🍭 Admin Dashboard</h1>
        <button
          onClick={handleLogout}
          className="bg-white text-pink-600 font-medium px-4 py-2 rounded-lg shadow hover:bg-pink-100 transition"
        >
          Logout
        </button>
      </nav>

      {/* Cards */}
      <div className="p-6 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {stats.map((stat, index) => (
          <div
            key={index}
            onClick={() => stat.path && navigate(stat.path)}
            className={`${
              stat.path ? 'cursor-pointer' : ''
            } bg-white p-6 rounded-2xl shadow-lg hover:shadow-xl transition`}
          >
            <h2 className="text-xl font-semibold text-pink-600 mb-2">{stat.label}</h2>
            <p className="text-3xl font-bold text-gray-800">{stat.count}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default AdminDashboard;
