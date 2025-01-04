import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { RequestsSection, ScheduledMocksSection, FriendsSection, HistorySection } from "../components/ProfileSections";

export default function MatchingInterface() {
  const [profileData, setProfileData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    async function fetchProfileData() {
      try {
        const response = await fetch("http://127.0.0.1:8000/api/maindata", {
          method: "GET",
          credentials: "include", // Ensure cookies/session is included
        });

        if (!response.ok) {
          throw new Error(`Failed to fetch: ${response.status}`);
        }

        const data = await response.json();
        setProfileData(data);
      } catch (err) {
        console.error("Error:", err);
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }

    fetchProfileData();
  }, []);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error}</p>;

  if (!profileData) return <p>No profile data available.</p>;

  return (
    <div className="p-6 max-w-3xl mx-auto">
      {/* Header with logout and profile picture */}
      <div className="flex justify-between items-center mb-6">
        <button onClick={() => navigate("/")} className="text-gray-600">Log out</button>
        <div className="relative">
          <div className="flex justify-center items-center h-12 w-12 rounded-full bg-gray-300 text-xl font-bold">
            {profileData.google_id[0]} {/* Display first letter of Google ID */}
          </div>
          <button className="absolute top-1/2 transform -translate-y-1/2 left-full ml-4 text-gray-600">settings</button>
        </div>
      </div>

      {/* Profile and warning section */}
      <div className="text-center mb-6">
        <div className="flex justify-center items-center mb-4">
          <div className="h-24 w-24 rounded-full bg-gray-300"></div>
        </div>
        <button onClick={() => navigate("/profile")} className="mt-4 bg-blue-500 text-white px-4 py-2 rounded">
          View Profile
        </button>
      </div>

      <div className="bg-yellow-100 text-yellow-800 p-4 mb-6 rounded-md text-center">
        <p>⚠️ Cannot request new matches when two mocks are pending completion</p>
      </div>

      {/* Sections */}
      <RequestsSection requests={profileData.requests || []} />
      <ScheduledMocksSection scheduledMocks={profileData.scheduled_mocks || []} />
      <FriendsSection friends={profileData.friends || []} />
      <HistorySection history={profileData.history || []} />
    </div>
  );
}
