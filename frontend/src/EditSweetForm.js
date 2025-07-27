import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import axios from 'axios';

// 🔁 Utility: Refresh JWT Access Token using the stored Refresh Token
const refreshAccessToken = async () => {
  const refresh = localStorage.getItem('refresh');
  try {
    const res = await axios.post('http://localhost:8000/api/auth/token/refresh/', { refresh });
    const newAccess = res.data.access;
    localStorage.setItem('access', newAccess);
    return newAccess;
  } catch (err) {
    console.error("Refresh token failed", err);
    throw err;
  }
};

const EditSweetForm = () => {
  const { id } = useParams(); // 🍬 Sweet ID from URL
  const navigate = useNavigate(); // 🔄 For redirection after update

  // 🧾 Form state
  const [formData, setFormData] = useState({
    name: '',
    description: '',
    category: '',
    price_per_kg: '',
    stock: '',
    is_available: true,
    ingredients: '',
    offer_percent: '',
    tags: '',
    image: null,
  });

  const [preview, setPreview] = useState(null); // 🌄 Image preview

  // 🔃 Fetch sweet details on mount
  useEffect(() => {
    axios.get(`http://localhost:8000/api/sweets/${id}/`)
      .then(res => {
        const data = res.data;
        setFormData({
          ...data,
          image: null, // Don’t prefill image field with URL
        });
        setPreview(data.image); // Set preview from URL
      })
      .catch(err => console.error("Fetch error:", err));
  }, [id]);

  // 📦 Handle input and file changes
  const handleChange = e => {
    const { name, value, type, checked, files } = e.target;
    if (type === 'file') {
      setFormData(prev => ({
        ...prev,
        [name]: files[0], // Store file
      }));
      setPreview(URL.createObjectURL(files[0])); // Update image preview
    } else {
      setFormData(prev => ({
        ...prev,
        [name]: type === 'checkbox' ? checked : value,
      }));
    }
  };

  // ✅ Form submit handler
  const handleSubmit = async (e) => {
    e.preventDefault();

    // Function to send PUT request with proper token
    const sendUpdateRequest = async (accessToken) => {
      const data = new FormData();
      for (const key in formData) {
        if (formData[key] !== null && formData[key] !== undefined) {
          data.append(key, formData[key]);
        }
      }

      return await axios.put(`http://localhost:8000/api/sweets/${id}/`, data, {
        headers: {
          'Content-Type': 'multipart/form-data',
          Authorization: `Bearer ${accessToken}`,
        },
      });
    };

    try {
      await sendUpdateRequest(localStorage.getItem('access'));
      alert("Sweet updated successfully!");
      navigate('/admin/sweets');
    } catch (err) {
      const errorData = err.response?.data;

      // ⏳ Token expired — try refresh
      if (
        errorData?.code === 'token_not_valid' &&
        errorData?.messages?.[0]?.message === 'Token is expired'
      ) {
        try {
          const newAccess = await refreshAccessToken();
          await sendUpdateRequest(newAccess);
          alert("Sweet updated after refreshing token!");
          navigate('/admin/sweets');
        } catch (refreshErr) {
          alert("Session expired. Please login again.");
          localStorage.removeItem('access');
          localStorage.removeItem('refresh');
          navigate('/login');
        }
      } else {
        console.error("Update error:", errorData || err.message);
        alert("Update failed. Please try again.");
      }
    }
  };

  return (
    <div className="max-w-xl mx-auto mt-10 p-6 bg-white rounded shadow">
      <h2 className="text-xl font-bold mb-4 text-pink-600">Edit Sweet 🍬</h2>
      <form onSubmit={handleSubmit} encType="multipart/form-data" className="space-y-3">
        {/* Name */}
        <input
          name="name"
          value={formData.name}
          onChange={handleChange}
          placeholder="Name"
          className="w-full p-2 border rounded"
          required
        />

        {/* Description */}
        <textarea
          name="description"
          value={formData.description}
          onChange={handleChange}
          placeholder="Description"
          className="w-full p-2 border rounded"
          required
        />

        {/* Category */}
        <input
          name="category"
          value={formData.category}
          onChange={handleChange}
          placeholder="Category"
          className="w-full p-2 border rounded"
        />

        {/* Price per kg */}
        <input
          name="price_per_kg"
          type="number"
          value={formData.price_per_kg}
          onChange={handleChange}
          placeholder="Price per kg"
          className="w-full p-2 border rounded"
          required
        />

        {/* Stock */}
        <input
          name="stock"
          type="number"
          value={formData.stock}
          onChange={handleChange}
          placeholder="Stock"
          className="w-full p-2 border rounded"
          required
        />

        {/* Ingredients */}
        <textarea
          name="ingredients"
          value={formData.ingredients}
          onChange={handleChange}
          placeholder="Ingredients"
          className="w-full p-2 border rounded"
        />

        {/* Offer Percent */}
        <input
          name="offer_percent"
          type="number"
          value={formData.offer_percent}
          onChange={handleChange}
          placeholder="Offer %"
          className="w-full p-2 border rounded"
        />

        {/* Tags */}
        <input
          name="tags"
          value={formData.tags}
          onChange={handleChange}
          placeholder="Tags"
          className="w-full p-2 border rounded"
        />

        {/* Image Preview and Upload */}
        {preview && (
          <div>
            <img src={preview} alt="Preview" className="w-40 h-40 object-cover mb-2 rounded" />
          </div>
        )}
        <input
          type="file"
          name="image"
          accept="image/*"
          onChange={handleChange}
          className="w-full p-2 border rounded"
        />

        {/* Availability Checkbox */}
        <label className="block text-sm">
          <input
            type="checkbox"
            name="is_available"
            checked={formData.is_available}
            onChange={handleChange}
          />
          <span className="ml-2">Available</span>
        </label>

        {/* Submit Button */}
        <button
          type="submit"
          className="w-full bg-green-500 hover:bg-green-600 text-white font-semibold py-2 rounded"
        >
          Update Sweet
        </button>
      </form>
    </div>
  );
};

export default EditSweetForm;
