import React from "react";

export function RequestsSection() {
    return (
        <div className="mb-6">
            <h3 className="text-lg font-bold mb-2">Requests</h3>
            <div className="flex items-center bg-gray-100 p-4 rounded-md mb-2">
                <div className="w-12 h-12 rounded-full bg-blue-300 mr-4"></div>
                <div className="flex-1">
                    <p>November 7th, 2024</p>
                    <p>12:30 PM</p>
                    <p>Focus: None</p>
                </div>
                <button className="bg-green-500 text-white px-4 py-2 rounded-md mr-2">Accept</button>
                <button className="bg-red-500 text-white px-4 py-2 rounded-md">Reject</button>
            </div>
        </div>
    );
}

export function ScheduledMocksSection() {
    return (
        <div className="mb-6">
            <h3 className="text-lg font-bold mb-2">Scheduled Mocks</h3>
            <div className="flex items-center bg-gray-100 p-4 rounded-md mb-2">
                <div className="w-12 h-12 rounded-full bg-blue-300 mr-4"></div>
                <div className="flex-1">
                    <p>November 4th, 2024</p>
                    <p>2:30 PM</p>
                    <p>Focus: DFS / BFS</p>
                </div>
                <button className="bg-blue-500 text-white px-4 py-2 rounded-md mr-2">Reschedule</button>
                <button className="bg-red-500 text-white px-4 py-2 rounded-md">Cancel</button>
            </div>
            {/* Add more mock items as needed */}
        </div>
    );
}

export function FriendsSection() {
    return (
        <div className="mb-6">
            <h3 className="text-lg font-bold mb-2">Friends</h3>
            <div className="flex items-center bg-gray-100 p-4 rounded-md mb-2">
                <div className="w-12 h-12 rounded-full bg-blue-300 mr-4"></div>
                <p>John Appleseed</p>
            </div>
            {/* Add more friends as needed */}
        </div>
    );
}

export function HistorySection() {
    return (
        <div className="mb-6">
            <h3 className="text-lg font-bold mb-2">History</h3>
            <button className="flex items-center text-gray-700">
                <span className="mr-2">⮟</span> View History
            </button>
        </div>
    );
}