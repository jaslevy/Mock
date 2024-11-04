import './App.css';

import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";
import Landing from "./pages/Landing";
import Register from "./pages/Register";
import Login from './pages/Login';
import RegistrationForm from './pages/RegistrationForm';
import MatchingInterface from './pages/MatchingInterface';
import Profile from './pages/Profile';

function App() {
  return (
    <Router>
        <Routes>
          <Route path="/" element={<Landing />} />
          <Route path="/about" element={<About />} />
          <Route path="/register" element={<Register />} />
          <Route path="/login" element={<Login />} />
          <Route path="/registration-form" element={<RegistrationForm />} />
          <Route path="/matching-interface" element={<MatchingInterface />} />
          <Route path="/profile" element={<Profile />} />
        </Routes>
    </Router>
  );
}

function About() {
  return <h2>About</h2>;
}

export default App;
