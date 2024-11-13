import React, { useEffect, useState } from "react";

export default function UserProfile() {
  const [profileData, setProfileData] = useState(null);

  useEffect(() => {
    async function fetchUserProfile() {
      try {
        // Fetch data from the backend API
        const response = await fetch("http://127.0.0.1:8000/users/");
        if (!response.ok) throw new Error("Failed to fetch user profile data");
        const data = await response.json();

        // Set the first user's profile data
        setProfileData(data[0]); // Assuming you want to display the first user's profile
      } catch (error) {
        console.error("Error:", error);
      }
    }

    fetchUserProfile();
  }, []);

  if (!profileData) return <div>Loading...</div>;

  return (
    <div className="p-6 max-w-lg mx-auto">
      <h1 className="text-2xl font-bold mb-4">{profileData.name}'s Profile</h1>
      <p><strong>Email:</strong> {profileData.email}</p>
      <p><strong>Bio:</strong> {profileData.bio}</p>
    </div>
  );
}
