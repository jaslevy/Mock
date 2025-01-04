import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom"; // Import useNavigate

export default function UserProfile() {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Editable fields
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [email, setEmail] = useState("");
  const [bio, setBio] = useState("");
  const [profilePicture, setProfilePicture] = useState("");

  const navigate = useNavigate(); // Initialize useNavigate

  useEffect(() => {
    async function fetchUserProfile() {
      try {
        const response = await fetch("http://127.0.0.1:8000/profile/edit", {
          method: "GET",
          credentials: "include", // Include cookies for authentication
        });

        if (!response.ok) {
          const errorText = await response.text();
          throw new Error(`Failed to fetch: ${response.status} - ${errorText}`);
        }

        const data = await response.json();
        const profile = data.profile;

        // Initialize editable fields
        setEmail(profile.email || "");
        setFirstName(profile.first_name || "");
        setLastName(profile.last_name || "");
        setBio(profile.bio || ""); // Default to empty string if bio is missing
        setProfilePicture(profile.profile_picture || ""); // Default to empty string if no profile picture

        // Set user ID as a cookie
        if (profile.google_id) {
          document.cookie = `user_id=${profile.google_id}; path=/;`;
        }
      } catch (err) {
        console.error("Error:", err);
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }

    fetchUserProfile();
  }, []);

  // Handle loading and error states
  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  // Save profile changes
  async function saveProfileChanges() {
    try {
      const updatedProfile = {
        first_name: firstName,
        last_name: lastName,
        bio: bio,
        profile_picture: profilePicture,
      };

      const response = await fetch("http://127.0.0.1:8000/profile/edit", {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
        body: JSON.stringify(updatedProfile),
      });

      if (!response.ok) {
        throw new Error("Failed to save profile changes");
      }

      alert("Profile updated successfully!");
    } catch (err) {
      console.error("Error:", err);
      alert("Error saving profile changes");
    }
  }

  return (
    <div className="p-6 max-w-lg mx-auto">
      <h1 className="text-2xl font-bold mb-4">Edit Your Profile</h1>

      <div className="mb-4">
        <label className="block text-sm font-medium mb-1">Email</label>
        <input
          type="email"
          value={email}
          readOnly
          className="border rounded-md p-2 w-full bg-gray-100 text-gray-500"
        />
      </div>

      <div className="mb-4">
        <label className="block text-sm font-medium mb-1">First Name</label>
        <input
          type="text"
          value={firstName}
          onChange={(e) => setFirstName(e.target.value)}
          className="border rounded-md p-2 w-full"
        />
      </div>

      <div className="mb-4">
        <label className="block text-sm font-medium mb-1">Last Name</label>
        <input
          type="text"
          value={lastName}
          onChange={(e) => setLastName(e.target.value)}
          className="border rounded-md p-2 w-full"
        />
      </div>

      <div className="mb-4">
        <label className="block text-sm font-medium mb-1">Bio</label>
        <textarea
          value={bio}
          onChange={(e) => setBio(e.target.value)}
          className="border rounded-md p-2 w-full"
        />
      </div>

      <div className="mb-4">
        <label className="block text-sm font-medium mb-1">Profile Picture URL</label>
        <input
          type="text"
          value={profilePicture}
          onChange={(e) => setProfilePicture(e.target.value)}
          className="border rounded-md p-2 w-full"
        />
      </div>

      <div className="flex gap-4">
        <button
          onClick={saveProfileChanges}
          className="bg-blue-500 text-white px-4 py-2 rounded-md"
        >
          Save Changes
        </button>
        <button
          onClick={() => navigate("/matching-interface")} // Navigate to the main page
          className="bg-gray-500 text-white px-4 py-2 rounded-md"
        >
          Go to Main Page
        </button>
      </div>
    </div>
  );
}
