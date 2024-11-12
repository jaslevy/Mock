import React, { useEffect, useState } from "react";

export default function UserProfile() {
  const [profileData, setProfileData] = useState(null);

  useEffect(() => {
    async function fetchUserProfile() {
      try {
        const response = await fetch("http://127.0.0.1:8000/profile/user");
        if (!response.ok) throw new Error("Failed to fetch user profile data");
        const html = await response.text();
        const parser = new DOMParser();
        const doc = parser.parseFromString(html, "text/html");
        const name = doc.querySelector("p:nth-child(2)").textContent.split(":")[1].trim();
        const email = doc.querySelector("p:nth-child(3)").textContent.split(":")[1].trim();
        const bio = doc.querySelector("p:nth-child(4)").textContent.split(":")[1].trim();
        setProfileData({ name, email, bio });
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