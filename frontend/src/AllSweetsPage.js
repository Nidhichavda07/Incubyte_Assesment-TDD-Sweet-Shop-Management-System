import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { FiEdit, FiTrash2 } from 'react-icons/fi';
import { useNavigate, Link } from 'react-router-dom';

const AllSweetsPage = () => {
  const [sweets, setSweets] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    axios
      .get('http://127.0.0.1:8000/api/sweets/', {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('access')}`,
        },
      })
      .then((res) => setSweets(res.data))
      .catch((err) => {
        console.error('Error fetching sweets:', err);
        alert('Failed to load sweets. Please log in again.');
      });
  }, );

 const handleEdit = (id) => {
  navigate(`/sweets/edit/${id}`);
};
  const handleDelete = (id) => {
    if (window.confirm('Are you sure you want to delete this sweet?')) {
      axios
        .delete(`http://127.0.0.1:8000/api/sweets/${id}/`, {
          headers: {
            Authorization: `Bearer ${localStorage.getItem('access')}`,
          },
        })
        .then(() => {
          setSweets((prev) => prev.filter((sweet) => sweet.id !== id));
        })
        .catch((err) => {
          console.error('Error deleting sweet:', err);
          alert('Delete failed.');
        });
    }
  };

  return (
    <div className="min-h-screen bg-pink-50 p-6">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold text-pink-700">🍭 All Sweets</h1>
        <Link to="/add-sweet" className="bg-pink-500 text-white px-4 py-2 rounded hover:bg-pink-600">
          + Add Sweet
        </Link>
      </div>

      <div className="overflow-x-auto rounded-lg shadow-lg">
        <table className="w-full table-auto bg-white border border-gray-200">
          <thead className="bg-pink-100">
            <tr>
              <th className="px-4 py-2 text-left">Image</th>
              <th className="px-4 py-2 text-left">Name</th>
              <th className="px-4 py-2 text-left">Price/kg (₹)</th>
              <th className="px-4 py-2 text-left">Stock</th>
              <th className="px-4 py-2 text-left">Available</th>
              <th className="px-4 py-2 text-left">Offer (%)</th>
              <th className="px-4 py-2 text-left">Tags</th>
              <th className="px-4 py-2 text-right">Actions</th>
            </tr>
          </thead>
          <tbody>
            {sweets.length === 0 ? (
              <tr>
                <td colSpan="8" className="text-center py-4 text-gray-600">
                  No sweets found.
                </td>
              </tr>
            ) : (
              sweets.map((sweet) => (
                <tr key={sweet.id} className="border-t hover:bg-pink-50">
                  <td className="px-4 py-2">
                    {sweet.image ? (
                      <img
                        src={`http://127.0.0.1:8000${sweet.image}`}
                        alt={sweet.name}
                        className="w-12 h-12 object-cover rounded"
                      />
                    ) : (
                      <span className="text-gray-400">No image</span>
                    )}
                  </td>
                  <td className="px-4 py-2">{sweet.name}</td>
                  <td className="px-4 py-2">₹{sweet.price_per_kg}</td>
                  <td className="px-4 py-2">{sweet.stock}</td>
                  <td className="px-4 py-2">{sweet.is_available ? 'Yes' : 'No'}</td>
                  <td className="px-4 py-2">{sweet.offer_percent}%</td>
                  <td className="px-4 py-2">{sweet.tags}</td>
                  <td className="px-4 py-2 text-right">
                    <button
  onClick={() => handleEdit(sweet.id)}
  className="text-yellow-500 hover:text-yellow-600 mx-1"
  title="Edit"
>
  <FiEdit size={18} />
</button>
                    <button
                      onClick={() => handleDelete(sweet.id)}
                      className="text-red-500 hover:text-red-600 mx-1"
                      title="Delete"
                    >
                      <FiTrash2 size={18} />
                    </button>
                  </td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default AllSweetsPage;
