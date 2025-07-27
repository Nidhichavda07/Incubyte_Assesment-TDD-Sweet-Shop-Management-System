import React, { useState } from 'react';
import axios from 'axios';

const AddSweetForm = () => {
  // Initial form state
  const [formData, setFormData] = useState({
    name: '',
    description: '',
    price: '',
    category: '',
    quantity_in_stock: '',
    is_available: true,
    ingredients: '',
    offer_percent: '',
    tags: '',
  });

  // State for image file
  const [image, setImage] = useState(null);

  // Handle text, number, and checkbox input changes
  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: type === 'checkbox' ? checked : value,
    }));
  };

  // Handle image file selection
  const handleFileChange = (e) => {
    setImage(e.target.files[0]);
  };

  // Submit form data with image as multipart/form-data
  const handleSubmit = async (e) => {
    e.preventDefault();

    const data = new FormData();

    // Append all form fields
    Object.entries(formData).forEach(([key, value]) => {
      data.append(key, value);
    });

    // Append image if selected
    if (image) {
      data.append('image', image);
    }

    try {
      // API request to create sweet
      const response = await axios.post('http://localhost:8000/api/sweets/', data, {
        headers: {
          'Content-Type': 'multipart/form-data',
          Authorization: `Bearer ${localStorage.getItem('access')}`, // JWT token
        },
      });

      alert('Sweet added successfully!');
      
      // Reset form after success
      setFormData({
        name: '',
        description: '',
        price: '',
        category: '',
        quantity_in_stock: '',
        is_available: true,
        ingredients: '',
        offer_percent: '',
        tags: '',
      });
      setImage(null);
    } catch (error) {
      console.error('Failed to add sweet:', error.response?.data || error.message);
      alert('Failed to add sweet.');
    }
  };

  return (
    <div className="max-w-xl mx-auto mt-10 bg-white p-6 shadow-md rounded-md">
      <h2 className="text-xl font-bold mb-4 text-pink-600">Add New Sweet 🍬</h2>
      <form onSubmit={handleSubmit} className="space-y-3">
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

        {/* Price */}
        <input
          type="number"
          name="price"
          value={formData.price}
          onChange={handleChange}
          placeholder="Price per kg"
          className="w-full p-2 border rounded"
          required
        />

        {/* Category */}
        <input
          type="text"
          name="category"
          value={formData.category}
          onChange={handleChange}
          placeholder="Category"
          className="w-full p-2 border rounded"
        />

        {/* Quantity in stock */}
        <input
          type="number"
          name="quantity_in_stock"
          value={formData.quantity_in_stock}
          onChange={handleChange}
          placeholder="Stock"
          className="w-full p-2 border rounded"
          required
        />

        {/* Ingredients */}
        <input
          type="text"
          name="ingredients"
          value={formData.ingredients}
          onChange={handleChange}
          placeholder="Ingredients"
          className="w-full p-2 border rounded"
        />

        {/* Offer percentage */}
        <input
          type="number"
          name="offer_percent"
          value={formData.offer_percent}
          onChange={handleChange}
          placeholder="Offer (%)"
          className="w-full p-2 border rounded"
        />

        {/* Tags */}
        <input
          type="text"
          name="tags"
          value={formData.tags}
          onChange={handleChange}
          placeholder="Tags"
          className="w-full p-2 border rounded"
        />

        {/* Availability Checkbox */}
        <label className="text-sm block">
          <input
            type="checkbox"
            name="is_available"
            checked={formData.is_available}
            onChange={handleChange}
          />
          <span className="ml-2">Available</span>
        </label>

        {/* Image Upload */}
        <input
          type="file"
          name="image"
          onChange={handleFileChange}
          className="w-full p-2"
          accept="image/*"
        />

        {/* Submit Button */}
        <button
          type="submit"
          className="bg-pink-500 text-white px-4 py-2 rounded hover:bg-pink-600 transition"
        >
          Add Sweet
        </button>
      </form>
    </div>
  );
};

export default AddSweetForm;
