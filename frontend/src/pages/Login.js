import { useState } from "react";
import { useNavigate } from "react-router-dom";
import LogRegPage from "../components/LogRegPage";
import { GoogleButton } from "../components/GoogleButton";

export default function Login() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");
    const navigate = useNavigate();

    // Handle form submission
    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError(""); // Reset error state

        try {
            const response = await fetch("http://127.0.0.1:8000/auth/login", {
                method: "POST",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                },
                body: new URLSearchParams({
                    username: username,
                    password: password,
                }),
            });

            if (response.ok) {
                const data = await response.json();
                if (data.status === "success") {
                    // Redirect to Matching Interface on successful login
                    console.log("Login successful, redirecting...");
                    navigate("/matching-interface");
                } else {
                    throw new Error("Incorrect username or password");
                }
            } else {
                throw new Error("Incorrect username or password");
            }
        } catch (error) {
            setError(error.message);
        } finally {
            setLoading(false);
        }
    };

    return (
        <LogRegPage title="Sign In" subtitle="View your matches and schedule mocks">
            {/* Google Sign-in Button */}
            {/* <GoogleButton text="Sign in with Google" /> */}

            {/* Login Form */}
            <form onSubmit={handleSubmit} className="mt-6 space-y-4">
                
                <div>
                    <label className="block text-sm font-medium text-gray-700">Username</label>
                    <input
                        type="text"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        required
                        className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                    />
                </div>
                <div>
                    <label className="block text-sm font-medium text-gray-700">Password</label>
                    <input
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                        className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                    />
                </div>
                <button
                    type="submit"
                    disabled={loading}
                    className={`w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white ${
                        loading ? "bg-blue-300 cursor-not-allowed" : "bg-blue-600 hover:bg-blue-700"
                    }`}
                >
                    {loading ? "Logging in..." : "Login"}
                </button>
            </form>

            {/* Error Modal */}
            {error && (
                <div className="fixed inset-0 flex items-center justify-center bg-gray-800 bg-opacity-50">
                    <div className="bg-white rounded-lg p-6 max-w-sm w-full shadow-lg relative">
                        <button
                            className="absolute top-2 right-2 text-gray-500 hover:text-gray-700"
                            onClick={() => setError("")}
                        >
                            &times;
                        </button>
                        <p className="text-red-600 font-semibold">{error}</p>
                    </div>
                </div>
            )}
        </LogRegPage>
    );
}
