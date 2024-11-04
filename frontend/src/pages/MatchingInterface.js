import { useNavigate } from "react-router-dom";
import { RequestsSection, ScheduledMocksSection, FriendsSection, HistorySection } from "../components/ProfileSections"; 


export default function MatchingInterface() {
    const navigate = useNavigate();

    return (
        <div className="p-6 max-w-3xl mx-auto">
        {/* Header */}
        <div className="flex justify-between items-center mb-6">
            <button onClick={() => navigate("/")} className="text-gray-600">Log out</button>
            <div className="relative">
                <div className="flex justify-center items-center h-12 w-12 rounded-full bg-gray-300 text-xl font-bold">
                    J
                </div>
                <button className="absolute top-1/2 transform -translate-y-1/2 left-full ml-4 text-gray-600">settings</button>
            </div>
        </div>

        {/* Profile Picture and Edit Profile Button */}
        <div className="text-center mb-6">
            <div className="flex justify-center items-center mb-4">
                <div className="h-24 w-24 rounded-full bg-gray-300"></div>
            </div>
            <button
                onClick={() => navigate("/profile")}
                className="mt-4 bg-blue-500 text-white px-4 py-2 rounded"
            >
                View Profile
            </button>
        </div>

        {/* Notification Banner */}
        <div className="bg-yellow-100 text-yellow-800 p-4 mb-6 rounded-md text-center">
            <p>⚠️ Cannot request new matches when two mocks are pending completion</p>
        </div>

        {/* Sections */}

        <RequestsSection />
        <ScheduledMocksSection />
        <FriendsSection />
        <HistorySection />
    </div>
    );
}

