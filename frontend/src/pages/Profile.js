import { useState, useEffect } from "react";

export default function Profile() {
    const [profileData, setProfileData] = useState(null);
    const [error, setError] = useState("");

    useEffect(() => {
        const fetchProfileData = async () => {
            try {
                const response = await fetch("http://127.0.0.1:8000/profile");
                if (response.ok) {
                    const data = await response.json();
                    setProfileData(data);
                } else {
                    throw new Error("Failed to fetch profile data");
                }
            } catch (error) {
                setError(error.message);
            }
        };

        fetchProfileData();
    }, []);

    if (error) return <p className="text-red-600">{error}</p>;

    return (
        <div className="p-6">
            {profileData ? (
                <div>
                    <h2 className="text-2xl font-bold">{profileData.name}</h2>
                    <p>Age: {profileData.age}</p>
                    <p>Bio: {profileData.bio}</p>
                    <h3 className="text-xl font-semibold mt-4">Interests:</h3>
                    <ul className="list-disc list-inside">
                        {profileData.interests.map((interest, index) => (
                            <li key={index}>{interest}</li>
                        ))}
                    </ul>
                </div>
            ) : (
                <p>Loading profile data...</p>
            )}
        </div>
    );
}
