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

function App() {
  return (
    <Router>
        <Routes>
          <Route path="/" element={<Landing />} />
          <Route path="/about" element={<About />} />
          <Route path="/register" element={<Register />} />
          <Route path="/login" element={<Login />} />
          <Route path="/registration-form" element={<RegistrationForm />} />
        </Routes>
    </Router>
  );
}

function About() {
  return <h2>About</h2>;
}

export default App;
