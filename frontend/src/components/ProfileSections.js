import React, {useState} from "react";

export function RequestsSection({ requests }) {
    return (
        <div className="mb-6">
            <h3 className="text-lg font-bold mb-2">Requests</h3>
            {requests.map(request => (
                <div key={request._id} className="flex items-center bg-gray-100 p-4 rounded-md mb-2">
                    <div className="w-12 h-12 rounded-full bg-blue-300 mr-4">
                        <img src={request.from_user.profile_picture} alt={request.from_user.name} className="w-full h-full rounded-full" />
                    </div>
                    <div className="flex-1">
                        <p>{new Date(request.date).toLocaleDateString()}</p>
                        <p>{request.time}</p>
                        <p>Focus: {request.focus}</p>
                    </div>
                    <button className="bg-green-500 text-white px-4 py-2 rounded-md mr-2">Accept</button>
                    <button className="bg-red-500 text-white px-4 py-2 rounded-md">Reject</button>
                </div>
            ))}
        </div>
    );
}


export function ScheduledMocksSection({ scheduledMocks }) {
    return (
        <div className="mb-6">
            <h3 className="text-lg font-bold mb-2">Scheduled Mocks</h3>
            {scheduledMocks.map(mock => (
                <div key={mock._id} className="flex items-center bg-gray-100 p-4 rounded-md mb-2">
                    <div className="w-12 h-12 rounded-full bg-blue-300 mr-4">
                        <img src={mock.with_user.profile_picture} alt={mock.with_user.name} className="w-full h-full rounded-full" />
                    </div>
                    <div className="flex-1">
                        <p>{new Date(mock.date).toLocaleDateString()}</p>
                        <p>{mock.time}</p>
                        <p>Focus: {mock.focus}</p>
                    </div>
                    <button className="bg-blue-500 text-white px-4 py-2 rounded-md mr-2">Reschedule</button>
                    <button className="bg-red-500 text-white px-4 py-2 rounded-md">Cancel</button>
                </div>
            ))}
        </div>
    );
}

export function FriendsSection({ friends }) {
    return (
        <div className="mb-6">
            <h3 className="text-lg font-bold mb-2">Friends</h3>
            {friends.map(friend => (
                <div key={friend._id} className="flex items-center bg-gray-100 p-4 rounded-md mb-2">
                    <div className="w-12 h-12 rounded-full bg-blue-300 mr-4">
                        <img src={friend.profile_picture} alt={friend.name} className="w-full h-full rounded-full" />
                    </div>
                    <p>{friend.name}</p>
                </div>
            ))}
        </div>
    );
}

export function HistorySection({ history }) {
    const [showAll, setShowAll] = useState(false);
    const historyToShow = showAll ? history : history.slice(0, 2);

    return (
        <div className="mb-6">
            <h3 className="text-lg font-bold mb-2">History</h3>
            {historyToShow.map(session => (
                <div key={session._id} className="flex items-center bg-gray-100 p-4 rounded-md mb-2">
                    <img
                        src={session.with_user.profile_picture}
                        alt={session.with_user.name}
                        className="w-12 h-12 rounded-full mr-4"
                    />
                    <div className="flex-1">
                        <p>{new Date(session.date).toLocaleDateString()}</p>
                        <p>{session.time}</p>
                        <p>Focus: {session.focus}</p>
                    </div>
                    <span className="text-green-500">Completed</span>
                </div>
            ))}
            {history.length > 2 && (
                <button
                    onClick={() => setShowAll(!showAll)}
                    className="text-blue-500 mt-2"
                >
                    {showAll ? "Show Less" : "View More History"}
                </button>
            )}
        </div>
    );
}
