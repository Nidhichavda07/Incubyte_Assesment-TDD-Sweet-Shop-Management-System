// import React from 'react';
// import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
// import Home from './Home';
// import RegisterForm from './RegisterForm';
// import LoginForm from './LoginForm';
// import Dashboard from './Dashboard';
// import AdminDashboard from './AdminDashboard';
// import AllSweetsPage from './AllSweetsPage';
// import AddSweetForm from './AddSweetForm';
// import EditSweetForm from './EditSweetForm';
// import Purchase from './Purchase';


// function App() {
//   const isLoggedIn = !!localStorage.getItem('access');

//   return (
//     <Router>
//       <Routes>
//         <Route path="/" element={<Home />} />
//         <Route path="/register" element={<RegisterForm />} />
//         <Route path="/login" element={<LoginForm />} />
//         <Route path="/admin-dashboard" element={<AdminDashboard />} />
//         <Route path="/dashboard" element={isLoggedIn ? <Dashboard /> : <Navigate to="/login" />} />
//         <Route path="/admin/sweets" element={<AllSweetsPage />} />
//         <Route path="/add-sweet" element={<AddSweetForm />} />
//         <Route path="/edit-sweet/:id" element={<EditSweetForm />} /> {/* new */}
//         <Route path="/purchase" element={<Purchase />} />

//             </Routes>
//     </Router>
//   );
// }

// export default App;

import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';

// Component Imports
import Home from './Home';
import RegisterForm from './RegisterForm';
import LoginForm from './LoginForm';
import Dashboard from './Dashboard';
import AdminDashboard from './AdminDashboard';
import AllSweetsPage from './AllSweetsPage';
import AddSweetForm from './AddSweetForm';
import EditSweetForm from './EditSweetForm';
import Purchase from './Purchase';

function App() {
  // Check if the user is logged in (based on JWT access token in localStorage)
  const isLoggedIn = !!localStorage.getItem('access');

  return (
    <Router>
      <Routes>
        {/* Public Routes */}
        <Route path="/" element={<Home />} />
        <Route path="/register" element={<RegisterForm />} />
        <Route path="/login" element={<LoginForm />} />

        {/* Protected User Dashboard (only accessible if logged in) */}
        <Route
          path="/dashboard"
          element={isLoggedIn ? <Dashboard /> : <Navigate to="/login" />}
        />

        {/* Admin Section */}
        <Route path="/admin-dashboard" element={<AdminDashboard />} />
        <Route path="/admin/sweets" element={<AllSweetsPage />} />
        <Route path="/add-sweet" element={<AddSweetForm />} />
        <Route path="/edit-sweet/:id" element={<EditSweetForm />} />

        {/* Purchase Page */}
        <Route path="/purchase" element={<Purchase />} />
      </Routes>
    </Router>
  );
}

export default App;
