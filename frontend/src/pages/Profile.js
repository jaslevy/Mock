import React, { useEffect, useState } from "react";

export default function UserProfile() {
    const [profileData, setProfileData] = useState(null);

    useEffect(() => {
        async function fetchUserProfile() {
            try {
                const response = await fetch("http://127.0.0.1:8000/api/profile/user");
                if (!response.ok) throw new Error("Failed to fetch user profile data");
                const data = await response.json();
                setProfileData(data);
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
            <p><strong>Age:</strong> {profileData.age}</p>
            <p><strong>Bio:</strong> {profileData.bio}</p>
            <div>
                <h3 className="font-bold mt-4">Interests:</h3>
                <ul className="list-disc list-inside">
                    {profileData.interests.map((interest, index) => (
                        <li key={index}>{interest}</li>
                    ))}
                </ul>
            </div>
        </div>
    );
}
